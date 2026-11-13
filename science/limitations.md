# What the preparation-time law covers

The time law identifies an unavoidable cost of keeping a stationary reservoir compact. On the critical hopping ring, the smallest possible jump radius has order $`(\log N)^2`$. Within the separate gain/loss model below, every reservoir in that radius regime needs a worst-input preparation time whose logarithm has order at least $`(\log N)^3`$. An explicit reservoir attains the same order. The slow time is therefore a property of this compact preparation task, rather than an artifact of that particular filter.

## The allowed reservoir

The system has one spinless fermionic mode per lattice site and no additional persistent modes. The generator is time independent and invariant under translation by one site. Its jumps are translated finite-support linear creation operators and translated finite-support linear annihilation operators, with gain and loss kept in separate families. Arbitrarily many such families and size-dependent complex coefficients are allowed. A translation-invariant number-conserving quadratic Hamiltonian may also be present; in this one-mode setting it commutes with every momentum occupation.

Preparation is required from every physical initial density matrix, including non-Gaussian states, at a specified fixed squared overlap with the whole Fermi sea. This already forces the stationary overlap to reach at least that target: the stationary density matrix is itself an allowed initial state. The gain/loss dynamics has positive occupation damping rates whenever such finite-time all-input preparation is possible. The rate scale $`\Gamma`$ bounds the total occupation damping rate at each sampled momentum. Multiplying the complete generator by a common factor changes the time units and does not change the dimensionless quantity $`\Gamma t`$.

The finite-size converse retains its explicit range, mesh and fidelity conditions. The asymptotic compact-range statement takes $`N\to\infty`$ along $`N=4M+2`$, with the fidelity targets and the constant in $`R\le K(\log N)^2`$ held fixed. Constants in an asymptotic lower bound may depend on these fixed choices.

## Why whole-state fidelity matters

The requested accuracy concerns the entire many-body state. For a gain/loss stationary state, the target overlap is a product of correct momentum-occupation probabilities. Since an all-input preparation guarantee also applies to that stationary input, a fixed positive requested overlap permits only a bounded sum of stationary occupation errors as the number of sites grows.

This criterion allows exceptional modes: it does not require every mode to have error of order $`1/N`$. The converse explicitly charges those exceptions. The same result does not follow merely from an energy-density target, accuracy of finitely many local observables, or an approximation on a fixed interval. Those are different preparation tasks.

The time target is also operational. It asks when **every** allowed initial state has reached a specified fixed target overlap. The proof uses occupation dynamics and a physical complementary Fock input. It does not identify the smallest occupation damping rate with the complete Liouvillian spectral gap.

## Coherent controls and other architectures

The existing spatial result for this target also permits general quadratic pairing when coherent range is counted. The temporal converse here uses the separate gain/loss and number-conserving structure. It makes no temporal claim for general pairing Hamiltonians or jumps that combine creation and annihilation in one family.

Additional modes per unit cell, enlarged unit cells, time-dependent control, measurement and feedback, nonlinear jumps, and non-Markovian reservoirs can change the allowed dynamics. They are outside this theorem. The result supplies no lower bound for these architectures and does not establish that the present time scale is unavoidable for arbitrary quantum state-preparation methods.

The locality convention is fermionic. Mapping to spins through a Jordan–Wigner transformation can introduce strings, so a fermion-local jump need not be local in the corresponding spin representation.

## Larger range, precision and implementation

The matching law concerns radius of order $`(\log N)^2`$. The more general resource inequality also shows that polynomial preparation time requires radius at least of order $`(\log N)^3`$. It does not supply a polynomial-time construction at that radius, the optimized preparation time for every larger radius, or a complete time–range frontier. Full-ring momentum-selective jumps provide a different endpoint, so the compact-range qualification is consequential.

The coefficients in the converse may be arbitrary finite complex numbers. The explicit realization can be programmed with finite coefficient precision, but its sufficient precision bound is not a universal lower bound on experimental calibration or coefficient-description cost. Neither theorem supplies a microscopic bath construction or a complete laboratory runtime estimate. Rate strengths, spatial support and the mathematical time required by the stated Lindblad model are the resources addressed here.

## Relation to earlier locality–time results

Earlier exact ground-state preparation results relate the spatial tails of target-annihilating jumps to zeros of their momentum weights and the resulting relaxation times. The present task permits an approximate mixed stationary state and optimizes over all finite-support gain/loss filters in the compact radius regime. The consequential statement is the universal worst-input time lower bound under this fixed global-fidelity criterion.

See the [scientific model](model.md), [converse](time_converse.md), [matching realization](construction.md) and [related-work comparison](../references/RELATED_WORK.md) for the exact statements and attribution. Those pages are the authority if a shortened summary omits a qualifier.
