# Related work and attribution

The question here is the **time required by a spatially economical reservoir**, rather than the existence of a stationary approximation. The target is the half-filled critical hopping-chain Fermi sea. The temporal theorem concerns one-site-translation-invariant, time-independent separate linear gain/loss reservoirs, one physical mode per cell, a number-conserving quadratic Hamiltonian, bounded momentum occupation rates, and fixed nonzero squared global overlap. Its precise quantifiers are in the [model](../science/model.md) and [converse](../science/time_converse.md).

## The spatial companion

[Fermi Sea Reservoir Locality][1] establishes the minimum spatial order $`R_{\min}=\Theta((\log N)^2)`$ at fixed whole-state overlap. Its spatial converse also covers pairing Hamiltonians and general linear Gaussian jumps when coherent range is counted. Its separate gain/loss construction already has

```math
\log(\Gamma t_{\mathrm{worst}})=\Theta((\log N)^3).
```

That time statement characterizes the construction; its preparation-cost account explicitly leaves optimization over other reservoirs open.

The present work inherits the spatial scale, aggregate occupation-error consequence of global fidelity, discrete root-deletion estimate, geometric-root construction, and its time accounting. The added conclusion is a universal necessary resource inequality

```math
\log(1+\Gamma t)+C R\ge c(\log N)^3
```

for every successful device in the stated gain/loss class. It gives a matching time order at logarithm-squared range and throughout the feasible radius-budget window $`R=o((\log N)^3)`$. Polynomial preparation time requires $`R=\Omega((\log N)^3)`$; sufficiency at that larger range is not established. The temporal converse does not inherit the companion's broader pairing scope. These are complementary resource statements about the same preparation problem.

## Exact locality and relaxation results

| Source | Operational model and established result | Relation to the present theorem |
| --- | --- | --- |
| Westhoff, Murciano and Moroder [2] | Exact target-preserving quadratic dynamics built from linear combinations of target Bogoliubov annihilators. Under translation invariance, momentum weights determine the relaxation rate; stronger suppression of critical algebraic jump tails forces stronger algebraic growth of preparation time. Appendix F studies specified strictly truncated filters and their overlaps. | The present stationary state may be a mixed approximation. Coefficients and jump families may vary arbitrarily with size. The lower bound optimizes over all strictly supported gain/loss filters at fixed global overlap, rather than fixing an exact-target weight profile or truncation prescription. |
| Tang, Barad and Wen [3] | A spectral criterion for exponentially local dark-state linear jumps. Sign-changing Fermi-level crossings obstruct exact local preparation. Their end matter distinguishes efficient spectral-filter evaluation from mixing; uniform momentum weights give logarithmic mixing but need not be local. | The present finite-size problem permits approximate stationarity and growing strict support. It determines an unavoidable time cost at logarithm-squared range, rather than an exact-target analyticity obstruction. |
| Zhan et al. [4] | Spectrally filtered Lindblad preparation, mixing-time bounds for quasifree models, and rapid mixing for specified weakly interacting gapped spin and fermion classes. The filtered jumps are constructed from Hamiltonian evolution. | These positive results do not impose the present strict-support constraint on a critical Fermi-sea gain/loss reservoir. A short abstract mixing time is not a statement that the required filtered jumps have logarithm-squared strict spatial support. |

For [2], the normalization $`\|B\|_{\mathrm{op}}=1`$ makes the overall dissipative scale explicit. Equations (6)–(8) and Appendix C relate momentum-weight zeros to spatial tails and asymptotic relaxation. Appendix F explains how small amplitudes amplify truncation errors and how profile changes alter finite-size performance. The new converse allows those profile changes and all other admissible gain/loss polynomials; its clipped root-depth estimate rules out a fast optimized replacement at the stated range.

In [3], the jump functions used for exact locality are shared across system sizes. Its end matter gives $`G\propto hP_+`$ and a mixing bound proportional to $`\Delta_h^{-2}\log(N/\epsilon^2)`$; the uniform-weight choice $`G\propto P_+`$ instead has constant mode damping. At a sign-changing Fermi crossing the latter spectral projector is nonlocal. Neither comparison contradicts a time lower bound that simultaneously charges strict spatial support and whole-state fidelity.

## Classical approximation ingredients

Root clustering and root-potential estimates are classical approximation tools. Newman's original paper [5], especially Lemma 3, supplies the continuous complex-root integral budget underlying the argument. Geometrically clustered roots give root-exponential rational approximation. Sherstov's Theorem 5.1 [6] gives sharp uniform rational sign-approximation error on an arithmetic grid; inverse-polynomial error already produces a logarithm-squared degree scale. That scale is not claimed as new approximation theory here.

The discrete curved momentum grid and the total-error budget needed for a whole-state overlap are treated in the spatial companion [1]. The temporal proof adds a logarithmic weight to that root budget. It then uses standard polynomial growth estimates and Jensen's formula to turn forced root depth into attenuation of an actual gain or loss rate near a Fermi point. This controls a physical rate polynomial, including common factors and roots near sampled momenta.

