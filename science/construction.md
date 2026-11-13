# Matching preparation at logarithm-squared range

The temporal converse is attained in order by a positive gain/loss reservoir. This construction, its coefficient rounding and its actual slow rate are inherited from [Fermi-Sea Reservoir Locality](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/tree/293b8e6914d8ff85ed3605d6c85dc95abfef4b61). We reproduce the mechanism and the estimates needed for the present time theorem. The new contribution of this project is the converse over all allowed reservoir designs, proved in [the time bound](time_converse.md).

Throughout, $`N=4M+2`$, $`0\lt\epsilon\lt1`$ and $`\Gamma\gt0`$. The target fills the momenta with positive cosine. Logarithms are natural. The error $`\epsilon`$ is squared pure-target infidelity.

## Positive momentum filters

Set

```math
q_0=\tanh(1/2),\qquad \kappa=-\log q_0,
```

and choose

```math
s=\left\lceil\max\left\{2,\log(N/2)+1,
1+\frac{\log(4N/\epsilon)}{2\kappa}\right\}\right\rceil,
\qquad m=s^2.
```

Define

```math
r_j=e^{-j/s},\qquad
p(x)=\prod_{j=0}^{m-1}(x+r_j),\qquad
h(k)=\frac{p(\cos k)}{p(1)}.
```

Use the gain and loss rates

```math
a(k)=\frac{\Gamma}{2}h(k)^2,\qquad
b(k)=\frac{\Gamma}{2}h(k+\pi)^2,\qquad g(k)=a(k)+b(k).
```

The two amplitudes are Laurent polynomials supported on offsets $`-m,\ldots,m`$. Consequently they are actual translated linear creation and annihilation jumps of radius $`R=m`$. A concrete real-space realization follows by writing

```math
h(k)=\sum_{r=-m}^{m}\alpha_r e^{irk},
\qquad
L_x^+=\sqrt{\Gamma/2}\sum_r\alpha_r c_{x+r}^{\dagger},
\qquad
L_x^-=\sqrt{\Gamma/2}\sum_r(-1)^r\alpha_r c_{x+r}.
```

Each normalized polynomial factor has three nonnegative Fourier coefficients, on offsets $`-1,0,1`$, summing to one. Their convolutions therefore give $`\alpha_r\ge0`$, $`\alpha_{-r}=\alpha_r`$ and $`\sum_r\alpha_r=1`$. This also supplies a finite coefficient construction. The target hopping Hamiltonian commutes with every occupation.

For real momentum, $`|h(k)|\le1`$, since $`|x+r_j|\le1+r_j`$ for $`|x|\le1`$. Thus $`g(k)\le\Gamma`$. At least one of the arguments $`\cos k`$ and $`-\cos k`$ is nonnegative, where $`p`$ is strictly positive, so $`g(k)\gt0`$.

## Whole-state stationary fidelity

For $`x\in[e^{-(m-1)/s},1]`$, at least $`s-1`$ roots have $`|\log(r_j/x)|\le1`$. Every root factor has modulus ratio at most one, and these nearby factors obey

```math
\frac{|r_j-x|}{r_j+x}
=\left|\tanh\frac{\log(r_j/x)}{2}\right|\le q_0.
```

It follows that

```math
\left|\frac{p(-x)}{p(x)}\right|\le q_0^{s-1}.
```

The smallest sampled absolute cosine is $`\sin(\pi/N)\ge2/N`$. The choice of $`s`$ puts every sampled argument in the stated interval and gives a total stationary wrong-occupation budget

```math
e_\infty(k)\le q_0^{2(s-1)},\qquad
\sum_k e_\infty(k)\le\epsilon/4.
```

The unique stationary occupation distribution is a product, with

```math
F_\infty=\prod_k[1-e_\infty(k)]\ge1-\epsilon/4.
```

This is a bound on the entire physical Fermi sea. No uniform per-mode error is assumed in the converse; uniform errors are only a convenient sufficient property of this construction.

## Finite time from arbitrary physical inputs

A useful lower rate bound follows from

```math
p(0)=e^{-(s^3-s)/2},\qquad
0\le\log p(1)\le s+1.
```

At every real momentum at least one nonnegative polynomial argument supplies

```math
g(k)\ge\frac{\Gamma}{2}e^{-s^3-s-2}.
```

For every initial state, including non-Gaussian states, the occupation equations close. The commuting wrong-occupation projectors give an operator union bound, so

```math
1-F_{\rho_0}(t)
\le\sum_k e_\infty(k)+N e^{-g_{\min}t}.
```

Therefore the explicit ideal time

```math
t=\frac{2}{\Gamma}e^{s^3+s+2}\log\frac{2N}{\epsilon}
```

suffices for overlap at least $`1-\epsilon`$ from every physical input. The exact worst-input curve, derived in [the model](model.md), is

```math
\inf_{\rho_0}F_{\rho_0}(t)
=F_\infty\prod_k(1-e^{-g(k)t}).
```

At fixed error, $`s=\log N+O_\epsilon(1)`$, hence

```math
R=O_\epsilon((\log N)^2),\qquad
\log(1+\Gamma t)=O_\epsilon((\log N)^3).
```

Together with the universal temporal converse this proves matching cubic-logarithmic order for the logarithm of the optimized preparation time, at a sufficiently large fixed logarithm-squared range budget. It does not establish an optimal leading constant or a fast construction at larger ranges.

## Finite coefficients and charged resources

The normalized coefficients may be rounded downward with the symmetry retained. The inherited [rounding proof](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/293b8e6914d8ff85ed3605d6c85dc95abfef4b61/science/reservoir_construction.md#dyadic-rounding-theorem) uses

```math
b_{\rm prec}=\left\lceil
\frac{s^3+s+2}{2\log2}+
\log_2\frac{4\sqrt2(2m+1)N}{\epsilon}
\right\rceil
```

fractional bits per independent amplitude coefficient. The resulting total amplitude error is bounded relative to the nonzero two-filter amplitude vector; stationary infidelity stays at most $`\epsilon/2`$ and every rate remains at least $`(\Gamma/4)e^{-s^3-s-2}`$. Doubling the ideal displayed time therefore gives the same complete-state guarantee for that rounded realization. This is a sufficient precision upper bound, not a precision lower bound.

Two translated jump families, one physical fermion mode per site and extensive total local rate are counted. $`\Gamma`$ bounds the sum of gain and loss occupation rates at each momentum, including all families. Neither the coefficient specification nor normalization makes preparation time free. The theorem concerns ideal Markovian generators; deriving a microscopic bath or manufacturing these filters is a separate implementation problem.

The [verification suite](../verification/README.md) evaluates rates as logarithmic products rather than expanding a catastrophically small near-Fermi amplitude in ordinary floating point.
