# Reproduce the finite checks

Run from the repository root with Python 3.11 or newer:

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/run_all.py
```

The command writes [results.json](results.json). A different destination can be supplied with `--output PATH`. The suite has no random inputs and normally takes a few seconds. The report records the interpreter and dependency versions used.

## What is checked

| Diagnostic | Independent calculation | Scope |
|---|---|---|
| Occupation dynamics and target overlap | A full Jordan–Wigner Fock-space Lindblad matrix, including Fourier jump-label mixing and a number-conserving Hamiltonian, is exponentiated and compared with the population equations. | Three modes, five times, including a correlated non-Gaussian input. Three modes is an algebra check, rather than an example on the theorem's $`N=4M+2`$ grid. |
| Worst input | The smallest eigenvalue of the evolved target projector is compared with the complementary Fock input and the full product formula. | A matrix calculation over every input state in the small system, rather than sampling a few Gaussian inputs. |
| Spectator reference | The full small-system channel is applied to diagonal and off-diagonal blocks of a system–reference entangled state. | Checks positivity, trace, reduction and target population. This does not assert a new diamond-distance preparation theorem. |
| Geometric-root construction | Direct logarithmic products over all momenta are compared with an independent 80-digit nearest-mode calculation, and the worst-input overlap equation is solved in logarithmic time. | Ideal unrounded filters at $`N=66,258,1026,4098,16386`$. |
| Large-size rate exponent | High-precision nearest-mode rates are bracketed by the explicit geometric-root sums. | Sizes through $`4\times10^{32}+2`$; only the minimum occupation rate is evaluated at these sizes. These rows are not full-grid time calculations. |
| Weighted root argument | Root deletion and the clipped weighted kernel bound are evaluated on the tangent grid. | Real sample poles, almost coincident roots, negative roots, imaginary and nonreal roots, roots near the window boundaries, and very small or large roots. |
| Clipping and normalization | Near-root Jensen geometry, Chebyshev complex growth, and finite-grid Bernstein sampling are checked separately. | Includes positive polynomials with cancelling monomials and positive trigonometric peaks centred between sample nodes. |
| Final finite certificate | The exact $`Z_N(R,f)`$ and logarithmic time bound are evaluated with 100-digit arithmetic and exact integer cube-root grid indices. | Includes failed-condition and weak finite rows rather than treating the asymptotic theorem as a useful small-size numerical bound. |

The full-channel calculation does not factor the fermionic channel into ordinary qubit channels. Only the commuting occupation algebra has the product evolution used in the theorem. Jordan–Wigner signs remain in the matrix calculation.

## Recorded results

The checked environment was Python 3.12.14, NumPy 2.3.5 and mpmath 1.3.0. The full Fock-space target-effect comparison had maximum absolute entry error below $`4\times10^{-15}`$; occupation errors were below $`2\times10^{-15}`$. The non-Gaussian input has connected occupation correlation $`1/4`$. Small negative output eigenvalues of order $`10^{-16}`$ are numerical roundoff.

The root diagnostics use the converse's final window $`a=\lceil N^{1/3}\rceil`$ and clipping point $`\ell=x_{a-1}`$. The Jensen geometry rows test five centers across the full allowed $`[-\ell,\ell]`$ range, including its endpoints, under $`\ell\le1/16`$. The finite-certificate rows use the final $`m=\lfloor4E_f\rfloor+1`$, $`Z_N(R,f)`$ and sampling conditions directly from [the temporal converse](../science/time_converse.md); no earlier auxiliary near-Fermi scale is used.

For the ideal geometric-root filter with parameter $`\epsilon=0.1`$ and requested all-input target overlap $`0.9`$:

| Sites | $`s`$ | Formal radius $`s^2`$ | $`\log(\Gamma/g_{\min})`$ | $`\log(\Gamma t_{\mathrm{worst}})`$ |
|---:|---:|---:|---:|---:|
| 66 | 7 | 49 | 221.22287 | 222.51754 |
| 258 | 7 | 49 | 282.67934 | 283.97402 |
| 1026 | 8 | 64 | 457.16212 | 458.45680 |
| 4098 | 9 | 81 | 681.32620 | 682.62087 |
| 16386 | 11 | 121 | 1242.17069 | 1243.46536 |

All logarithms are natural. At $`N=66`$ the formal radius exceeds half the ring; periodic offsets can be combined. That row checks dynamics and conventions, rather than an efficient finite-size design. Integer jumps in $`s`$ make finite ratios with $`(\log N)^3`$ nonmonotone. The very large nearest-mode rows approach the leading coefficient one without constituting a proof of that limit.

The construction's stationary infidelity is very small in these examples. The displayed floating-point overlap can round to one; `stationary_log_overlap` and `stationary_infidelity` in the report retain the small error instead of asserting exact purity.

## Numerical and scientific limits

The suite uses floating-point and arbitrary-precision numerical arithmetic, rather than interval certificates. It computes the ideal product filter directly, without synthesizing or rounding its Fourier coefficients. The finite-precision construction and its inherited rounding theorem are mathematical statements; this suite does not certify a particular rounded hardware coefficient list.

Times are represented by their logarithms because the rates are too small to use ordinary floating-point elapsed times. Stable logarithms of the product factors avoid overflow and underflow. The asymptotic theorem, arbitrary-root inequalities, arbitrary family count and literature comparison rest on the written scientific arguments. These finite checks target consequential conventions and examples; they do not prove those universal claims or certify publication priority.

The upper construction and its parameter choice are inherited from [Fermi-Sea-Reservoir-Locality](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/tree/293b8e6914d8ff85ed3605d6c85dc95abfef4b61), especially its `science/reservoir_construction.md` and `science/preparation_costs.md`. The optimization-over-reservoirs temporal converse is the subject of this repository.
