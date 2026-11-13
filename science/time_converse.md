# Finite-size temporal converse

The [model](model.md) fixes the separate gain/loss class, physical inputs and rate normalization. This page converts the [weighted root budget](root_budget.md) into an unavoidable preparation time. It uses a small physical occupation damping rate, without identifying it with the full fermionic Liouvillian gap.

## Rate polynomials and their finite-ring norm

Every gain or loss rate is a nonnegative trigonometric polynomial of degree at most $`2R`$. Under

```math
x=\tan[(k-\pi/2)/2],
```

there are real polynomials $`A,B`$, nonnegative on the real axis, such that

```math
 a(k(x))=\frac{A(x)}{(1+x^2)^{2R}},\qquad
 b(k(x))=\frac{B(x)}{(1+x^2)^{2R}},
 \qquad \deg A,\deg B\le4R.
```

This follows by substituting the fractional-linear expression for $`e^{ik}`$ into a Laurent polynomial of degree at most $`2R`$ and multiplying by the displayed common denominator. The representation remains valid for arbitrarily many jump families and for coefficient cancellations. No positivity of individual polynomial coefficients is assumed.

Assume for the moment that $`2\pi R/N\le1/2`$. Trigonometric Bernstein's inequality gives

```math
\|g'\|_\infty\le2R\|g\|_\infty.
```

A maximizer lies within $`\pi/N`$ of a grid point. The finite-ring budget therefore implies

```math
\|g\|_\infty\le\frac{\Gamma}{1-2\pi R/N}\le2\Gamma.
```

Because the continuous rates are nonnegative, $`a,b\le g`$. Thus, for either $`P=A`$ or $`P=B`$,

```math
\max_{x\in[-1,1]}|P(x)|\le2\Gamma\,2^{2R}.
```

Expand $`P`$ in Chebyshev polynomials. Its constant coefficient has magnitude at most this interval norm and every other coefficient at most twice it. On $`|z|\le1/2`$, the recurrence implies $`|T_j(z)|\le2^j`$. Summing the resulting geometric bound, with $`\deg P\le4R`$, yields the explicit complex norm

```math
\boxed{\max_{|z|\le1/2}|P(z)|\le\Gamma\,2^{6R+3}.}
```

## Root cost forces a small desired rate

