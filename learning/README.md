# Learn the preparation-time theorem

A reservoir may have the right destination and still take an extremely long time to get there. This project asks how quickly a spatially compact reservoir can prepare an entire critical Fermi sea from an arbitrary physical initial state.

The learning route uses one anchor: **Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems* (Oxford University Press, 2002)**. Start with the [source bridge](anchor_bridge.md) for a short section map and the translations needed here. The [30 milestones](milestones.md) organize 14 background targets followed by 16 targets tracing the new argument. They are a map of the science, with no prior assessment or personal progress assumed.

## A route through the whole story

| Step | What becomes understandable | Read |
| --- | --- | --- |
| One mode | A gain rate fixes filling, a loss rate fixes emptying, and their sum fixes occupation relaxation. | The worked example below; [bridge](anchor_bridge.md#one-mode-dynamics-and-the-conventions-that-matter) |
| The full register | A good average occupation is different from a good probability of the entire Fermi-sea pattern. The worst input can be identified exactly. | [Model](../science/model.md#complete-register-score) |
| Spatial support | A finite-support jump becomes a finite-degree Fourier polynomial. Stationary occupations depend on a ratio of rates. | [Bridge](anchor_bridge.md#from-spatial-support-to-a-polynomial-question); [rate polynomials](../science/time_converse.md#rate-polynomials-and-their-finite-ring-norm) |
| The new obstruction | Accuracy across many scales forces roots deep near a Fermi point; bounded physical rates then force slow relaxation. | [Weighted root budget](../science/root_budget.md); [time converse](../science/time_converse.md) |
| The complete result | The inherited reservoir attains the same cubic-logarithmic time order that every admissible compact reservoir must pay. | [Construction](../science/construction.md); [limitations](../science/limitations.md) |

The background phase ends by assembling the physical task and the polynomial representation. The narrative phase follows the weighted-root mechanism through its physical rate bound, matching construction and scope. The specialist proof pages remain the authority for constants and finite-size conditions.

## Worked example: two occupations, one slow mode

Consider two fermionic normal modes, with annihilation operators $`c_1,c_2`$ and number projectors $`n_i=c_i^\dagger c_i`$. The desired occupation pattern is $`|10\rangle`$: fill mode 1 and empty mode 2. A density matrix supported on this odd-particle vector is a physical fermionic state. The generator has no coherent term and uses

```math
\mathcal L=\sum_{i=1}^{2}
\left(a_i\mathcal D[c_i^\dagger]+b_i\mathcal D[c_i]\right),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
```

The nonnegative numbers $`a_i`$ and $`b_i`$ are rates: the corresponding jump amplitudes are $`\sqrt{a_i}`$ and $`\sqrt{b_i}`$. Choose a positive rate scale $`\gamma`$ and the following rates.

| Mode | Desired bit | Gain $`a_i`$ | Loss $`b_i`$ | Total rate $`g_i=a_i+b_i`$ | Stationary correct-bit probability |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | $`3\gamma/4`$ | $`\gamma/4`$ | $`\gamma`$ | $`3/4`$ |
| 2 | 0 | $`\gamma/40`$ | $`3\gamma/40`$ | $`\gamma/10`$ | $`3/4`$ |

For either mode the occupation expectation solves

```math
\frac{d}{dt}\langle n_i\rangle
=a_i-g_i\langle n_i\rangle,
\qquad
\langle n_i\rangle_t
=\frac{a_i}{g_i}
+\left(\langle n_i\rangle_0-\frac{a_i}{g_i}\right)e^{-g_it}.
```

Thus $`a_i/g_i`$ is the stationary filling, while $`1/g_i`$ is the occupation relaxation time. Mode 2 has the same stationary accuracy as mode 1 but relaxes ten times more slowly.

The stationary probability of the **whole** target pattern is

```math
F_\infty=\frac34\frac34=\frac9{16}.
```

This score is squared pure-target fidelity, $`F(t)=\langle10|\rho(t)|10\rangle`$. It is the probability that both occupation measurements return their desired bits in the same run. It is not the average of two separate correct-bit probabilities.

The worst initial pattern is the complementary one, $`|01\rangle`$. Each mode starts wrong. Their correct-bit probabilities are $`(3/4)(1-e^{-g_it})`$, so

```math
F_{\min}(t)=\frac9{16}
(1-e^{-\gamma t})(1-e^{-\gamma t/10}).
```

This is the minimum over all physical initial density matrices, including states with occupation coherences. To see why, evolve the target projector in the Heisenberg picture. It remains diagonal in the occupation basis. For one mode, starting in the correct bit adds $`e^{-g_it}`$ to the probability obtained from the wrong bit. The diagonal target-transition kernel is a product of these nonnegative factors, so $`|01\rangle`$ gives its smallest eigenvalue. An arbitrary initial density matrix supplies a convex combination of diagonal entries; its coherences cannot lower that minimum. The [model](../science/model.md#complete-register-score) gives the general argument.

At $`t=10\log2/\gamma`$, the fast mode has nearly relaxed but the slow factor is only $`1/2`$:

```math
F_{\min}(t)=\frac9{32}(1-2^{-10})\approx0.2810.
```

For a requested overlap $`f=1/2`$, a simple necessary condition comes from dropping the fast factor:

```math
\frac9{16}(1-e^{-\gamma t/10})\ge\frac12
\quad\Longrightarrow\quad
t\ge\frac{10\log9}{\gamma}.
```

This necessary time is about $`21.97/\gamma`$. At $`t=30/\gamma`$, direct substitution gives $`F_{\min}(t)\approx0.5345`$, so that time suffices. A requested overlap of $`0.6`$ is never attained from every input: it already exceeds $`F_\infty=0.5625`$.

Finally, multiply both $`a_2`$ and $`b_2`$ by a small positive factor. The stationary state remains the same, because their ratio remains the same, but the second mode becomes still slower. This is the distinction the many-mode theorem resolves: an accurate occupation ratio alone does not determine preparation time.

The example explains the dynamics and scoring. It is not a small-size demonstration of the large-ring root bound or a claim about the necessary support of these two normal-mode jumps.

## From two modes to a critical sea

In the ring, the desired bit changes across two Fermi points. A reservoir must sharply separate occupied and empty momenta while keeping its real-space jumps compact. The main theorem shows that all admissible gain/loss filters pay a severe time cost at logarithm-squared radius:

```math
\log(1+\Gamma T_{\mathrm{opt}})=\Theta((\log N)^3).
```

Here the target whole-state overlap stays fixed in $`(0,1)`$, and an attaining radius coefficient must be sufficiently large. The more general necessary inequality is $`\log(1+\Gamma t)+CR\ge c(\log N)^3`$. It requires at least cubic-logarithmic radius for polynomial preparation time, without establishing a polynomial-time construction there.

The result concerns time-independent, one-site-translation-invariant separate linear gain/loss jumps, one physical fermion mode per cell, number-conserving quadratic coherent dynamics and bounded momentum occupation rates. Pairing, extra modes, feedback and time-dependent control are different architectures. The [bridge](anchor_bridge.md#the-bridge-ends-at-the-actual-theorem) connects these qualifications to the proof rather than treating them as optional details.
