# A weighted root budget from whole-state accuracy

This page proves the approximation statement used by the [time converse](time_converse.md). The extra logarithmic weight measures how strongly roots near a Fermi point attenuate a normalized physical rate.

## Finite-grid quantities

Let $`N=4M+2\ge1026`$ and define

```math
\begin{aligned}
a&=\lceil N^{1/3}\rceil,& b&=\lfloor N/8\rfloor,&
\delta&=N^{-1/3},\\
x_j&=\tan\frac{(j+1/2)\pi}{N},&
w_j&=\log\frac{x_{j+1}}{x_j},&\nu_j&=\log\frac1{x_j}.
\end{aligned}
```

Only $`a-1\le j\le b+1`$ is needed. Here $`a\le b`$, $`0\lt x_{a-1}\lt x_{b+1}\lt1`$, and the weights $`w_j`$ decrease with $`j`$. Write

```math
\ell=x_{a-1},\quad L=\log(1/\ell),\quad
w=w_a,\quad U=w\nu_a,\quad
T=\tfrac12(\nu_a^2-\nu_{b+1}^2),\quad
\Lambda=2\log\frac{1-\delta}{\delta}.
```

The symbols $`\nu_j`$ are logarithmic weights, unrelated to gain-jump labels in the [model](model.md).

For a complex root $`z`$, including multiplicity, define

```math
h_z(x)=\left|\log\left|\frac{x+z}{x-z}\right|\right|,
\qquad
s_L(z)=\min\{\log_+(1/|z|),L\}.
```

At $`z=0`$, set $`h_0=0`$ and $`s_L(0)=L`$. Real poles have their extended-real values before deletion. The constants used below are

```math
C_0=\frac{\pi^2}{2},\qquad C_1=\frac72\zeta(3).
```

## Lemma 1: one weighted root

For each $`z`$, delete at most two indices from $`\{a,\ldots,b\}`$ as follows. If $`r=|z|\lt x_{a-1}`$ or $`r\ge x_{b+1}`$, delete none. Otherwise choose the unique $`q`$ with $`x_q\le r\lt x_{q+1}`$ and delete $`\{q,q+1\}\cap\{a,\ldots,b\}`$. If $`h_z=0`$, no deletion is needed.

For the retained indices, and after any additional deletions,

```math
\boxed{
\sum_j w_j\nu_j h_z(x_j)
\le C_0s_L(z)+C_1+C_0w.
}
```

**Proof.** For $`r>0`$, the real-root kernel bounds the complex one:

```math
h_z(x)\le h_r(x)
=K(\log(x/r)),\qquad
K(y)=\log\coth(|y|/2).
```

The kernel is nonnegative, even and integrable. Expansion on the positive half-line gives

```math
K(y)=2\sum_{m\ge0}\frac{e^{-(2m+1)y}}{2m+1},\quad y>0,
\qquad
\int_{\mathbb R}K(y)\,dy=C_0,
\qquad
\int_{\mathbb R}|y|K(y)\,dy=C_1.
```

For $`\alpha=|\mathrm{Re}z|`$, the actual kernel can be written as

```math
h_z(x)=\tfrac12\log\frac{x^2+r^2+2\alpha x}{x^2+r^2-2\alpha x}.
```

Its derivative has the sign of $`r^2-x^2`$ when $`\alpha>0`$; when $`\alpha=0`$ it vanishes identically. Thus the actual $`h_z`$ is increasing up to $`r`$ and decreasing afterwards. The inherited two-index deletion allows disjoint integration cells: assign the right cell $`[x_j,x_{j+1}]`$ on the increasing branch and the left cell $`[x_{j-1},x_j]`$ on the decreasing branch. On a right cell,

```math
\nu_j\le\log(1/x)+w,\qquad h_z(x_j)\le h_z(x).
```

On a left cell, $`\nu_j\le\log(1/x)`$, $`h_z(x_j)\le h_z(x)`$ and $`w_j\le w_{j-1}`$. The assigned cells do not overlap and lie inside $`[\ell,x_{b+1}]`$. Consequently the discrete sum is bounded by

```math
I_z+C_0w,\qquad
I_z=\int_{\ell}^{x_{b+1}}\log(1/x)h_z(x)\,\frac{dx}{x}.
```

If $`r\lt\ell`$, the logarithmic weight is at most $`L`$, so $`I_z\le C_0L`$. If $`r\ge\ell`$, put $`y=\log(x/r)`$. Since $`x\lt1`$ on the integration interval,

