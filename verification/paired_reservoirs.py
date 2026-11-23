"""Finite two-mode check of the pairing extension for Fermi-sea preparation."""

import json

import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov


def adj(matrix):
    return matrix.conj().T


def lindblad(rho, hamiltonian, jumps):
    derivative = -1j * (hamiltonian @ rho - rho @ hamiltonian)
    for jump in jumps:
        rate = adj(jump) @ jump
        derivative += jump @ rho @ adj(jump) - (rate @ rho + rho @ rate) / 2
    return derivative


def correlation(rho, fields):
    return np.array([
        [np.trace(rho @ adj(right) @ left) for right in fields]
        for left in fields
    ])


def majorana_covariance(rho, fields):
    return 1j * (np.array([
        [np.trace(rho @ left @ adj(right)) for right in fields]
        for left in fields
    ]) - np.eye(2))


def projector(vector):
    return np.outer(vector, vector.conj())


def mixed_vectors(rng, count):
    vectors = rng.normal(size=(2, count)) + 1j * rng.normal(size=(2, count))
    return vectors / (2 * np.sqrt(count))


def minimum_eigenvalue(matrix):
    return np.linalg.eigvalsh((matrix + adj(matrix)) / 2).min()


def run():
    rng = np.random.default_rng(20261123)
    annihilator = np.array([[0, 1], [0, 0]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    parity_one = np.diag([1, -1])
    c_k = np.kron(annihilator, identity)
    c_minus_k = np.kron(parity_one, annihilator)
    nambu = np.array([c_k, adj(c_minus_k)])
    majoranas = np.array([nambu[0] + nambu[1], -1j * (nambu[0] - nambu[1])])
    transform = np.array([[1, 1j], [1, -1j]]) / np.sqrt(2)
    parity = np.kron(parity_one, parity_one)
    zero, nambu_vacuum, _, full = np.eye(4)
    pair_targets = [projector(zero), projector(full)]
    maxima = dict(mapping=0.0, derivative=0.0, rho_trace=0.0,
                  parity=0.0, stationary_residual=0.0)
    minima = dict(stationary_psd=np.inf, stationary_upper=np.inf,
                  gain_inequality=np.inf, loss_inequality=np.inf,
                  unwanted_rate_slack=np.inf, even_parity_slack=np.inf)

    coherent_scales = (0.0, 1.0, 1e4, 1e8)
    for coherent_scale in coherent_scales:
        for _ in range(16):
            gain_vectors = mixed_vectors(rng, 3)
            loss_vectors = mixed_vectors(rng, 3)
            gain = gain_vectors @ adj(gain_vectors)
            loss = loss_vectors @ adj(loss_vectors)
            dissipation = gain + loss
            jumps = [
                sum(vector[i] * adj(nambu[i]) for i in range(2))
                for vector in gain_vectors.T
            ] + [
                sum(vector[i].conj() * nambu[i] for i in range(2))
                for vector in loss_vectors.T
            ]
            pairing = coherent_scale * np.exp(1j * rng.uniform(-np.pi, np.pi))
            h = np.array([[0.37, pairing], [pairing.conj(), -0.24]])
            hamiltonian = sum(h[i, j] * adj(nambu[i]) @ nambu[j]
                              for i in range(2) for j in range(2))
            drift = -1j * h - dissipation / 2

            sample = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
            rho = sample @ adj(sample)
            rho = (rho + parity @ rho @ parity) / (2 * np.trace(rho))
            nambu_cov = correlation(rho, nambu)
            cov = majorana_covariance(rho, majoranas)
            cov_minus = majorana_covariance(rho, np.array([adj(w) for w in majoranas]))
            occupation_minus = np.trace(rho @ adj(c_minus_k) @ c_minus_k)
            occupation_k = 0.5 + (cov[0, 1] - cov[1, 0] + 1j * np.trace(cov)) / 4
            mapped = transform @ (identity + 1j * cov) @ adj(transform) / 2
            maxima['mapping'] = max(maxima['mapping'], np.max(np.abs(mapped - nambu_cov)),
                                    np.max(np.abs(cov_minus + cov.T)),
                                    abs(occupation_k - nambu_cov[0, 0]),
                                    abs(occupation_minus - (1 - nambu_cov[1, 1])))

            derivative_exact = correlation(lindblad(rho, hamiltonian, jumps), nambu)
            derivative_formula = drift @ nambu_cov + nambu_cov @ adj(drift) + gain
            scale = max(1.0, np.linalg.norm(derivative_exact, ord='fro'))
            maxima['derivative'] = max(maxima['derivative'],
                                       np.max(np.abs(derivative_exact - derivative_formula)) / scale)

            stationary = solve_continuous_lyapunov(drift, -gain)
            residual = np.max(np.abs(drift @ stationary + stationary @ adj(drift) + gain))
            maxima['stationary_residual'] = max(maxima['stationary_residual'], residual)
            total = np.trace(dissipation).real
            minima['stationary_psd'] = min(minima['stationary_psd'], minimum_eigenvalue(stationary))
            minima['stationary_upper'] = min(minima['stationary_upper'], minimum_eigenvalue(identity - stationary))
            minima['gain_inequality'] = min(minima['gain_inequality'], minimum_eigenvalue(total * stationary - gain))
            minima['loss_inequality'] = min(minima['loss_inequality'], minimum_eigenvalue(total * (identity - stationary) - loss))
            for occupied in (0, 1):
                empty = 1 - occupied
                wrong_occupation = (1 - stationary[occupied, occupied] + stationary[empty, empty]).real
                wrong_rate = (loss[occupied, occupied] + gain[empty, empty]).real
                slack = wrong_occupation - wrong_rate / total
                minima['unwanted_rate_slack'] = min(minima['unwanted_rate_slack'], slack)

            odd_input = projector(nambu_vacuum)
            even_projector = sum(pair_targets)
            assert np.trace(even_projector @ odd_input) == 0
            matrix_units = np.eye(16).reshape((16, 4, 4))
            superoperator = np.column_stack([
                lindblad(unit, hamiltonian, jumps).ravel() for unit in matrix_units
            ])
            for dimensionless_time in (0.05, 0.2, 1.0, 3.0):
                time = dimensionless_time / total
                channel = expm(time * superoperator)
                state = (channel @ odd_input.ravel()).reshape((4, 4))
                maxima['rho_trace'] = max(maxima['rho_trace'], abs(np.trace(state) - 1))
                maxima['parity'] = max(maxima['parity'], np.max(np.abs(parity @ state - state @ parity)))
                even_weight = np.trace(even_projector @ state).real
                slack = -np.expm1(-dimensionless_time) - even_weight
                minima['even_parity_slack'] = min(minima['even_parity_slack'], slack)

    assert maxima['mapping'] < 1e-12
    assert maxima['derivative'] < 1e-12
    assert maxima['parity'] < 1e-12
    assert maxima['stationary_residual'] < 2e-7
    assert maxima['rho_trace'] < 2e-6
    assert min(minima.values()) >= -2e-6
    return {
        "seed": 20261123,
        "pairs": 16 * len(coherent_scales),
        "times_per_pair": 4,
        "pairing_amplitudes": coherent_scales,
        "maximum_errors": {name: float(value) for name, value in maxima.items()},
        "minimum_margins": {name: float(value) for name, value in minima.items()},
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, allow_nan=False))
