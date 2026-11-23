# What makes a compact reservoir slow?

An accurate stationary state and a useful preparation procedure impose different demands. A reservoir can have a stationary state with substantial overlap with the critical Fermi sea while approaching it extremely slowly. The present result determines whether better filter coefficients can remove that slow preparation without increasing the spatial order.

The [paired theorem](paired_reservoirs.md) makes this comparison even with an arbitrary translation-invariant quadratic Hamiltonian. At fixed whole-state overlap, the logarithm of the optimized time has order $`(\log N)^3`$ from a sufficiently large logarithm-squared radius budget up to any fixed sublinear power of $`N`$. The known geometric-root reservoir attains this order wherever its radius fits.

## The physical competition

The target occupation jumps from filled to empty across each Fermi point. A finite-support translated jump has a polynomial momentum amplitude. Separate gain and loss therefore produce nonnegative trigonometric rate polynomials $`a(k)`$ and $`b(k)`$, with

```math
n(k)=\frac{a(k)}{a(k)+b(k)},
\qquad
g(k)=a(k)+b(k).
```

The ratio determines the stationary occupation. The sum determines how quickly that mode forgets its initial occupation. Whole-state fidelity forces the ratio to distinguish the two sides of the Fermi point over many scales; the logarithm-squared range is enough to make that discrimination possible.

The [separate gain/loss converse](time_converse.md) charges the accompanying amplitude. Its weighted root estimate shows that an accurate compact filter must accumulate enough root depth near a Fermi point to suppress at least one physical rate there. Bounded overall rates prevent compensating this suppression by unlimited gain. The bounded aggregate occupation error guarantees a nearby correctly biased mode, so the small numerator also gives a small total damping rate at an actual sampled momentum.

This is a constraint on all admissible filters, including size-dependent complex coefficients, many translated jump families, and common polynomial factors. It is not inferred from the behavior of one chosen construction.

## Pairing and the rate bound

For general linear jumps, a stationary block's covariance bounds its total wrong-direction dissipative rate. The resulting ratio of positive rate polynomials distinguishes the two sides of the Fermi point even when the Hamiltonian mixes particle and hole amplitudes. The same Hamiltonian preserves each momentum pair's physical parity. Starting a pair in an odd Fock state therefore gives a preparation-time bound in terms of its total jump rate.

If the time were short, all pair rates would have to be large enough for their ratios to survive a low-order Taylor approximation on a short momentum window. The required step across the Fermi point exceeds the available polynomial degree. The [paired proof](paired_reservoirs.md) makes this contradiction quantitative.

## Why one slow mode matters

In the separate gain/loss class, the requested output is the entire Fermi sea, prepared from every physical initial state. The complementary Fock state starts every target occupation incorrectly. For separate gain/loss dynamics its target population is

```math
\inf_{\rho_0}F_{\rho_0}(t)
=F_\infty\prod_k\bigl(1-e^{-g(k)t}\bigr).
```

Off-diagonal initial matrix elements do not lower this minimum. The product is bounded above by the factor of any one momentum, so a single sufficiently slow occupation blocks every fixed positive all-input overlap target until a time proportional to its inverse damping rate.

This operational argument avoids identifying an occupation damping rate with the full fermionic Liouvillian spectral gap. It also explains why an energy-density target or a small set of local observables would be a different task: they need not resolve every occupation well enough for a fixed whole-state overlap.

## What this changes for reservoir design

The [stationary companion](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/main/science/jump_radius.md) proves the minimum jump radius of order $`(\log N)^2`$ and supplies a reservoir attaining that order. Polynomial worst-input preparation time requires $`R_J+1\ge N\exp[-O((\log N)^{1/3})]`$. Full-ring momentum-selective jumps attain logarithmic time. The smallest radius allowing polynomial time lies between those two bounds.

Efficient digital construction or simulation of a spectrally filtered jump is also a different resource statement. A spectral projector with favorable abstract mixing may have long spatial tails. The [related-work account](../references/RELATED_WORK.md) separates exact-target tail bounds, rapid-mixing results, the inherited rational filters, and the finite-support time optimum proved here.

## Scope of the conclusion

The main result allows arbitrary pairing and strength in a one-site-translation-invariant quadratic Hamiltonian. Its budget $`\Gamma`$ bounds the total jump amplitude squared per momentum pair. The narrower result uses number-conserving coherent dynamics, separate gain and loss and a per-momentum occupation-rate cap. Additional persistent modes, enlarged cells, time-dependent controls, measurements and feedback lie outside these models. The [limitations](limitations.md) give the complete scope.
