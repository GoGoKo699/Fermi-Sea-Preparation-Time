# Scientific account

The task is to prepare a critical Fermi sea from every physical initial state, with an autonomous translation-invariant fermionic reservoir. Stationary feasibility and elapsed time have different optimal scalings.

1. [Preparation time with pairing](paired_reservoirs.md) proves the rate–radius–time law for arbitrary linear jumps and arbitrary translation-invariant quadratic Hamiltonians. It reduces stationary block covariances to scalar dissipative selectivity, uses parity to witness time, and applies discrete root deletion to a local Taylor approximation.
2. [Separate gain/loss model and exact occupation dynamics](model.md) give the exact worst-input curve for the narrower number-conserving model with a per-momentum rate cap.
3. [Weighted root budget](root_budget.md) and [finite-size time converse](time_converse.md) retain explicit finite-size estimates for that gain/loss model, using Jensen attenuation of actual rate polynomials.
4. [Matching construction](construction.md) uses the inherited positive geometric-root filters. It gives stationary accuracy, a finite-time bound and finite coefficient precision.
5. [Interpretation](interpretation.md) and [limitations](limitations.md) place the results in context and specify their physical scope.

The [stationary companion](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/main/science/jump_radius.md) establishes the jump-only radius threshold. See the [related-work comparison](../references/RELATED_WORK.md) for attribution and the [verification guide](../verification/README.md) for the numerical diagnostics.
