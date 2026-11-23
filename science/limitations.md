# Scope of the preparation-time laws

## The allowed reservoir

The [paired theorem](paired_reservoirs.md) treats one fermionic mode per site on a ring, with one-site translation invariance, a time-independent quadratic Hamiltonian and translated finite-support linear jumps. Pairing may occur in the Hamiltonian and the jumps. Only the actual jump radius $`R_J`$ is charged, and the budget $`\Gamma`$ bounds the total squared Fourier jump amplitudes per momentum pair. The coherent range and strength may depend on the system size and are unrestricted. The locality convention is fermionic. A spin representation may add Jordan–Wigner strings.

## Why whole-state fidelity matters

The target is the whole Fermi sea at a fixed squared overlap $`f\in(0,1)`$. Every physical input that commutes with total fermion parity must reach that overlap at the same time. This includes non-Gaussian states and projectors onto odd Fock states. A stationary Gaussian state supplies the aggregate approximation constraint, while an initially odd momentum pair supplies the time bound. The argument allows occasional inaccurate modes and makes no Liouvillian gap identification.

The [separate gain/loss result](time_converse.md) uses a per-mode occupation-rate cap and a number-conserving Hamiltonian. It gives an explicit finite-size time certificate and the exact all-input curve. Its hypotheses and constants remain useful in that narrower setting.

## Larger range, precision and implementation

The paired bound scales as $`[\log(N/(R_J+1))]^3`$ for the logarithm of one plus normalized time. At every fixed $`\epsilon\in(0,1)`$, the optimal logarithm has order $`(\log N)^3`$ from a sufficiently large logarithm-squared radius budget up to $`N^{1-\epsilon}`$. Polynomial normalized time requires $`R_J+1\ge N\exp[-O((\log N)^{1/3})]`$. Full-ring support gives a logarithmic-time construction. The exact radius that permits polynomial time remains open between these endpoints.

The coefficients may be arbitrary finite complex numbers. The [explicit compact reservoir](construction.md) has a sufficient finite-precision specification. The bounds charge rate, radius and elapsed Lindblad time. They do not establish a microscopic bath implementation, a calibration lower bound or an end-to-end hardware runtime.

## Coherent controls and other architectures

Extra persistent modes, enlarged unit cells, time-dependent control, measurement, feedback, nonlinear jumps and non-Markovian dynamics fall outside the model. Energy density and selected local observables are different scores. The [related-work comparison](../references/RELATED_WORK.md) distinguishes finite-support, whole-state approximate preparation from exact-target locality theorems and rapid mixing in other models.