Ordinary rational approximation only controls a ratio. Here

```math
n(k)=\frac{a(k)}{a(k)+b(k)},
\qquad
g(k)=a(k)+b(k).
```

A common positive multiplier changes $`g`$ without changing $`n`$. Its realization also affects polynomial degree and hence support. Consequently an approximation-error or rational-degree bound alone does not fix the preparation time. The temporal theorem bounds the possible rate normalization of all admissible physical representatives. Restricted-denominator approximation is itself an established topic [9]; the present claim is the stated finite-grid, aggregate-error, rate-normalized preparation bound.

Trefethen, Nakatsukasa and Weideman [8] explain exponential and tapered root/pole clustering using potential-theoretic models. Their work provides useful context for the construction and the root geometry. Neither the use of clustered roots nor the use of logarithmic potentials is an independent contribution of this project.

## Gaussian tensor-network antecedent

Franco-Rubio and Cirac [7] study the same critical hopping-chain target through Gaussian fermionic matrix product states. Their rigorous inapproximability theorem requires superpolynomial Gaussian-MPS bond dimension; their CFT and numerical analysis explores sharper scales. Appendix D constructs rational momentum occupations from polynomials and uses logarithmically distributed roots. This supplies an important representational antecedent, including the filter mechanism.

Virtual bond dimension, dissipative jump support and physical preparation time are different resources. The Gaussian-MPS theorem does not directly bound the minimum occupation damping rate of every bounded-strength reservoir. Conversely, the present gain/loss theorem is not a lower bound on arbitrary tensor-network descriptions, general quantum circuits, or non-Gaussian preparation.

## References

The machine-readable bibliography is [references.bib](references.bib).

1. *Fermi Sea Reservoir Locality*, scientific repository, revision [293b8e6914d8ff85ed3605d6c85dc95abfef4b61][1]. See the [range converse][1a], [construction][1b], and [preparation costs][1c].
2. P. Westhoff, S. Murciano and M. Moroder, *Locality-Preparation Time Tradeoffs in Dissipative Quantum Systems*, [arXiv:2610.13784v1][2] (2026). See the main setup, Appendix C, and Appendix F.
3. Q. Tang, R. Barad and X. Wen, *Locality in Dissipative Ground-State Preparation*, [arXiv:2610.40628v1][3] (2026). See the exact spectral criterion and the spectral-filtering end matter.
4. Y. Zhan et al., *Rapid quantum ground state preparation via dissipative dynamics*, Phys. Rev. X **16**, 011004 (2026), [DOI][4a]; [arXiv:2503.15827v3][4]. See Sec. II, Theorems 1–3, and their model restrictions.
5. D. J. Newman, *Rational approximation to $`|x|`$*, Michigan Math. J. **11**, 11–14 (1964), [DOI][5].
6. A. A. Sherstov, *The Intersection of Two Halfspaces Has High Threshold Degree*, SIAM J. Comput. **42**, 2329–2374 (2013), [DOI][6]; [author manuscript][6a].
7. A. Franco-Rubio and J. I. Cirac, *Gaussian matrix product states cannot efficiently describe critical systems*, Phys. Rev. B **106**, 235136 (2022), [DOI][7]; [arXiv:2204.02478][7a].
8. L. N. Trefethen, Y. Nakatsukasa and J. A. C. Weideman, *Exponential node clustering at singularities for rational approximation, quadrature, and PDEs*, Numer. Math. **147**, 227–254 (2021), [DOI][8]; [author manuscript][8a].
9. E. H. Kaufman Jr. and G. D. Taylor, *Uniform approximation by rational functions having restricted denominators*, J. Approx. Theory **32**, 9–26 (1981), [DOI][9].

[1]: https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/tree/293b8e6914d8ff85ed3605d6c85dc95abfef4b61
[1a]: https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/293b8e6914d8ff85ed3605d6c85dc95abfef4b61/science/range_lower_bound.md
[1b]: https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/293b8e6914d8ff85ed3605d6c85dc95abfef4b61/science/reservoir_construction.md
[1c]: https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/293b8e6914d8ff85ed3605d6c85dc95abfef4b61/science/preparation_costs.md
[2]: https://arxiv.org/abs/2610.13784v1
[3]: https://arxiv.org/abs/2610.40628v1
[4]: https://arxiv.org/abs/2503.15827v3
[4a]: https://doi.org/10.1103/wzb3-dbg9
[5]: https://doi.org/10.1307/mmj/1028999029
[6]: https://doi.org/10.1137/100785260
[6a]: https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf
[7]: https://doi.org/10.1103/PhysRevB.106.235136
[7a]: https://arxiv.org/abs/2204.02478
[8]: https://doi.org/10.1007/s00211-020-01168-2
[8a]: https://people.maths.ox.ac.uk/trefethen/clustering.pdf
[9]: https://doi.org/10.1016/0021-9045(81)90018-6
