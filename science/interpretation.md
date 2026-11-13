# What makes a compact reservoir slow?

An accurate stationary state and a useful preparation procedure impose different demands. A reservoir can have a stationary state with substantial overlap with the critical Fermi sea while approaching it extremely slowly. The present result determines whether better filter coefficients can remove that slow preparation without increasing the spatial order.

They cannot within the stated autonomous gain/loss class. At fixed whole-state overlap, every successful device satisfies the radius-time inequality

```math
\log(1+\Gamma t)+C R\ge c(\log N)^3
```

for positive constants at sufficiently large sizes. In particular, every bounded-rate family with jump radius $`R\le K(\log N)^2`$, for a size-independent $`K`$, has

```math
\log\!\bigl(\Gamma t_{\mathrm{worst}}\bigr)
=\Omega((\log N)^3).
```

The known geometric-root reservoir attains an upper bound of the same order for a sufficiently large fixed range constant. Thus the spatially optimal range order has an unavoidable preparation time $`\Gamma^{-1}\exp[\Theta((\log N)^3)]`$ in this model. Feasibility at every smaller constant $`K`$ is not asserted. The matching time order persists when the allowed radius is increased to any $`o((\log N)^3)`$ budget that already permits the construction.

## The physical competition

The target occupation jumps from filled to empty across each Fermi point. A finite-support translated jump has a polynomial momentum amplitude. Separate gain and loss therefore produce nonnegative trigonometric rate polynomials $`a(k)`$ and $`b(k)`$, with

```math
n(k)=\frac{a(k)}{a(k)+b(k)},
\qquad
g(k)=a(k)+b(k).
```

The ratio determines the stationary occupation. The sum determines how quickly that mode forgets its initial occupation. Whole-state fidelity forces the ratio to distinguish the two sides of the Fermi point over many scales; the logarithm-squared range is enough to make that discrimination possible.

The temporal converse charges the accompanying amplitude. Its weighted root estimate shows that an accurate compact filter must accumulate enough root depth near a Fermi point to suppress at least one physical rate there. Bounded overall rates prevent compensating this suppression by unlimited gain. The bounded aggregate occupation error guarantees a nearby correctly biased mode, so the small numerator also gives a small total damping rate at an actual sampled momentum.

This is a constraint on all admissible filters, including size-dependent complex coefficients, many translated jump families, and common polynomial factors. It is not inferred from the behavior of one chosen construction.

## Why one slow mode matters

The requested output is the entire Fermi sea, prepared from every physical initial state. The complementary Fock state starts every target occupation incorrectly. For separate gain/loss dynamics its target population is

```math
\inf_{\rho_0}F_{\rho_0}(t)
=F_\infty\prod_k\bigl(1-e^{-g(k)t}\bigr).
```

Off-diagonal initial matrix elements do not lower this minimum. The product is bounded above by the factor of any one momentum, so a single sufficiently slow occupation blocks every fixed positive all-input overlap target until a time proportional to its inverse damping rate.

This operational argument avoids identifying an occupation damping rate with the full fermionic Liouvillian spectral gap. It also explains why an energy-density target or a small set of local observables would be a different task: they need not resolve every occupation well enough for a fixed whole-state overlap.

## What this changes for reservoir design

The [spatial companion](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/tree/293b8e6914d8ff85ed3605d6c85dc95abfef4b61) already proves the optimal spatial order and supplies a reservoir with the stated time. The new obstruction closes the possibility that this large time is merely a poor coefficient choice. Polynomial worst-input preparation time requires at least $`\Omega((\log N)^3)`$ radius, exceeding the stationary-feasibility scale. This is a necessary condition; no polynomial-time construction at that radius is established.

Increasing the range may change the answer. With full-ring support, momentum-selective gain/loss jumps can give constant damping to every mode and logarithmic all-input preparation time at fixed error. The theorem does not determine the optimal interpolation between these endpoints.

Efficient digital construction or simulation of a spectrally filtered jump is also a different resource statement. A spectral projector with favorable abstract mixing may have long spatial tails. The [related-work account](../references/RELATED_WORK.md) separates exact-target tail bounds, rapid-mixing results, the inherited rational filters, and the finite-support time optimum proved here.

## Scope of the conclusion

The Hamiltonian is quadratic, translation invariant and number conserving. With one mode per cell it commutes with every momentum occupation and cannot transfer population around the slow mode. Pairing Hamiltonians, jumps mixing creation and annihilation, additional persistent modes, enlarged cells, time-dependent controls, measurements and feedback are outside the temporal theorem.

The budget $`\Gamma`$ bounds each sampled total occupation damping rate. It is not a microscopic bath bandwidth, a complete gate cost, or a laboratory resource estimate. The result supplies a mathematical preparation-time obstruction under that budget. See the [model](model.md), [converse](time_converse.md), [matching construction](construction.md), and [limitations](limitations.md) for the complete statement.
