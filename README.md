# Fermi-Sea Preparation Time

**Preparing a critical Fermi sea in polynomial time requires a jump radius close to the ring-size scale, even with pairing.**

Consider a periodic chain with one fermionic mode per site and no auxiliary modes. The target fills the momenta with positive cosine. The generator is autonomous and invariant under translation by one site. Its linear fermionic jumps have radius $`R_J`$, and the total squared jump amplitude in each momentum pair is bounded by $`\Gamma`$. The quadratic Hamiltonian can include pairing, with arbitrary strength and range.

At every fixed squared whole-state overlap $`f\in(0,1)`$, preparation from **every physical initial state** requires

```math
\log\!\left(1+\Gamma t_{\mathrm{worst}}(f)\right)
\ge c_f\left[\log\!\left(\frac{N}{R_J+1}\right)\right]^3,\qquad N=4M+2,
```

for sufficiently large $`N/(R_J+1)`$. For every fixed $`\epsilon\in(0,1)`$, the logarithm of the optimized time has order $`(\log N)^3`$ from a sufficiently large logarithm-squared radius budget up through $`N^{1-\epsilon}`$. Polynomial time needs $`R_J+1\ge N\exp[-O((\log N)^{1/3})]`$. Full-ring jump support attains $`\Theta_f(\Gamma^{-1}\log N)`$ time. The smallest radius that allows polynomial time remains open between these bounds.

The [stationary companion](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/main/science/jump_radius.md) proves that the minimum **jump** radius for stationary accuracy is $`\Theta_f((\log N)^2)`$, even with an unrestricted translation-invariant quadratic Hamiltonian. It supplies the discrete root-deletion method and the construction that attains the compact-radius time order. This repository proves the [operational time bound](science/paired_reservoirs.md).

## Why compact jumps cost time

Whole-state fidelity limits the total error across momentum pairs. At stationarity that constraint forces the jump coefficients to distinguish filled from empty pairs across many scales near a Fermi point. If preparation were fast, the jump rates would have to stay large enough to change the parity of each initially odd pair. On a shrinking momentum window, a short Taylor polynomial would then preserve the rate ratios. The required step in those ratios needs more polynomial roots than the short Taylor expansion can supply.

## Read the science

Start with the [scientific overview](science/README.md), or follow a specific question.

| Question | Authoritative account |
| --- | --- |
| How does the result handle pairing and unrestricted coherent evolution? | [Paired-reservoir theorem](science/paired_reservoirs.md) |
| What happens with separate gain and loss and a number-conserving Hamiltonian? | [Model and exact dynamics](science/model.md), [weighted root estimate](science/root_budget.md), and [explicit finite-size converse](science/time_converse.md) |
| Which reservoir attains the compact-radius time order? | [Matching construction](science/construction.md) |
| What changes physically, and which assumptions matter? | [Interpretation](science/interpretation.md) and [limitations](science/limitations.md) |
| Which results and techniques are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [LLM reading guide](llms.txt) maps questions to the same sources. The separate gain/loss proof retains explicit finite-size constants. The paired theorem is asymptotic at fixed overlap.

## Learn the result

The educational anchor is **Breuer and Petruccione, *The Theory of Open Quantum Systems* (2002)**. The [source bridge](learning/anchor_bridge.md) connects Markovian generators and relaxation to fermionic covariance, pair parity, and the rate–radius–time proof.

Start with the [worked two-mode example](learning/README.md#worked-example-two-occupations-one-slow-mode), then follow the [30 milestones](learning/milestones.md) through exact gain/loss dynamics, the matching construction, and the generalization to paired reservoirs.

## Reproduce the checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) covers exact small Fock-space calculations with mixed jumps and strong pairing, separate gain/loss examples, and finite root and filter diagnostics. The analytical proofs establish the large-size bounds.

## Scope

The model uses time-independent Markovian dynamics with one physical fermionic mode per cell and strict jump support. The guarantee concerns squared overlap with the entire Fermi sea from every physical initial state, including non-Gaussian inputs. Auxiliary modes, nonlinear jumps, feedback and time-dependent control lie outside the model.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
