#!/usr/bin/env python3
"""Finite numerical diagnostics; the general theorem is proved in science/.

Run from the repository root: python3 verification/run_all.py
Only NumPy and mpmath are required. No stochastic scientific data are loaded.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import platform
from pathlib import Path

import mpmath as mp
import numpy as np


def require(condition, message):
    if not bool(condition):
        raise AssertionError(message)


def annihilators(n):
    ident = np.eye(2)
    parity = np.diag([1.0, -1.0])
    lower = np.array([[0.0, 1.0], [0.0, 0.0]])
    answer = []
    for j in range(n):
        op = np.ones((1, 1))
        for k in range(n):
            op = np.kron(op, parity if k < j else lower if k == j else ident)
        answer.append(op.astype(complex))
    return answer


def lindblad_matrix(h, jumps):
    """Column-vectorization convention, built independently from populations."""
    d = len(h)
    ident = np.eye(d)
    answer = -1j * (np.kron(ident, h) - np.kron(h.T, ident))
    for ell in jumps:
        q = ell.conj().T @ ell
        answer += np.kron(ell.conj(), ell)
        answer -= (np.kron(ident, q) + np.kron(q.T, ident)) / 2
    return answer


def vec(a):
    return a.reshape(-1, order="F")


def unvec(a, d):
    return a.reshape((d, d), order="F")


def fock_check():
    """Full 3-mode Fock Liouvillian versus the occupation-diagonal formula.

    N=3 is a small algebra check, not a finite example of the N=4M+2 theorem.
    Jordan-Wigner signs, Fourier phases, Hamiltonian and reference blocks are
    retained; no tensor-product factorization of the full fermionic channel
    is assumed.
    """
    n = 3
    d = 2**n
    site = annihilators(n)
    momenta = 2 * np.pi * np.arange(n) / n
    modes = [sum(np.exp(-1j * k * x) * site[x] for x in range(n)) / np.sqrt(n)
             for k in momenta]
    nums = [c.conj().T @ c for c in modes]
    eye = np.eye(d)
    a = np.array([0.81, 0.19, 0.27])
    b = np.array([0.12, 0.71, 0.63])
    g = a + b
    desired = np.array([1, 0, 0])
    pi = np.where(desired, a / g, b / g)
    finf = float(np.prod(pi))
    target_bits = [nums[j] if desired[j] else eye - nums[j] for j in range(n)]
    target = eye.copy()
    for p in target_bits:
        target = target @ p
    h = sum(e * q for e, q in zip([0.17, -0.32, 0.61], nums))
    modal_jumps = ([np.sqrt(a[j]) * modes[j].conj().T for j in range(n)]
                   + [np.sqrt(b[j]) * modes[j] for j in range(n)])
    # Unitary Fourier mixing of physical translated jump labels.
    physical = []
    for x in range(n):
        physical.append(sum(np.exp(1j * momenta[j] * x) * modal_jumps[j]
                            for j in range(n)) / np.sqrt(n))
        physical.append(sum(np.exp(-1j * momenta[j] * x) * modal_jumps[n + j]
                            for j in range(n)) / np.sqrt(n))
    liou = lindblad_matrix(h, physical)
    modal = lindblad_matrix(h, modal_jumps)
    mixing_error = float(np.max(np.abs(liou - modal)))
    require(mixing_error < 2e-14, "Fourier jump-label mixing failed")
    eig, basis = np.linalg.eig(liou)
    inverse = np.linalg.inv(basis)
    condition = float(np.linalg.cond(basis))
    require(condition < 1e5, "Small-Liouvillian eigendecomposition is ill-conditioned")

    def channel(rho, time):
        return unvec(basis @ (np.exp(time * eig) * (inverse @ vec(rho))), d)

    # Correlated even-parity mixture is non-Gaussian: <n0 n1> != <n0><n1>.
    vacuum = np.zeros(d, dtype=complex)
    vacuum[0] = 1
    pair = modes[0].conj().T @ modes[1].conj().T @ vacuum
    pair /= np.linalg.norm(pair)
    branch = [vacuum, pair]
    non_gaussian = (np.outer(vacuum, vacuum.conj()) + np.outer(pair, pair.conj())) / 2
    wick_defect = float(np.real(np.trace(non_gaussian @ nums[0] @ nums[1])
                                    - np.trace(non_gaussian @ nums[0])
                                    * np.trace(non_gaussian @ nums[1])))
    require(abs(wick_defect) > 0.2, "Input did not test non-Gaussian correlations")
    worst = eye.copy()
    for p in target_bits:
        worst = worst @ (eye - p)
    require(abs(np.trace(worst) - 1) < 2e-14, "Complementary Fock projector rank failed")
    worst_effect_error = 0.0
    population_error = 0.0
    reference_error = 0.0
    reference_min_eig = 1.0
    trace_error = 0.0
    row_checks = []
    for time in [0.0, 0.09, 0.7, 2.0, 6.0]:
        propagator = basis @ np.diag(np.exp(time * eig)) @ inverse
        heisenberg = unvec(propagator.conj().T @ vec(target), d)
        expected_effect = eye.copy()
        for j, p in enumerate(target_bits):
            decay = math.exp(-g[j] * time)
            expected_effect = expected_effect @ (pi[j] * (1 - decay) * eye + decay * p)
        effect_error = float(np.max(np.abs(heisenberg - expected_effect)))
        worst_effect_error = max(worst_effect_error, effect_error)
        exact_worst = finf * float(np.prod(-np.expm1(-g * time)))
        actual_worst = float(np.real(np.trace(target @ channel(worst, time))))
        minimum = float(np.linalg.eigvalsh((heisenberg + heisenberg.conj().T) / 2)[0])
        require(abs(minimum - exact_worst) < 3e-12, "Minimum over all input states failed")
        require(abs(actual_worst - exact_worst) < 3e-12, "Complementary input not minimizing")
        for j, nj in enumerate(nums):
            output = float(np.real(np.trace(nj @ channel(non_gaussian, time))))
            initial = float(np.real(np.trace(nj @ non_gaussian)))
            expected = a[j] / g[j] + (initial - a[j] / g[j]) * math.exp(-g[j] * time)
            population_error = max(population_error, abs(output - expected))
        # Entangled spectator reference; apply the full system map to each
        # off-diagonal reference block, preserving system-reference coherence.
        output_sr = np.zeros((2 * d, 2 * d), dtype=complex)
        for r in range(2):
            for s in range(2):
                block = np.outer(branch[r], branch[s].conj()) / 2
                output_sr[r*d:(r+1)*d, s*d:(s+1)*d] = channel(block, time)
        reduced = output_sr[:d, :d] + output_sr[d:, d:]
        reference_error = max(reference_error, float(np.max(np.abs(reduced - channel(non_gaussian, time)))))
        reference_min_eig = min(reference_min_eig, float(np.linalg.eigvalsh((output_sr + output_sr.conj().T)/2)[0]))
        trace_error = max(trace_error, abs(float(np.real(np.trace(output_sr))) - 1))
        reference_overlap = np.real(np.trace(np.kron(np.eye(2), target) @ output_sr))
        require(abs(reference_overlap - np.trace(expected_effect @ non_gaussian)) < 4e-12,
                "Reference-entangled input population identity failed")
        row_checks.append({"time": time, "worst_overlap": exact_worst,
                           "effect_operator_error": effect_error})
    require(worst_effect_error < 4e-12, "Target Heisenberg operator did not factor on diagonal algebra")
    require(population_error < 3e-12, "Exact occupation equations failed")
    require(reference_error < 2e-12 and reference_min_eig > -3e-12 and trace_error < 3e-12,
            "Spectator-reference channel check failed")
    return {"modes": n, "full_liouville_dimension": d*d,
            "finite_theorem_grid": False, "fourier_mixing_error": mixing_error,
            "eigenbasis_condition": condition, "non_gaussian_wick_defect": wick_defect,
            "max_effect_error": worst_effect_error, "max_population_error": population_error,
            "reference_reduction_error": reference_error,
            "minimum_reference_output_eigenvalue": reference_min_eig,
            "max_trace_error": trace_error, "curves": row_checks}


def filter_parameter(n, epsilon):
    kappa = -math.log(math.tanh(0.5))
    return math.ceil(max(2, math.log(n / 2) + 1,
                         1 + math.log(4*n/epsilon)/(2*kappa)))


def filter_log_rates(n, epsilon):
    s = filter_parameter(n, epsilon)
    roots = np.exp(-np.arange(s*s) / s)
    normalizer = np.log1p(roots).sum()
    x = np.cos(2 * np.pi * np.arange(n) / n)
    # Direct log products avoid catastrophic coefficient cancellation near
    # the Fermi points. These are ideal, unrounded construction rates.
    with np.errstate(divide="ignore"):
        plus = np.log(np.abs(x[:, None] + roots[None, :])).sum(axis=1) - normalizer
        minus = np.log(np.abs(-x[:, None] + roots[None, :])).sum(axis=1) - normalizer
    loga = 2 * plus - math.log(2)
    logb = 2 * minus - math.log(2)
    logg = np.logaddexp(loga, logb)
    correct = np.where(x > 0, loga, logb)
    wrong = np.where(x > 0, logb, loga)
    log_finfty = -float(np.logaddexp(0, wrong - correct).sum())
    return s, logg, log_finfty


def log_worst_overlap(logtime, logg, logfinf):
    x = logg + logtime
    terms = np.empty_like(x)
    tiny = x < -30
    large = x > math.log(45)
    middle = ~(tiny | large)
    terms[tiny] = x[tiny]  # relative correction below 5e-14 per tiny factor
    terms[large] = 0.0    # discarded absolute log correction below 3e-20
    terms[middle] = np.log(-np.expm1(-np.exp(x[middle])))
    return logfinf + float(terms.sum())


def geometric_checks():
    epsilon = 0.1
    wanted = 0.9
    rows = []
    for n in [66, 258, 1026, 4098, 16386]:
        s, logg, logfinf = filter_log_rates(n, epsilon)
        finf = math.exp(logfinf)
        require(finf >= 1 - epsilon/4 - 2e-12, "Ideal stationary fidelity guarantee failed")
        require(float(logg.max()) <= 3e-13, "Discrete-grid Gamma normalization failed")
        require(np.isfinite(logg).all(), "Construction lost a positive occupation rate")
        gap = 1 - wanted/finf
        lower = -float(logg.min()) + math.log(-math.log(gap))
        upper = -float(logg.min()) + math.log(math.log(n/gap))
        require(log_worst_overlap(lower, logg, logfinf) <= math.log(wanted) + 2e-11,
                "Minimum-rate lower time bracket failed")
        require(log_worst_overlap(upper, logg, logfinf) >= math.log(wanted) - 2e-11,
                "Union-bound upper time bracket failed")
        for _ in range(80):
            middle = (lower + upper)/2
            if log_worst_overlap(middle, logg, logfinf) < math.log(wanted):
                lower = middle
            else:
                upper = middle
        logtime = (lower + upper)/2
        require(abs(log_worst_overlap(logtime, logg, logfinf) - math.log(wanted)) < 3e-10,
                "Worst-input product root did not converge")
        # Independent 80-digit minimum-rate calculation at sin(pi/N).
        with mp.workdps(80):
            x = mp.sin(mp.pi/n)
            roots = [mp.exp(-mp.mpf(j)/s) for j in range(s*s)]
            norm = mp.fsum(mp.log1p(r) for r in roots)
            lp = mp.fsum(mp.log(x+r) for r in roots) - norm
            lm = mp.fsum(mp.log(abs(-x+r)) for r in roots) - norm
            oracle_min = mp.log((mp.exp(2*lp)+mp.exp(2*lm))/2)
            minimum_error = abs(float(oracle_min) - float(logg.min()))
        require(minimum_error < 2e-8, "High-precision minimum rate disagreed")
        rows.append({"sites": n, "s": s, "formal_radius": s*s,
                     "stationary_overlap": finf, "stationary_log_overlap": logfinf,
                     "stationary_infidelity": -math.expm1(logfinf),
                     "log_inverse_minimum_rate": -float(logg.min()),
                     "log_worst_time_to_overlap_0.9": logtime,
                     "log_time_over_logN_cubed": logtime/math.log(n)**3,
                     "mp_minimum_log_rate_error": minimum_error,
                     "formal_radius_exceeds_half_ring": s*s > n/2})
    # Large sizes use the nearest-mode rate only. They are NOT evaluations
    # of all N mode factors or full preparation times.
    large = []
    with mp.workdps(90):
        for power in [2, 4, 8, 16, 32]:
            n = 4 * 10**power + 2
            s = filter_parameter(n, epsilon)
            x = mp.sin(mp.pi/n)
            roots = [mp.exp(-mp.mpf(j)/s) for j in range(s*s)]
            norm = mp.fsum(mp.log1p(r) for r in roots)
            lp = mp.fsum(mp.log(x+r) for r in roots)-norm
            lm = mp.fsum(mp.log(abs(-x+r)) for r in roots)-norm
            log_inverse = -mp.log((mp.exp(2*lp)+mp.exp(2*lm))/2)
            big_l = mp.log(1/x)
            total = mp.fsum(min(mp.mpf(j)/s, big_l) for j in range(s*s))
            require(2*total-4*(s+1) <= log_inverse + mp.mpf('1e-65'),
                    "Lower finite geometric-sum bracket failed")
            require(log_inverse <= 2*total+2*(s+1)+mp.log(2)+mp.mpf('1e-65'),
                    "Upper finite geometric-sum bracket failed")
            large.append({"sites_exact_integer": str(n), "s": s,
                          "log_inverse_minimum_rate": float(log_inverse),
                          "log_inverse_rate_over_logN_cubed": float(log_inverse/mp.log(n)**3),
                          "scope": "nearest-mode rate only; not full-grid time"})
    return {"epsilon_parameter": epsilon, "target_overlap": wanted,
            "rates": "ideal unrounded geometric-root construction; Gamma=1",
            "finite_product_curves": rows, "large_size_minimum_rates": large}


def ceil_cuberoot(n):
    """Exact integer arithmetic, including sizes far beyond double precision."""
    a = 1 << ((n.bit_length()+2)//3)
    while True:
        next_a = (2*a + n//(a*a))//3
        if next_a >= a:
            break
        a = next_a
    return a + (a*a*a < n)


def tangent_grid(n):
    a = ceil_cuberoot(n)
    b = n//8
    ids = np.arange(a-1, b+2)
    x = np.tan((ids+0.5)*np.pi/n)
    return a, b, x


def deleted_nodes(r, a, b, x):
    if r < x[0] or r >= x[-1]:
        return set()
    ell = int(np.searchsorted(x, r, side="right") - 1) + a - 1
    return {j for j in [ell, ell+1] if a <= j <= b}


def root_diagnostics():
    c0 = math.pi**2/2
    c1 = 3.5*float(mp.zeta(3))
    rows = []
    for n in [1026, 4098, 16386]:
        a, b, outer = tangent_grid(n)
        x = outer[1:-1]
        weights = np.diff(np.log(outer))[1:]
        lcap = math.log(1/outer[0])
        require(np.all(np.diff(np.diff(np.log(outer))) <= 2e-14),
                "Logarithmic grid weights were not decreasing")
        centre = float(x[len(x)//2])
        roots = [0j, 1j*centre, centre+0j, -centre+0j,
                 centre*(1+1e-12)+0j, centre*(1-1e-12)+0j,
                 centre+1e-14j*centre, centre+0.2j*centre,
                 0.1*float(x[0])+0j, float(outer[0])+0j,
                 float(outer[-1])+0j, 0.01+0.2j, 2+0j, 1e-100+0j, 1e100+0j]
        max_unweighted = 0.0
        max_weighted_fraction = 0.0
        cases = []
        for z in roots:
            r = abs(z)
            deleted = deleted_nodes(r, a, b, outer)
            keep = np.array([j not in deleted for j in range(a, b+1)])
            nodes = x[keep]
            if z == 0 or z.real == 0:
                kernel = np.zeros(len(nodes))
            else:
                # log1p form avoids cancellation for extremely small/large roots.
                alpha = abs(z.real)
                rr = abs(z)
                ratio = 2*alpha*nodes/(nodes*nodes+rr*rr)
                ratio = np.minimum(ratio, 1-np.finfo(float).eps)
                kernel = np.arctanh(ratio)
            unweighted = float(np.dot(weights[keep], kernel))
            weighted = float(np.dot(weights[keep]*np.log(1/nodes), kernel))
            clipped = lcap if r == 0 else min(max(math.log(1/r), 0), lcap)
            bound = c0*clipped + c1 + c0*float(weights[0])
            require(unweighted <= c0+5e-12, "Root deletion unweighted integral budget failed")
            require(weighted <= bound+2e-10, "Weighted clipped root budget failed")
            require(np.isfinite(weighted), "A real sample pole was not removed")
            max_unweighted = max(max_unweighted, unweighted)
            max_weighted_fraction = max(max_weighted_fraction, weighted/bound)
            cases.append({"root_real": z.real, "root_imag": z.imag,
                          "deleted_count": len(deleted), "weighted_sum": weighted,
                          "finite_upper_bound": bound})
        rows.append({"sites": n, "selected_nodes": len(x), "a": a, "b": b,
                     "clip_ell": float(outer[0]), "clip_L": lcap,
                     "tested_roots": len(roots), "maximum_unweighted_sum": max_unweighted,
                     "unweighted_budget": c0, "maximum_weighted_bound_fraction": max_weighted_fraction,
                     "adversarial_cases": cases})
    # Non-finite undeleted pole is deliberately present: deleting nearby
    # nodes is necessary, rather than a numerical convenience.
    return {"grids": rows, "undeleted_exact_sample_pole": "infinite; excluded before kernel evaluation",
            "scope": "finite root/pole diagnostics, not proof of the all-root bound"}


def clipping_jensen_diagnostics():
    """Test root geometry and complex growth against adversarial polynomials."""
    records = []
    for n in [4098, 65538, 1048578]:
        a, _, outer = tangent_grid(n)
        xa = float(outer[0])
        lcap = math.log(1/xa)
        require(xa <= 1/16, "The finite Jensen disk condition failed")
        roots = [0j, xa/20+0j, xa/2+0j, xa+0j, 2*xa+0j,
                 xa*(1+1e-12)+1e-15j, 0.03+0.04j, 0.1249+0j,
                 0.1251+0j, 0.5+0j, 2+0j, -xa+0j]
        minimum_margin = math.inf
        for point in [-xa, -xa/4, 0, xa/4, xa]:
            for z in roots:
                r = abs(z)
                clip = lcap if r == 0 else min(max(math.log(1/r), 0), lcap)
                if r < 1/8:
                    distance = abs(z-point)
                    if distance == 0:
                        continue  # P(point)=0 gives the attenuation bound directly.
                    lhs = math.log(0.25/distance)
                    rhs = clip-math.log(8)
                    minimum_margin = min(minimum_margin, lhs-rhs)
                    require(lhs+1e-13 >= rhs, "Clipped near-root Jensen geometry failed")
                else:
                    require(clip <= math.log(8)+1e-13, "Far-root clipping correction failed")
        records.append({"sites": n, "clip_ell_x_a_minus_1": xa,
                        "minimum_near_root_margin": minimum_margin,
                        "root_cases": len(roots), "evaluation_points": 5,
                        "center_range": "entire allowed [-ell,ell], including endpoints"})
    # Positive polynomials (T_m(x)+a)^2 have strongly cancelling monomials
    # but a known exact real-interval supremum. Check the elementary
    # Chebyshev complex-growth bound on a fixed disk.
    growth = []
    theta = np.linspace(0, 2*np.pi, 2049)
    z = 0.5*np.exp(1j*theta)
    for degree in [2, 4, 8, 16]:
        for shift in [0.0, 0.17, 1.1]:
            coeff = np.zeros(degree+1)
            coeff[-1] = 1
            values = (np.polynomial.chebyshev.chebval(z, coeff)+shift)**2
            real_sup = (1+abs(shift))**2
            pdegree = 2*degree
            ratio = float(np.max(np.abs(values)))/real_sup
            bound = 2.0**(pdegree+2)
            require(ratio <= bound*(1+1e-13), "Complex Chebyshev growth bound failed")
            growth.append({"polynomial_degree": pdegree, "shift": shift,
                           "complex_max_over_real_sup": ratio, "finite_bound": bound})
    return {"clipping_geometry": records, "complex_growth": growth,
            "scope": "finite geometric diagnostics; no polynomial-root certification"}


def finite_certificate_diagnostics():
    """Evaluate the exact final finite bound, including vacuous small rows.

    Stable elementary expressions are used when N is astronomically large:
    log(tan(t+h)/tan(t)) is evaluated by log1p(sin(h)/(sin(t)cos(t+h))).
    The cube-root grid index itself is computed in exact integer arithmetic.
    These rows are mathematical bound diagnostics, not physical simulations.
    """
    rows = []
    with mp.workdps(100):
        f = mp.mpf('0.9')
        ef = -mp.log(f)
        chi = -mp.log1p(-f)
        c0 = mp.pi**2/2
        c1 = mp.mpf('3.5')*mp.zeta(3)
        m = int(mp.floor(4*ef))+1
        limiting = 4/(27*mp.pi**2)
        for power in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
            n = 4*10**power+2
            a = ceil_cuberoot(n)
            b = n//8
            logn = mp.log(n)
            radius = int(mp.ceil(2*logn**2))
            h = mp.pi/n
            ta = (mp.mpf(a)+mp.mpf('.5'))*h
            x_ell = mp.tan((mp.mpf(a)-mp.mpf('.5'))*h)
            nu_a = -mp.log(mp.tan(ta))
            nu_end = -mp.log(mp.tan((mp.mpf(b)+mp.mpf('1.5'))*h))
            w = mp.log1p(mp.sin(h)/(mp.sin(ta)*mp.cos(ta+h)))
            u = w*nu_a
            total = (nu_a**2-nu_end**2)/2
            delta = mp.exp(-logn/3)
            lam = 2*(mp.log1p(-delta)-mp.log(delta))
            z = max(mp.mpf(0), lam*(total-u*(16*radius+ef/delta))
                    - 8*radius*(c1+c0*w))/c0
            log_lower = mp.log(3*chi/32)+z/2-18*radius*mp.log(2)
            conditions = {"N_at_least_1026": n >= 1026,
                          "ell_at_most_1_over_16": x_ell <= mp.mpf(1)/16,
                          "good_mode_count_at_most_a": m <= a,
                          "sampling_condition": 2*mp.pi*radius/n <= mp.mpf('.5')}
            valid = all(conditions.values())
            rows.append({"N_decimal_exponent": power, "N_exact_description": f"4*10^{power}+2",
                         "radius": radius, "radius_rule": "ceil(2(log N)^2)",
                         "conditions": conditions, "finite_bound_applies": valid,
                         "Z": float(z), "formula_log_Gamma_time_value": float(log_lower),
                         "log_Gamma_time_lower_bound": float(log_lower) if valid else None,
                         "lower_log_time_over_logN_cubed": float(log_lower/logn**3) if valid else None,
                         "asymptotic_lower_coefficient": float(limiting),
                         "scope": "necessary bound evaluation; no assertion radius is feasible"})
        require(rows[-1]["finite_bound_applies"], "Large finite certificate conditions failed")
        require(0 < rows[-1]["lower_log_time_over_logN_cubed"] < float(limiting),
                "Large-size finite certificate did not enter the nonvacuous regime")
    return {"target_overlap": 0.9, "rows": rows,
            "scope": "100-digit elementary finite-bound evaluations, not interval certificates"}


def sampled_normalization_diagnostics():
    records = []
    for n in [66, 258, 1026]:
        for radius in [1, 2, 4]:
            # A narrow positive peak intentionally centred between grid nodes.
            offsets = np.arange(-radius, radius+1)
            peak = np.pi/n
            coefficients = np.exp(-1j*offsets*peak)/(2*radius+1)
            grid = 2*np.pi*np.arange(n)/n
            fine = np.linspace(0, 2*np.pi, 32769)
            rate_grid = np.abs(np.exp(1j*grid[:, None]*offsets)@coefficients)**2
            rate_fine = np.abs(np.exp(1j*fine[:, None]*offsets)@coefficients)**2
            discrete_sup = float(rate_grid.max())
            observed_continuous = max(1.0, float(rate_fine.max()))
            sampling_factor = 2*radius*np.pi/n
            bound = discrete_sup/(1-sampling_factor)
            require(observed_continuous <= bound+2e-13, "Finite-grid Bernstein correction failed")
            records.append({"sites": n, "jump_radius": radius,
                            "grid_sup": discrete_sup, "known_continuous_sup": 1.0,
                            "Bernstein_corrected_bound": bound})
    return {"between_node_peaks": records,
            "scope": "positive trig-polynomial sampling diagnostics"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="verification/results.json")
    args = parser.parse_args()
    report = {"schema_version": 1,
              "checked_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "environment": {"python": platform.python_version(), "numpy": np.__version__,
                              "mpmath": mp.__version__},
              "status": "passed", "randomness": "none",
              "scientific_limit": "Finite numerical diagnostics do not prove asymptotics, arbitrary-root inequalities, or literature priority.",
              "fock_lindblad": fock_check(),
              "geometric_root_construction": geometric_checks(),
              "weighted_root_deletion": root_diagnostics(),
              "clipping_jensen": clipping_jensen_diagnostics(),
              "finite_temporal_certificate": finite_certificate_diagnostics(),
              "grid_normalization": sampled_normalization_diagnostics()}
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"status": report["status"], "report": str(path),
                      "fock_effect_error": report["fock_lindblad"]["max_effect_error"],
                      "finite_construction_sizes": [r["sites"] for r in report["geometric_root_construction"]["finite_product_curves"]],
                      "root_grids": [r["sites"] for r in report["weighted_root_deletion"]["grids"]]}, indent=2))


if __name__ == "__main__":
    main()