Use the finite-grid quantities $`a,b,\delta,\ell,L,w,U,T,\Lambda,C_0,C_1`$ from [the root-budget page](root_budget.md#finite-grid-quantities). Suppose $`\ell\le1/16`$. For every real center $`x_*`$ with $`|x_*|\le\ell`$, Jensen's formula on the disk of radius $`1/4`$ centered there gives

```math
\log|P(x_*)|
\le\log(\Gamma 2^{6R+3})
-\sum_z\log_+\frac{1/4}{|z-x_*|}.
```

A zero at the center is interpreted by continuity and already gives a zero rate. For a root with $`|z|\lt1/8`$, its distance to the center is at most $`2\max\{|z|,\ell\}`$, and it lies in this disk. Therefore its Jensen penalty is at least $`s_L(z)-\log8`$. For every other root, $`s_L(z)\le\log8`$. Consequently,

```math
\sum_z\log_+\frac{1/4}{|z-x_*|}
\ge\sum_zs_L(z)-4R\log8,
```

and hence, writing $`S_P=\sum_{z\in\mathcal Z(P)}s_L(z)`$,

```math
\boxed{|P(x_*)|\le\Gamma\,2^{18R+3}e^{-S_P}.}
```

Common factors only increase this root cost; they cannot evade the physical norm bound by an arbitrary rescaling.

Let a finite-time all-input guarantee $`F_{\min}(t)\ge f`$ hold, and put $`E=E_f=-\log f`$. Among the $`m=\lfloor4E\rfloor+1`$ nearest occupied modes on the selected side of a Fermi point, at least one has wrong-occupation error at most $`1/4`$. Otherwise their total error would exceed $`E`$. The same holds on the empty side. If $`m\le a`$, their tangent coordinates have magnitude at most $`\ell`$.

The root budget applies with $`d\le8R`$. Thus at least one of $`A,B`$ has cost at least half the explicit lower bound below. If it is $`A`$, choose the good occupied mode, where $`a/g\ge3/4`$. If it is $`B`$, choose the good empty mode, where $`b/g\ge3/4`$. In either case a physical mode obeys

```math
 g(k_*)\le\frac43\Gamma\,2^{18R+3}e^{-S_P}.
```

This selects the side where the attenuated polynomial is the desired rate. Smallness of an unwanted rate alone would not control the damping.

## Finite-size theorem

Let $`N=4M+2\ge1026`$, $`f\in(0,1)`$, and use the elementary finite-grid quantities defined above. Assume

```math
\ell\le1/16,\qquad
\lfloor4E_f\rfloor+1\le a,\qquad
2\pi R/N\le1/2.
```

These are explicit, checkable conditions. At every fixed $`f`$ they hold for all sufficiently large sizes whenever $`R=O((\log N)^2)`$. Define

```math
\begin{aligned}
E_f&=-\log f,& \chi_f&=-\log(1-f),\\
Z_N(R,f)&=
\frac{
\left[\Lambda\{T-U(16R+E_f/\delta)\}
-8R(C_1+C_0w)\right]_+
}{C_0}.
\end{aligned}
```

**Theorem.** Every allowed device with $`F_{\min}(t)\ge f`$ satisfies

```math
\boxed{
\Gamma t\ge\frac{3\chi_f}{32}
\exp\!\left[\frac{Z_N(R,f)}2-18R\log2\right].
}
```

**Proof.** Finite success excludes zero-rate modes. The exact population curve in the model gives $`F_\infty\ge f`$ and aggregate error at most $`E_f`$. Lemma 2 then gives $`S_A+S_B\ge Z_N(R,f)`$. Select $`P`$ and its good physical mode as above, so $`S_P\ge Z_N(R,f)/2`$.

The all-input curve is bounded above by any single factor:

```math
 F_{\min}(t)\le1-e^{-g(k_*)t}.
```

Thus $`g(k_*)t\ge\chi_f`$. Combining this with the desired-rate bound gives

```math
\Gamma t\ge\frac34\chi_f\,2^{-18R-3}e^{S_P},
```

which is the displayed theorem. $`\square`$

The inequality may be weak or vacuous at a finite size; its positive part is not a numerical assertion that the radius is feasible. It is a universal necessary condition for any device attaining the specified overlap.

## Cubic logarithm and the radius-time consequence

For fixed $`f`$ and $`R\le K(\log N)^2`$ with fixed $`K`$, the root-budget asymptotics give

```math
 Z_N(R,f)\ge
\left(\frac8{27\pi^2}+o(1)\right)(\log N)^3.
```

The $`18R\log2`$ term is lower order. Therefore

```math
\liminf_{N\to\infty}
\frac{\log(\Gamma t)}{(\log N)^3}
\ge\frac4{27\pi^2}.
```

The finite inequality also supplies a linear radius-time tradeoff. Dropping the positive part to obtain a weaker valid bound gives

```math
\log(\Gamma t)+A_N R\ge B_N(f),
```

where

```math
\begin{aligned}
A_N&=18\log2+
\frac{16\Lambda U+8(C_1+C_0w)}{2C_0},\\
B_N(f)&=\frac{\Lambda(T-U E_f/\delta)}{2C_0}
+\log\frac{3\chi_f}{32}.
\end{aligned}
```

Here $`A_N`$ tends to the finite constant $`18\log2+4C_1/C_0`$, while

```math
B_N(f)=\left(\frac4{27\pi^2}+o(1)\right)(\log N)^3.
```

This proves $`\log(1+\Gamma t)+C R\ge c(\log N)^3`$ for some fixed positive constants and all sufficiently large sizes satisfying the sampling condition. If that condition fails, $`R>N/(4\pi)`$ already dominates a cubic logarithm, so the stated asymptotic resource inequality remains valid after reducing $`c`$ if needed.

In particular, every polynomial-time sequence $`\Gamma t\le N^p`$ with fixed $`p`$ must have $`R=\Omega((\log N)^3)`$. This is a necessary radius condition, not an attaining polynomial-time theorem.

## Optimizing under a radius budget

Let $`\mathcal R_N`$ be an allowed radius budget, and use the fixed-$`\Gamma`$ optimized time $`T_{\mathrm{opt}}(N,\mathcal R_N,f)`$ defined in the [model](model.md#complete-register-score). If

```math
K_0(\log N)^2\le\mathcal R_N=o((\log N)^3),
```

where the fixed $`K_0`$ is large enough for the [inherited construction](construction.md), then the optimal time obeys

```math
\log(1+\Gamma T_{\mathrm{opt}}(N,\mathcal R_N,f))=\Theta((\log N)^3).
```

The universal linear tradeoff gives the lower order because $`C\mathcal R_N=o((\log N)^3)`$. The construction supplies the upper order while using only $`O((\log N)^2)`$ of the available radius. This is a matching time order throughout a radius-budget window, without a matching theorem at or beyond cubic-logarithmic radius.

## What the converse does and does not establish

The time cost is optimized over every allowed rate polynomial, coefficient choice and finite number of translated gain/loss families. It is not limited to the inherited geometric-root construction. The proof permits arbitrary physical input states and arbitrary number-conserving translation-invariant quadratic Hamiltonians.

The restriction to separate gain/loss jumps is load-bearing. General creation-annihilation jumps, pairing Hamiltonians, additional cell modes, measurements or time-dependent controls can change the stationary equations and lie outside this theorem. The result concerns effective Markovian dynamics; it does not optimize coefficient precision, microscopic reservoir engineering or a quantum-versus-classical computational comparison.
