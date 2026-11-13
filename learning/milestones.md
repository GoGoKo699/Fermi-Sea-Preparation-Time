# Thirty milestones from a local reservoir to the global time law

This common map has exactly **30 understanding targets**: 14 background/preliminary targets and 16 narrative/innovation targets. The first phase builds from one occupation bit and one open-system map to the complete preparation task and its inherited spatial foothold. The second phase builds the temporal obstruction from individual roots, combines it with the inherited construction, and ends with the optimized resource statement and its boundaries.

The educational anchor is Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems* (2002). The [anchor bridge](anchor_bridge.md) identifies the verified source sections and translates their notation. Fermionic occupation algebra, rational approximation, the weighted root proof and complex-polynomial arguments are supplied in the project pages. Primary research citations there retain their own attribution.

Dependencies below point only backward. Source pointers identify where to develop each target; the map does not claim to cover every technical detail of those sources.

## Background and preliminaries — 14 milestones

### M01 — One mode and its occupation

- **Central question:** What is the quantum object that one gain or loss jump changes?
- **Understanding target:** Explain the empty and occupied states of one fermion mode, the occupation projector and the difference between a state and an occupation probability.
- **Dependencies and story role:** Entry point; gives a concrete local object before introducing a reservoir or a many-body target.
- **Conceptual connection:** A quantum state supplies probabilities for a binary occupation, while the later dynamics acts on the full density operator.
- **Source pointers:** Anchor §2.1.3 (pure states and statistical mixtures), as mapped in the [bridge](anchor_bridge.md); [model: register and target](../science/model.md#register-target-and-physical-inputs).

### M02 — A Fermi sea on a ring

- **Central question:** Which occupations define the state we want to prepare?
- **Understanding target:** Relate site modes to Fourier modes, identify the filled and empty sides of the Fermi points, and explain why the size convention avoids a sampled crossing.
- **Dependencies and story role:** M01; assembles the local modes into a definite many-body target.
- **Conceptual connection:** Spatially local couplings become momentum-dependent amplitudes, and a sharp occupation change is the feature those amplitudes must reproduce.
- **Source pointers:** [Model: register and target](../science/model.md#register-target-and-physical-inputs).

### M03 — Accuracy of the entire register

- **Central question:** What does fixed overlap with a many-body pure target demand?
- **Understanding target:** Interpret squared target overlap and distinguish whole-state preparation from low energy density or accurate local observables.
- **Dependencies and story role:** M01–M02; fixes the requested output before discussing a preparation method.
- **Conceptual connection:** Many small occupation errors can destroy a global overlap even when local measurements look accurate.
- **Source pointers:** Anchor §§2.1.4 and 2.4.2 for probability and effects; [complete-register score](../science/model.md#complete-register-score); [whole-state fidelity](../science/limitations.md#why-whole-state-fidelity-matters). The project defines the target-overlap criterion.

### M04 — From a channel to continuous Markovian evolution

- **Central question:** How is an autonomous open quantum evolution described?
- **Understanding target:** Explain complete positivity, trace preservation, the semigroup property and the role of a time-independent generator.
- **Dependencies and story role:** M01 and M03; introduces the dynamical framework in which preparation time is measured.
- **Conceptual connection:** The same physical device acts for different elapsed times, rather than receiving a new externally chosen control at each step.
- **Source pointers:** Anchor §§2.4.2–2.4.3, 3.1.3 and 3.2.1–3.2.2; [model: allowed generators](../science/model.md#allowed-autonomous-generators); [bridge](anchor_bridge.md).

### M05 — Gain, loss and one relaxation rate

- **Central question:** How do two quantum jumps set one mode's stationary population and speed?
- **Understanding target:** Explain the equations with gain rate, loss rate and their sum; distinguish the stationary ratio from the damping sum.
- **Dependencies and story role:** M01 and M04; supplies the local mechanism that later supports both the construction and the converse.
- **Conceptual connection:** A favorable stationary occupation can coexist with extremely slow approach to it.
- **Source pointers:** Anchor §1.4.4 for jump-process master equations and §3.2.2 for the quantum generator; [rates and occupation dynamics](../science/model.md#allowed-autonomous-generators); [physical competition](../science/interpretation.md#the-physical-competition).

### M06 — Fermionic algebra and physical inputs

- **Central question:** Which many-body inputs must the preparation guarantee cover?
- **Understanding target:** Explain the canonical anticommutation relations, parity-compatible density matrices and why an odd-particle Fock projector remains a physical state.
- **Dependencies and story role:** M01–M02 and M04; makes the input quantifier precise before choosing a worst input.
- **Conceptual connection:** Fermionic signs matter in operators, but they need not survive in occupation transition probabilities.
- **Source pointers:** Anchor §2.2.1 supplies general composition foundations; the fermionic specialization is in [physical inputs](../science/model.md#register-target-and-physical-inputs) and [the occupation-algebra derivation](../science/model.md#complete-register-score).

### M07 — Finite spatial support becomes a polynomial

- **Central question:** How does a jump radius constrain its momentum dependence?
- **Understanding target:** Trace a finite-support translated jump into a Laurent-polynomial amplitude and a nonnegative trigonometric gain or loss rate.
- **Dependencies and story role:** M02 and M05–M06; connects the spatial resource to a mathematical restriction.
- **Conceptual connection:** Radius constrains polynomial degree even when the coefficients are complex and many jump families are permitted.
- **Source pointers:** [Allowed generators](../science/model.md#allowed-autonomous-generators); [rate polynomials](../science/time_converse.md#rate-polynomials-and-their-finite-ring-norm).

### M08 — Fixing the physical time scale

- **Central question:** What prevents a reservoir from removing slowness by multiplying all rates?
- **Understanding target:** Interpret the sampled total-rate budget, the dimensionless time and the distinction between finite-grid normalization and a continuous-momentum norm.
- **Dependencies and story role:** M05 and M07; completes the rate resource accounting needed for a meaningful time bound.
- **Conceptual connection:** A filter's occupation ratio is invariant under rescaling, while its preparation time is not.
- **Source pointers:** [Model: rate budget](../science/model.md#allowed-autonomous-generators); [finite-ring norm](../science/time_converse.md#rate-polynomials-and-their-finite-ring-norm).

### M09 — What the Hamiltonian can change

- **Central question:** Can the allowed coherent dynamics move population away from a slow momentum mode?
- **Understanding target:** Explain why a translation-invariant number-conserving quadratic Hamiltonian commutes with momentum occupations, and locate the excluded pairing and control architectures.
- **Dependencies and story role:** M02, M04 and M06–M08; completes the allowed-device model.
- **Conceptual connection:** A restriction on coherent dynamics is part of the theorem's mechanism, rather than a detail that can be dropped after the calculation.
- **Source pointers:** [Allowed generators](../science/model.md#allowed-autonomous-generators); [architectural boundaries](../science/limitations.md#coherent-controls-and-other-architectures).

### M10 — A closed occupation algebra

- **Central question:** Why can an all-input quantum statement use classical occupation transitions?
- **Understanding target:** Use the adjoint gain/loss identities to explain cancellation of fermionic signs and closure of functions of the commuting occupations.
- **Dependencies and story role:** M04–M09; turns local mode dynamics into an exact register-level tool.
- **Conceptual connection:** Restricting an evolved observable to a closed algebra does not require the initial quantum state to be Gaussian or diagonal.
- **Source pointers:** Anchor §§3.1.2 and 3.2.3; [project CAR and Heisenberg derivation](../science/model.md#complete-register-score); [bridge](anchor_bridge.md).

### M11 — The worst input is a physical state

- **Central question:** Which initial state makes the whole-register target population smallest?
- **Understanding target:** Reconstruct the one-mode correct-bit transitions, the product minimum at the complementary Fock state and the exact all-input fidelity curve.
- **Dependencies and story role:** M03, M06 and M10; makes the time target operational instead of relying on a spectral-gap label.
- **Conceptual connection:** Every mode starts wrong in one legitimate physical input, so a single slow occupation can obstruct every fixed positive all-input overlap.
- **Source pointers:** Anchor §§1.4.4 and 2.1.4 for transitions and joint probabilities; [exact all-input curve](../science/model.md#complete-register-score); [why one slow mode matters](../science/interpretation.md#why-one-slow-mode-matters).

### M12 — A bounded sum of stationary errors

- **Central question:** What does a finite-time global guarantee imply about stationary occupations?
- **Understanding target:** Explain why successful all-input preparation forces adequate stationary overlap, and how a product overlap bounds the sum of occupation errors while allowing exceptional modes.
- **Dependencies and story role:** M03, M05 and M11; extracts the accuracy premise used by the universal converse.
- **Conceptual connection:** The converse must control aggregate errors; a uniform inverse-size error premise would describe a narrower task.
- **Source pointers:** [Complete-register score](../science/model.md#complete-register-score); [aggregate-error root lemma](../science/root_budget.md#lemma-2-aggregate-error-forces-cubic-root-cost).

### M13 — Odds, roots and classical approximation

- **Central question:** How can an occupation step constrain the roots of finite-degree polynomials?
- **Understanding target:** Relate stationary odds to a rational function on the tangent grid, explain opposite-argument log ratios and identify the inherited continuous root kernel and discrete root-deletion method.
- **Dependencies and story role:** M07 and M12; introduces the approximation language needed to understand the new time argument.
- **Conceptual connection:** Root counts describe spatial feasibility; the location of those roots will carry additional dynamical information.
- **Source pointers:** [Rate-polynomial representation](../science/time_converse.md#rate-polynomials-and-their-finite-ring-norm); [root-budget definitions](../science/root_budget.md#finite-grid-quantities); [inherited ingredients](../science/root_budget.md#scaling-and-inherited-ingredients).

### M14 — The preparation question left open by spatial feasibility

- **Central question:** What was already established, and which possibility must the new theorem eliminate?
- **Understanding target:** Assemble the target, generator restrictions, rate budget and all-input accuracy; explain the inherited logarithm-squared spatial order and the slow explicit filter without treating its time as an optimized lower bound.
- **Dependencies and story role:** M01–M13; closes the background phase with the complete scientific question.
- **Conceptual connection:** The open issue is whether a different admissible filter can stabilize the same state at the same spatial order and approach it much faster.
- **Source pointers:** [Model: main result and attribution](../science/model.md#main-result); [matching construction](../science/construction.md); [physical interpretation](../science/interpretation.md).

## Narrative and innovation — 16 milestones

### M15 — Resolving the crossing on many scales

- **Central question:** Why does one Fermi-point neighborhood supply more than a single boundary comparison?
- **Understanding target:** Explain the paired sampled modes, logarithmic mesh weights and a window that approaches the crossing as the register grows.
- **Dependencies and story role:** M02, M12–M14; starts the new argument with the local geometry of the occupation discontinuity.
- **Conceptual connection:** Whole-state accuracy constrains the filter across an entire hierarchy of momentum scales.
- **Source pointers:** [Finite-grid quantities](../science/root_budget.md#finite-grid-quantities); [aggregate-error root lemma](../science/root_budget.md#lemma-2-aggregate-error-forces-cubic-root-cost).

### M16 — Paying for exceptions and near-sample roots

- **Central question:** How can the proof remain uniform when some modes are inaccurate or roots nearly hit the grid?
- **Understanding target:** Distinguish occupation-bad deletions from root-peak deletions, and explain why their lost weighted mass is explicitly bounded.
- **Dependencies and story role:** M12–M13 and M15; removes the failure modes that a uniform-error or continuous-only argument would overlook.
- **Conceptual connection:** Exceptional modes are permitted by the physical score, while singular sampled root terms are handled by the inherited two-index prescription.
- **Source pointers:** [One weighted root](../science/root_budget.md#lemma-1-one-weighted-root); [aggregate-error lemma](../science/root_budget.md#lemma-2-aggregate-error-forces-cubic-root-cost).

### M17 — The extra weight measures root depth

- **Central question:** What changes when each scale is weighted by its distance from the crossing on a logarithmic axis?
- **Understanding target:** Explain the new logarithmic weight, the kernel's finite first moment and the difference between counting useful roots and charging their depth.
- **Dependencies and story role:** M13 and M15–M16; identifies the new analytical mechanism.
- **Conceptual connection:** The inherited unweighted kernel controls spatial degree; its weighted moment controls amplitude attenuation relevant to time.
- **Source pointers:** [Weighted root lemma and kernel moments](../science/root_budget.md#lemma-1-one-weighted-root); [attribution](../science/root_budget.md#scaling-and-inherited-ingredients).

### M18 — Clipping the root charge at the finite mesh

- **Central question:** Why does the converse not need an unbounded charge for a root arbitrarily close to zero?
- **Understanding target:** Interpret the clipped root cost, its cutoff at the left integration endpoint and the cases of complex, zero and very small roots.
- **Dependencies and story role:** M15–M17; makes the weighted estimate uniform before it is applied to arbitrary reservoir coefficients.
- **Conceptual connection:** The selected finite grid window fixes the root depth needed by this estimate; clipping does not assert that deeper roots have no physical effect.
- **Source pointers:** [Root-cost definition and one-root bound](../science/root_budget.md#finite-grid-quantities); [proof of Lemma 1](../science/root_budget.md#lemma-1-one-weighted-root).

### M19 — From global accuracy to a cubic root budget

- **Central question:** Where does the third logarithm enter the universal converse?
- **Understanding target:** Connect the good-node log-odds contrast, the weighted scale mass and the controlled deletions to a cubic-logarithmic total root cost.
- **Dependencies and story role:** M12 and M15–M18; combines the local root estimates into the first global result of the new proof.
- **Conceptual connection:** One logarithm comes from accuracy, while the weighted hierarchy of scales contributes two more.
- **Source pointers:** [Aggregate-error root lemma](../science/root_budget.md#lemma-2-aggregate-error-forces-cubic-root-cost); [asymptotic scaling](../science/root_budget.md#scaling-and-inherited-ingredients).

### M20 — A sampled rate budget controls a complex polynomial

- **Central question:** How can a bound on physical rates constrain the complex values used by Jensen's formula?
- **Understanding target:** Explain the finite-grid-to-continuous Bernstein step, the tangent numerator degree and the elementary Chebyshev bound on a fixed complex disk.
- **Dependencies and story role:** M07–M08 and M13; supplies the normalization bridge needed to turn root location into an absolute rate bound.
- **Conceptual connection:** Polynomial cancellations and arbitrarily many jump families do not remove the link between physical rate normalization and complex growth.
- **Source pointers:** [Rate polynomials and finite-ring norm](../science/time_converse.md#rate-polynomials-and-their-finite-ring-norm).

### M21 — Jensen turns root depth into attenuation

- **Central question:** Why must a polynomial with a large clipped root cost be small near the Fermi point?
- **Understanding target:** Interpret the fixed-disk Jensen penalty and explain how the degree correction, small roots and common factors are controlled.
- **Dependencies and story role:** M18–M20; converts the approximation budget into a physical amplitude restriction.
- **Conceptual connection:** Fixing the largest physical rate prevents a reservoir from compensating deep root attenuation by unrestricted rescaling.
- **Source pointers:** [Root cost and a small desired rate](../science/time_converse.md#root-cost-forces-a-small-desired-rate).

### M22 — Selecting the desired side of the crossing

- **Central question:** When does a small numerator imply a small total damping rate?
- **Understanding target:** Explain why a nearby good occupied mode is chosen for an attenuated gain polynomial, and a good empty mode for an attenuated loss polynomial.
- **Dependencies and story role:** M05, M12 and M21; resolves the decisive inference between polynomial attenuation and slow physical relaxation.
- **Conceptual connection:** Small unwanted rates improve purity without implying slowness; a small desired rate at a correctly biased mode forces the entire damping sum to be small.
- **Source pointers:** [Good-mode selection](../science/time_converse.md#root-cost-forces-a-small-desired-rate); [finite-size theorem](../science/time_converse.md#finite-size-theorem).

### M23 — One slow occupation forces elapsed time

- **Central question:** Why does the selected slow rate obstruct the stated preparation task?
- **Understanding target:** Combine the exact all-input product with the selected mode's factor to obtain a lower bound on actual elapsed time at fixed overlap.
- **Dependencies and story role:** M11 and M22; completes the operational part of the temporal converse.
- **Conceptual connection:** The proof needs neither a Gaussian input promise nor an identification of this occupation rate with the full Liouvillian gap.
- **Source pointers:** [All-input curve](../science/model.md#complete-register-score); [finite-size theorem proof](../science/time_converse.md#finite-size-theorem).

### M24 — Reading the finite-size certificate

- **Central question:** Which hypotheses and finite quantities make the bound usable for a particular register?
- **Understanding target:** Interpret the mesh, good-mode count, sampled-rate condition and positive-part root bound; distinguish a necessary condition from a feasible design or a numerically strong estimate.
- **Dependencies and story role:** M15–M23; integrates the complete converse before taking an asymptotic limit.
- **Conceptual connection:** Explicit finite conditions keep a large-size law tied to its actual fidelity and normalization conventions.
- **Source pointers:** [Finite-size theorem](../science/time_converse.md#finite-size-theorem); [verification scope](../verification/README.md).

### M25 — An inherited filter is an actual reservoir

- **Central question:** How do geometrically spaced roots become local Lindblad jumps rather than a formal occupation curve?
- **Understanding target:** Explain the normalized gain/loss polynomials, their finite Laurent support, positive rates and two translated physical jump families.
- **Dependencies and story role:** M05, M07–M08 and M14; begins the attainment side of the story after the universal obstruction.
- **Conceptual connection:** The construction is inherited; its role here is to demonstrate that the lower time order can be attained in the same resource model.
- **Source pointers:** Anchor §3.2.2 for the generator framework; [positive momentum filters](../science/construction.md#positive-momentum-filters); [construction attribution](../science/construction.md).

### M26 — Accurate stationary ratios and slow dynamics

- **Central question:** How does the same filter achieve small errors while remaining very slow?
- **Understanding target:** Connect the root-ratio suppression to whole-state stationary fidelity, then relate the minimum absolute amplitude to the all-input time bound.
- **Dependencies and story role:** M03, M05, M11 and M25; connects the construction's static and dynamical properties.
- **Conceptual connection:** A uniform per-mode error bound is a sufficient design feature of the upper construction; the converse was proved under only an aggregate error constraint.
- **Source pointers:** [Stationary fidelity](../science/construction.md#whole-state-stationary-fidelity); [finite-time preparation](../science/construction.md#finite-time-from-arbitrary-physical-inputs).

### M27 — Finite coefficients without free preparation time

- **Central question:** Does the attaining construction require exact real-number coefficients?
- **Understanding target:** Explain the inherited relative-amplitude rounding control, its sufficient precision budget and why preserving positive damping preserves the time order without making it fast.
- **Dependencies and story role:** M08 and M25–M26; completes the upper construction's relevant resource accounting.
- **Conceptual connection:** A finite specification theorem is distinct from a universal precision lower bound or a microscopic bath implementation.
- **Source pointers:** [Finite coefficients and charged resources](../science/construction.md#finite-coefficients-and-charged-resources); [implementation limits](../science/limitations.md#larger-range-precision-and-implementation).

### M28 — The optimized compact-radius law

- **Central question:** What is optimal after both the converse and the construction are credited?
- **Understanding target:** Define the fixed-rate optimized preparation time and explain the matching cubic-logarithmic logarithm of time for sufficiently large logarithm-squared radius budgets, including the subcubic-logarithmic budget window.
- **Dependencies and story role:** M19–M27; combines necessity and attainment into the project's central optimized statement.
- **Conceptual connection:** The enormous time is intrinsic to all admissible compact reservoirs, rather than an avoidable defect of one inherited filter.
- **Source pointers:** [Optimized-time definition](../science/model.md#complete-register-score); [main result](../science/model.md#main-result); [radius-budget optimization](../science/time_converse.md#optimizing-under-a-radius-budget).

### M29 — What a larger radius could change

- **Central question:** Which conclusion follows about polynomial preparation time, and which frontier remains open?
- **Understanding target:** Derive the necessary cubic-logarithmic radius from the general resource inequality, distinguish necessity from attainment, and place full-ring momentum-selective preparation at the separate large-range endpoint.
- **Dependencies and story role:** M08, M24 and M28; connects the compact optimum to the wider design question without extending the theorem beyond its proof.
- **Conceptual connection:** Increasing the spatial budget may remove this obstruction, but the present theorem supplies no matching polynomial-time design at the necessary radius.
- **Source pointers:** [General radius-time consequence](../science/time_converse.md#cubic-logarithm-and-the-radius-time-consequence); [reservoir-design implications](../science/interpretation.md#what-this-changes-for-reservoir-design); [larger-range limits](../science/limitations.md#larger-range-precision-and-implementation).

### M30 — The full scientific account and its boundary

- **Central question:** What can now be concluded about preparing a critical Fermi sea with a compact autonomous reservoir?
- **Understanding target:** Present one connected account of the task, allowed dynamics, global score, new weighted-root/attenuation converse, inherited matching construction and optimized time law; state the unresolved leading constant, larger-range frontier and excluded architectures.
- **Dependencies and story role:** M01–M29; closes the narrative phase by integrating the physical meaning, attribution and scope of the result.
- **Conceptual connection:** Stationary spatial feasibility and operational preparation time are distinct resources, and the theorem settles their compact-radius relation within a precisely stated gain/loss model.
- **Source pointers:** [Scientific overview](../science/README.md); [interpretation](../science/interpretation.md); [limitations](../science/limitations.md); [related work](../references/RELATED_WORK.md); [anchor bridge](anchor_bridge.md).