```math
\log(1/x)\le\log_+(1/r)+|y|,
\qquad
I_z\le C_0\log_+(1/r)+C_1.
```

These cases give $`I_z\le C_0s_L(z)+C_1`$. At $`z=0`$ the original kernel vanishes and the statement holds directly. Nonnegativity permits further deletions. $`\square`$

The deletion is essential: a root arbitrarily close to a sampled point can create an arbitrarily large individual discrete log term.

## Lemma 2: aggregate error forces cubic root cost

Suppose occupations $`n(k)\in[0,1]`$ have total wrong-occupation error at most $`E`$, relative to the Fermi sea. Suppose their odds on the tangent grid are

```math
\frac{n(\pi/2+2\arctan x)}{1-n(\pi/2+2\arctan x)}
=\frac{A(x)}{B(x)},
```

with nonzero polynomials $`A,B`$ and total root multiplicity $`d=\deg A+\deg B`$. Exact zero or infinite odds are permitted before root deletion. Then

```math
\boxed{
\sum_{z\in\mathcal Z(A)\sqcup\mathcal Z(B)}s_L(z)
\ge
\frac{
\left[\Lambda\{T-U(2d+E/\delta)\}
-d(C_1+C_0w)\right]_+
}{C_0}.
}
```

**Proof.** The selected paired momenta

```math
k_j^\pm=\pi/2\pm(2j+1)\pi/N,
\qquad a\le j\le b,
```

belong to $`K_N`$. The minus mode is occupied in the target and the plus mode empty. All selected physical modes are distinct.

Delete the union of Lemma 1's root deletions; at most $`2d`$ nodes are lost. Also delete a node if either selected occupation error exceeds $`\delta`$. At most $`E/\delta`$ nodes are lost for this reason, because the physical modes are distinct. Denote the surviving set by $`G`$.

Every node has weight $`w_j\nu_j\le U`$. Moreover,

```math
\sum_{j=a}^b w_j\nu_j
=\tfrac12\sum_{j=a}^b(\nu_j^2-\nu_{j+1}^2+w_j^2)
\ge T.
```

Thus $`\sum_{j\in G}w_j\nu_j\ge T-U(2d+E/\delta)`$. At surviving nodes both odds are finite and positive, and their log difference obeys

```math
q_j:=\log\frac{n(k_j^-)}{1-n(k_j^-)}
-\log\frac{n(k_j^+)}{1-n(k_j^+)}\ge\Lambda.
```

Factor $`A,B`$. Their leading coefficients cancel between opposite arguments, giving

```math
q_j\le\sum_{z\in\mathcal Z(A)\sqcup\mathcal Z(B)}h_z(x_j).
```

Apply Lemma 1, with the common additional deletions, to conclude

```math
\Lambda\{T-U(2d+E/\delta)\}
\le C_0\sum_zs_L(z)+d(C_1+C_0w).
```

The left side may be negative; the root cost is nonnegative. Taking its implied positive-part lower bound proves the result. $`\square`$

## Scaling and inherited ingredients

At fixed $`E`$ and $`d=O((\log N)^2)`$,

```math
\begin{aligned}
\nu_a&=\tfrac23\log N-\log\pi+o(1),&
w&=(1+o(1))N^{-1/3},\\
T&=(\tfrac29+o(1))(\log N)^2,&
\Lambda&=(\tfrac23+o(1))\log N.
\end{aligned}
```

The occupation-bad deletion contributes $`O_E((\log N)^2)`$ after multiplication by $`\Lambda`$; root-deletion and per-root constant terms are also lower order. Therefore

```math
\sum_zs_L(z)
\ge\left(\frac8{27\pi^2}+o(1)\right)(\log N)^3.
```

The unweighted logarithmic-kernel estimate is classical: see D. J. Newman, *Rational approximation to* $`|x|`$, Michigan Math. J. **11**, 11–14 (1964), [Lemma 3 on p. 13](https://doi.org/10.1307/mmj/1028999029). Its continuous root integral is credited here; the displayed kernel expansion gives a self-contained calculation of the mass and first moment used in the weighted proof.

The tangent grid, aggregate-error treatment, unimodality and two-node deletion are inherited from the [pinned unweighted scalar argument](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/293b8e6914d8ff85ed3605d6c85dc95abfef4b61/science/range_lower_bound.md). Here the lower endpoint is chosen closer to the Fermi point and each node receives the additional $`\log(1/x)`$ weight. The finite first moment of the root kernel controls that extra weight. This is the step that supplies the temporal cubic logarithm.
