# Scientific account

The task is to prepare an entire critical Fermi sea from an arbitrary physical input using a stationary finite-range gain/loss reservoir. Spatial feasibility and elapsed preparation time have different optimal scalings.

1. [Model and exact occupation dynamics](model.md) define the finite ring, rate normalization, fidelity and worst-input time.
2. [Weighted root budget](root_budget.md) turns the whole-state fidelity constraint into a logarithmic moment of polynomial roots. The ordinary root potential and discrete pole deletions are inherited; the weighted moment is the temporal ingredient.
3. [Finite-size time converse](time_converse.md) uses bounded polynomial growth and Jensen attenuation to identify a slow physical mode and derives the general space–time obstruction.
4. [Matching construction](construction.md) reproduces the inherited positive geometric-root filters, their accuracy, finite-time bound and finite coefficient specification.
5. [Interpretation](interpretation.md) connects the result to autonomous cooling; [limitations](limitations.md) state the physical and mathematical boundaries.

The [related-work comparison](../references/RELATED_WORK.md) identifies exact model/theorem differences and assigns shared results to their sources. The [verification guide](../verification/README.md) provides executable diagnostics and their limits.
