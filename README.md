# Fermi-Sea Preparation Time

**A compact reservoir can reach a critical Fermi sea, yet take longer than every polynomial time to prepare it.**

Consider a periodic chain with one fermionic mode per site. The target fills the momenta with positive cosine. A stationary reservoir uses translated finite-range linear gain and loss jumps, a number-conserving quadratic Hamiltonian and no auxiliary modes. Its coefficients and number of jump families may depend on system size. The total occupation relaxation rate at each momentum is bounded by $`\Gamma`$.

At every fixed squared whole-state overlap $`f\in(0,1)`$, preparation from **every physical initial state** obeys

```math
R+\log\!\left(1+\Gamma t_{\mathrm{worst}}(f)\right)
=\Omega_f((\log N)^3),\qquad N=4M+2.
```

Here $`R`$ is the jump radius. Let $`T_{\mathrm{opt}}(N,R_{\max},f)`$ minimize the worst-input time over devices with radius at most $`R_{\max}`$. At a sufficiently large fixed logarithm-squared radius budget, it has the matching order

```math
\log\!\left(1+\Gamma T_{\mathrm{opt}}(N,R_{\max},f)\right)
=\Theta_f((\log N)^3).
```

Thus the minimum spatial order $`\Theta((\log N)^2)`$ is compatible with preparation, but entails a superpolynomial waiting time. Polynomial preparation time requires $`R=\Omega_f((\log N)^3)`$; an attaining construction at that larger radius is not established.

The [spatial companion](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/tree/293b8e6914d8ff85ed3605d6c85dc95abfef4b61) supplies the minimum-radius result, discrete root-deletion foundation and matching slow construction. **The contribution here is the temporal converse optimized over all bounded-rate reservoirs in the stated gain/loss class.** It shows that the construction's extreme slowdown is unavoidable, rather than a poor choice of coefficients. The companion's broader spatial theorem permits pairing; this temporal theorem does not.

## Why compactness costs time

Whole-state fidelity limits the total occupation error. Across many distances from a Fermi point, the gain-to-loss odds must therefore change strongly between occupied and empty modes. Factoring their finite-degree polynomials converts these changes into a root budget. Weighting that budget by logarithmic distance forces many roots deep near the crossing.

A bounded polynomial cannot hide the resulting attenuation: a fixed-disk growth bound and Jensen's formula force a very small gain or loss rate near the Fermi point. A correctly occupied nearby mode then has a very small total relaxation rate. Starting that mode in the wrong occupation makes the all-input preparation task slow.

## Read the science

Start with the [scientific overview](science/README.md), or follow a specific question.

| Question | Authoritative account |
| --- | --- |
| What is supplied, allowed and charged? | [Model and exact dynamics](science/model.md) |
| How does global fidelity force a weighted polynomial-root budget? | [Weighted root estimate](science/root_budget.md) |
| Why must some physical occupation mode relax extremely slowly? | [Finite-size time converse](science/time_converse.md) |
| Can the cubic-logarithmic time order be attained? | [Matching construction](science/construction.md) |
| What changes physically, and which assumptions matter? | [Interpretation](science/interpretation.md) and [limitations](science/limitations.md) |
| Which results and techniques are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [LLM reading guide](llms.txt) maps questions to these same sources. Exact finite-size constants and conditions appear in the proof pages; the asymptotic order does not promise a useful numerical lower bound at small sizes.

## Learn the result

The single educational anchor is **Breuer and Petruccione, *The Theory of Open Quantum Systems* (2002)**. The [source bridge](learning/anchor_bridge.md) selects the relevant sections, translates rate and fidelity conventions, and supplies the project-specific fermionic, approximation and Jensen steps.

Start with the [complete two-mode example](learning/README.md#worked-example-two-occupations-one-slow-mode), then use the [30-milestone map](learning/milestones.md): 14 background targets and 16 targets assembling the temporal argument, matching construction and scope. The [learning overview](learning/README.md) connects these routes; specialist readers can continue directly to the science pages above.

## Reproduce the checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) separates small Fock-space dynamics, reference/non-Gaussian input checks, logarithmic evaluation of the slow construction and adversarial root diagnostics. Finite calculations support conventions and examples; the arbitrary-size theorem follows from the analytical proof.

## Scope

This is a time-independent, one-site-translation-invariant, one-mode-per-cell gain/loss theorem with ideal Markovian dynamics and number-conserving coherent evolution. It controls whole-state overlap from all physical initial states, rather than energy density or selected local observables. Pairing, nonlinear jumps, auxiliary modes, feedback and time-dependent control can change the model. No quantum computational advantage, optimal faster-radius construction or microscopic bath implementation follows.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
