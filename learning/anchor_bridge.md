# From open-system dynamics to the Fermi-sea time bound

The single educational anchor is **H.-P. Breuer and F. Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002)**. Its statistical description of states, quantum operations and Markovian master equations supplies the opening language. The fermionic reduction, spatial-filter problem and weighted-root converse are developed in this project.

The [publisher's book record](https://academic.oup.com/book/27757) provides an access route. Oxford's online record is dated 2007 and identifies the paperback ISBN 9780199213900; the selected anchor remains the 2002 book, ISBN 9780198520634. Section identifiers below were checked against the published contents, with the publisher's chapter records confirming their subjects. They are reading pointers, not a claim that the textbook proves the new theorem or that every chapter is required.

## A focused section map

| Foundation needed here | Anchor pointer | How it enters the project |
| --- | --- | --- |
| Classical transitions and a master equation | §1.4.4 | An empty occupation gains a particle, and a filled occupation loses one. This becomes a two-state chain after the quantum reduction. |
| States, measurement probabilities and composite systems | §§2.1.3–2.1.4; §2.2.1 | A density matrix includes mixtures and coherences; the target projector scores the entire register. |
| Physical quantum maps | §§2.4.2–2.4.3 | Complete positivity is the appropriate consistency condition for open-system evolution. |
| State evolution versus observable evolution | §§3.1.2–3.1.3 | The adjoint evolution of the target projector exposes the exact worst input. |
| A fixed Markovian generator | §§3.2.1–3.2.3 | A semigroup, its Lindblad generator and its adjoint give the dynamics assumed in the model. |
| A familiar elementary decay model | §3.4.2, optional analogy | One fermionic occupation has two values, but the many-mode fermionic channel must still be treated using the canonical anticommutation relations. |

Publisher chapter entries: [Quantum Probability, Chapter 2](https://doi.org/10.1093/acprof:oso/9780199213900.003.02) and [Quantum Master Equations, Chapter 3](https://doi.org/10.1093/acprof:oso/9780199213900.003.03). These identify the same anchor. Research papers in [related work](../references/RELATED_WORK.md) provide attribution and scientific comparisons, rather than additional educational anchors.

## One-mode dynamics and the conventions that matter

A fermionic mode can be empty, $`|0\rangle`$, or occupied, $`|1\rangle`$. Its annihilator $`c`$ takes an occupied mode to the empty state, and $`c^\dagger`$ performs the reverse change. The number operator $`n=c^\dagger c`$ is a projector: its possible measurement outcomes are 0 and 1.

In the convention used throughout the repository,

```math
\mathcal L(\rho)=-i[H,\rho]
+a\mathcal D[c^\dagger](\rho)+b\mathcal D[c](\rho),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
```

The gain and loss jump operators may equivalently be written $`\sqrt a\,c^\dagger`$ and $`\sqrt b\,c`$. The square roots matter: multiplying a jump amplitude by a factor multiplies its rate by the square of that factor.

The adjoint is defined by $`\mathrm{Tr}[O\mathcal L(\rho)]=\mathrm{Tr}[\mathcal L^\dagger(O)\rho]`$. When the coherent Hamiltonian commutes with $`n`$,

```math
\mathcal L^\dagger(n)=a(1-n)-bn,
\qquad
\frac{d}{dt}\langle n\rangle=a-(a+b)\langle n\rangle.
```

The ratio $`a/(a+b)`$ fixes the destination; the sum $`g=a+b`$ fixes occupation relaxation. This separates a stationary approximation problem from a time problem. The [two-mode example](README.md#worked-example-two-occupations-one-slow-mode) computes both from beginning to end.

| Textbook concept | Repository convention or specialization | Consequence for reading the theorem |
| --- | --- | --- |
| Reduced density matrix | $`\rho`$ may be any physical fermionic state, not only a Gaussian state. | Solving covariance dynamics alone would not justify the stated all-input score. |
| A Markovian semigroup | $`e^{t\mathcal L}`$ with one time-independent generator | Intermediate controls, feedback and time dependence are outside the result. |
| Hamiltonian plus dissipator | A number-conserving translation-invariant quadratic $`H`$, and separate linear gain/loss jumps | In momentum space $`H`$ commutes with every occupation and cannot speed this score. Pairing is outside this temporal proof. |
| Relaxation rate | $`g(k)=a(k)+b(k)`$ | This is a physical occupation damping rate; it is not identified with the full Liouvillian spectral gap. |
| A transition probability | $`F=\langle\mathrm{FS}_N|\rho|\mathrm{FS}_N\rangle`$ | This is squared pure-target fidelity, with all occupation bits correct at once. |
| A dissipative time scale | $`\max_{k\in K_N}g(k)\le\Gamma`$ | Time cannot be shortened by multiplying all rates without limit. $`\Gamma`$ is an effective rate budget, not a microscopic bath-cost model. |

The theorem assumes the effective Lindblad description. It does not derive a bath from a system-environment Hamiltonian or certify the accuracy of a weak-coupling approximation for exponentially long laboratory times.

## The fermionic and whole-register steps supplied here

For many modes the canonical anticommutation relations are

```math
\{c_k,c_l^\dagger\}=\delta_{kl},\qquad
\{c_k,c_l\}=0.
```

These relations determine the signs of Fock-space operators. An occupation projector is even in the fermionic operators. In the adjoint action on any function of occupations, signs from a jump and its adjoint cancel. The diagonal occupation algebra therefore evolves as a product of classical gain/loss chains. This statement concerns that algebra; it does not replace the full fermionic channel by an unqualified tensor product of qubit channels.

The [model](../science/model.md#complete-register-score) proves the cancellation and then evolves the entire target projector. If $`e(k)`$ is the stationary wrong-bit probability, it obtains

```math
F_\infty=\prod_k(1-e(k)),
\qquad
F_{\min}(t)=F_\infty\prod_k(1-e^{-g(k)t}).
```

The complementary Fock state attains this minimum. Its projector commutes with fermion parity even when its particle number is odd, so it is an allowed physical witness. Since the evolved target projector is diagonal, non-Gaussian initial states and occupation coherences cannot lower its smallest eigenvalue.

A fixed positive guarantee $`F_{\min}(t)\ge f`$ implies

```math
\prod_k(1-e(k))\ge f,
\qquad
\sum_k e(k)\le-\log f.
```

The second implication follows from $`-\log(1-e)\ge e`$. It bounds the **sum** of errors. It does not say that every mode has error of order $`1/N`$. The root argument must explicitly tolerate a limited number of exceptional modes.

## From spatial support to a polynomial question

Translation invariance makes momentum a useful basis. A jump supported on offsets $`-R,\ldots,R`$ has a Fourier amplitude that is a Laurent polynomial: a finite sum of powers $`e^{irk}`$. Summing squared amplitudes gives nonnegative rates $`a(k),b(k)`$, each a trigonometric polynomial of degree at most $`2R`$. The stationary occupation is

```math
n_\infty(k)=\frac{a(k)}{a(k)+b(k)}.
```

The target occupation jumps from one side of the Fermi point to the other. Near a point use the coordinate $`x=\tan[(k-\pi/2)/2]`$. The [rate-polynomial reduction](../science/time_converse.md#rate-polynomials-and-their-finite-ring-norm) writes

```math
a(k(x))=\frac{A(x)}{(1+x^2)^{2R}},\qquad
b(k(x))=\frac{B(x)}{(1+x^2)^{2R}},
\qquad \deg A,\deg B\le4R.
```

The occupation odds are $`A/B`$. Their ratio controls accuracy, whereas their absolute scale controls time. Multiplying both by a common factor preserves the odds and can alter damping. This is why a rational approximation theorem by itself cannot finish the temporal argument.

## Why the new proof needs a weighted root budget

Factor $`A`$ and $`B`$ into their complex roots. A root contributes a logarithmic potential to the difference between odds at opposite distances from a Fermi point. Roots near sampled momenta can produce large individual terms, so the [root-budget proof](../science/root_budget.md#lemma-1-one-weighted-root) deletes at most two nearby nodes per root before comparing a discrete sum with an integral. Nodes with large occupation error are also charged against the finite total-error budget.

The inherited unweighted argument counts how many roots are needed. The temporal proof additionally weights each distance $`x`$ by $`\log(1/x)`$. At good nodes the occupied and empty odds differ by order $`\log N`$; the logarithmically weighted mesh has mass of order $`(\log N)^2`$. Their product forces a total clipped root depth of order $`(\log N)^3`$.

The clipping prevents a single root arbitrarily close to the crossing from acquiring unbounded credit. A finite first moment of the root kernel controls the extra weight. The [weighted lemmas](../science/root_budget.md) supply these calculations, including the deletion rules, kernel integrals and exceptional-node accounting. The textbook introduces neither this finite-grid approximation problem nor its solution.

## From deep roots to an actual slow occupation

Jensen's formula relates roots inside a disk to how small a polynomial must be near its center when its outer magnitude is bounded. Here the finite-ring rate budget first bounds the physical rate polynomials on a real interval, then a Chebyshev expansion bounds them on a fixed complex disk. Combining those bounds with the forced root depth gives a very small value of either $`A`$ or $`B`$ near a Fermi point.

That alone is not enough. A very small **unwanted** rate is desirable and need not slow relaxation. The [desired-rate selection](../science/time_converse.md#root-cost-forces-a-small-desired-rate) chooses a correctly approximated occupied mode when $`A`$ is small, or an empty mode when $`B`$ is small. There the small rate is at least three quarters of the total rate, so the total $`g(k_*)`$ must also be small.

Finally the exact all-input curve contains the factor $`1-e^{-g(k_*)t}`$. Starting that mode in its wrong occupation is a physical way to expose the delay. This completes the connection from a complex root estimate to an actual preparation-time obstruction, without assuming that an occupation rate equals a global spectral gap.

## The bridge ends at the actual theorem

At fixed whole-state overlap $`f\in(0,1)`$, every successful device in the stated gain/loss class satisfies

```math
\log(1+\Gamma t)+CR\ge c(\log N)^3.
```

At an available radius of sufficiently large logarithm-squared order, the [inherited geometric-root reservoir](../science/construction.md) attains the same cubic-logarithmic order for the logarithm of preparation time. Thus its slowdown is necessary for this reservoir class, not merely an unfortunate coefficient choice. The optimized time retains that order throughout the feasible radius-budget window below cubic-logarithmic order stated in the [converse](../science/time_converse.md#optimizing-under-a-radius-budget).

Polynomial time consequently needs at least cubic-logarithmic radius. An attaining polynomial-time construction at that radius, arbitrary pairing dynamics, extra cell modes and general preparation architectures remain outside the result. The [limitations](../science/limitations.md) keep these distinctions with the claim. The [milestone map](milestones.md) ends by assembling this result, its inherited foundations and its precise physical scope.
