# Preparation time with pairing and bounded dissipation

## Model and theorem

Let $`N=4M+2`$ and fill the momenta with $`\cos k>0`$ on the periodic ring, with one physical fermionic mode per site and no auxiliaries. Consider a time-independent Lindbladian with a one-site-translation-invariant quadratic Hamiltonian and translated linear fermionic jump families of radius $`R_J`$. Pairing is allowed. There is no restriction on the strength or spatial range of the Hamiltonian. Let $`g(k)`$ be the sum of squared Fourier jump coefficients for the pair $`\{k,-k\}`$, and normalize by $`\max_k g(k)\le\Gamma`$ for $`\Gamma>0`$, counting the scalar polynomial twice at $`0,\pi`$ by definition. Let $`t`$ attain squared overlap at least fixed $`f\in(0,1)`$ from every parity-invariant physical density matrix. There are $`c_f>0`$ and $`S_f<\infty`$ such that for $`S=N/(R_J+1)\ge S_f`$,

```math
\log(1+\Gamma t)\ge c_f [\log S]^3.
```

For polynomial normalized time $`\Gamma t\le N^p`$ with fixed $`p>0`$, this gives $`R_J+1\ge N\exp[-O_{f,p}((\log N)^{1/3})]`$ (also valid if $`S\lt S_f`$). For each fixed $`0<\epsilon<1`$, any $`R_J\le N^{1-\epsilon}`$ entails cubic-logarithmic normalized log-time. The inherited $`O((\log N)^2)`$-radius separate gain/loss filters attain the same time order for every budget from a sufficiently large constant times $`(\log N)^2`$ up to $`N^{1-\epsilon}`$. At radius $`N/2`$, inverse discrete Fourier transforms of the two occupation masks give exact rate-filter preparation in $`O_f(\Gamma^{-1}\log N)`$, the unrestricted-radius optimal time order. The smallest radius that allows polynomial time remains open up to the displayed subpolynomial factor.

The [stationary companion result](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/main/science/jump_radius.md) allows unrestricted jump and Hamiltonian strengths. If there is a unique physical stationary state with overlap at least $`f`$, then $`R_J=\Omega_f((\log N)^2)`$ even with unrestricted translation-invariant quadratic Hamiltonian. The existing filters give the matching order. The same radius lower bound applies under finite all-input success. The temporal result needs neither uniqueness nor convergence as a hypothesis.

## 1. A scalar rate score for a paired reservoir

Fourier mix the translations of the jumps. For distinct $`k,-k`$ use canonical Nambu annihilators $`d=(c_k,c_{-k}^\dagger)^T`$, with physical particle and hole related by the second entry. Use $`u_\mu(k)=\sum_r u_{\mu,r}e^{ikr}`$ and $`v_\mu(k)=\sum_r v_{\mu,r}e^{ikr}`$ for the same Fourier label. For each jump family the $`k`$ channel is $`u_\mu(k)d_1+v_\mu(k)d_2`$ and the $`-k`$ channel is $`v_\mu(-k)d_1^\dagger+u_\mu(-k)d_2^\dagger`$. The common trigonometric degree bound for each $`u_\mu,v_\mu`$ is $`R_J`$. Let $`G`$ be the gain Gram matrix in the $`d`$ frame, $`B`$ the loss Gram matrix, and $`D=G+B`$. With $`M_{ij}=\langle d_j^\dagger d_i\rangle`$, the block evolution is

```math
\dot M=-i[h,M]-\{D,M\}/2+G,\qquad 0\preceq M\preceq I.
```

The quadratic Hamiltonian is a particle-number-preserving form in this Nambu block, up to a constant. The covariance equation follows from the canonical anticommutation relations or from the standard [quasi-free covariance equation](https://arxiv.org/abs/2112.08344). Translation invariance permits correlations only within these momentum pairs and the two self-conjugate modes. A translation-invariant Gaussian state is a tensor product across these blocks in a fixed fermionic ordering. This includes the Gaussian states with fixed occupation on any one block. The orbit of an initial translation-invariant mixed Gaussian state stays Gaussian and translation-invariant. Cesàro average its covariances and take an accumulation point. The covariance stays in the closed physical set, and the affine equation makes the accumulation point stationary because the time-endpoint difference divided by the averaging time vanishes. The Gaussian state with this covariance is stationary. Thus its overlap $`F`$ is at least $`f`$ under an all-input time guarantee and under the unique-stationary-state hypothesis of the spatial corollary.

At a stationary block, diagonalize $`M`$ with eigenvalues $`m_i`$. The coherent commutator has zero diagonal, and $`G_{ii}=m_iD_{ii}`$. Positivity of $`G`$ gives $`|G_{ij}|\le\sqrt{G_{ii}G_{jj}}`$, and Cauchy–Schwarz yields for any vector $`v`$,

```math
v^\dagger Gv\le(\sum_i|v_i|\sqrt{m_i D_{ii}})^2\le(v^\dagger Mv)\mathrm{Tr}D.
```

The same argument with $`I-M`$ and $`B`$ gives $`B\preceq(\mathrm{Tr}D)(I-M)`$. Set

```math
\begin{aligned}
a(k)&=G_{11}+B_{22}=\sum_\mu (|v_\mu(k)|^2+|v_\mu(-k)|^2),\\
b(k)&=B_{11}+G_{22}=\sum_\mu (|u_\mu(k)|^2+|u_\mu(-k)|^2).
\end{aligned}
```

Both are nonnegative trigonometric polynomials of degree at most $`2R_J`$, with $`a+b=g=\mathrm{Tr}D`$. If the physical pair is filled, the target Nambu covariance is $`\mathrm{diag}(1,0)`$, so the wrong rate $`b`$ is at most $`g[(1-M_{11})+M_{22}]`$. If it is empty, the target is $`\mathrm{diag}(0,1)`$, and the wrong rate $`a`$ is at most $`g[M_{11}+(1-M_{22})]`$. Thus the scalar effective occupation $`a/g`$ has error at most the **sum** of wrong physical occupation probabilities in its pair. If $`F_{\mathcal B}`$ is stationary squared overlap on a pair $`\mathcal B`$, this sum is at most $`2(1-F_{\mathcal B})`$ because the target projector lies under either correct-occupation projector. On any distinct collection of pairs the aggregate scalar error is at most $`E=-2\log f`$, by $`F=\prod_{\mathcal B} F_{\mathcal B}`$. The scalar occupation is a bound on dissipative selectivity and has no claim to reproduce the true paired dynamics.

## 2. Pair parity is a physical time witness

Choose an odd Fock input in a single pair. The target has even physical parity in this pair. Its even projector $`\Pi_e`$ commutes with $`H`$ and with jumps in other pairs, while each jump in this pair reverses that pair's parity. For such a jump, $`L^\dagger\Pi_e L=L^\dagger L(I-\Pi_e)`$ and the anticommutator term is $`-L^\dagger L\Pi_e`$. It follows that $`\dot p_e\le g(k)(1-p_e)`$, because each linear jump in this frame is either a pure Nambu gain or loss and its squared operator norm is its squared coefficient norm. Starting at $`p_e(0)=0`$ gives $`p_e(t)\le1-e^{-g(k)t}`$. The target projector is dominated by $`\Pi_e`$, so the all-input guarantee requires

```math
g(k)\,t\ge\chi_f=-\log(1-f)
```

for every distinct pair. This uses an even observable directly on physical density matrices. If instead the stationary assumption is physical uniqueness, $`g(k)=0`$ would conserve $`\Pi_e`$ exactly and yield distinct stationary density matrices by averaging the evolutions of inputs in the two pair-parity sectors. So $`g(k)>0`$ on all pairs in that case too. Starting all distinct pairs in odd Fock states gives a translation-invariant Gaussian input with factorized evolution on the pairs. Its whole-state overlap is bounded by $`(1-e^{-\Gamma t})^{N/2-1}`$, proving $`\Gamma t=\Omega_f(\log N)`$ at any radius.

## 3. Taylor approximation near the Fermi crossing

Assume $`S=N/(R_J+1)`$ is sufficiently large. For either real rate polynomial $`p=a,b`$, trigonometric Bernstein gives $`\sup_k|p'(k)|\le2R_J\sup_k|p(k)|`$ on the circle. A maximum is within $`\pi/N`$ of a sampled point, so $`\sup_k|p(k)|\le2\Gamma`$. Iteration bounds derivative order $`j`$ by $`2\Gamma(2R_J)^j`$. In $`q=k-\pi/2`$, on the real window $`|q|\le\sqrt S/N`$, the order-$`m`$ Taylor polynomials $`T_a,T_b`$ have uniform error at most

```math
\eta=2\Gamma(2/\sqrt S)^{m+1}\le2\Gamma S^{-(m+1)/3}\qquad(S\ge64).
```

Put $`A=T_a+2\eta`$, $`B=T_b+2\eta`$. Each is strictly positive in the window, has degree at most $`m`$, and differs from its physical rate by an amount in $`[\eta,3\eta]`$. At sampled points, $`|A/(A+B)-a/g|\le 6\eta/g\le 6\eta t/\chi_f`$. Choose $`m=\lfloor c_0(\log S)^2\rfloor`$ and assume, for contradiction, $`\log(1+\Gamma t)\le(c_0/12)(\log S)^3`$. The occupation error added by the approximation is then $`o_f(\delta)`$ for $`\delta=S^{-1/8}`$.

Use $`q_j=(2j+1)\pi/N`$ with $`j`$ from $`j_0=\lceil S^{1/4}\rceil`$ to $`j_1=\lfloor S^{1/2}/(8\pi)\rfloor`$. Both physical momenta $`\pi/2\pm q_j`$ and their immediate neighbors lie within the window for sufficiently large $`S`$. The negative side is occupied, the positive side empty. Both windows lie in the positive half of the Brillouin zone, so the selected momenta represent distinct physical pairs. The weights $`w_j=\log(q_{j+1}/q_j)`$ decrease, the largest is $`O(S^{-1/4})`$, and their sum is $`(1/4+o(1))\log S`$. Discard nodes with either physical effective error exceeding $`\delta`$, at most $`E/\delta`$ nodes. At each retained node the approximating odds $`A/B`$ have signed log contrast at least $`2\log[(1-2\delta)/(2\delta)]\ge(1/8)\log S`$ for large $`S`$.

For any root $`z`$ of either approximant, its contribution to the absolute contrast at $`q>0`$ is bounded by $`h_z(q)=|\log|(q+z)/(q-z)||`$. Remove at most two grid nodes bracketing $`|z|`$ for each root. The remaining logarithmic weighted sum of $`h_z`$ is at most $`\pi^2/2`$. Indeed $`h_z`$ is increasing up to $`|z|`$ and decreasing afterwards. Bound the sum on increasing cells by integrating to the right and on decreasing cells by integrating to the left, using decreasing weights. The cells are disjoint after bracketing deletion, and $`h_z(e^y)\le\log\coth(|y-\log|z||/2)`$ integrates to $`\pi^2/2`$ on the real log axis. A zero root contributes zero. This is the [Reservoir Locality discrete root-deletion argument](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/blob/293b8e6914d8ff85ed3605d6c85dc95abfef4b61/science/range_lower_bound.md#lemma-2-discrete-root-budget-after-at-most-two-deletions) on an angular grid, whose logarithmic weights obey the same properties.

These root deletions cost at most $`4m`$ further nodes. All deletions together cost $`O((m+E/\delta)S^{-1/4})=o(1)`$ in weight. Factoring $`A,B`$, their leading coefficients cancel in the contrast. The retained contrast therefore contributes at least $`(\log S)^2/64`$ and at most $`(2m)\pi^2/2`$. Take $`c_0=1/(256\pi^2)`$ to contradict by a strict margin. All constants may be fixed before the large-$`S`$ limit, with the size threshold allowed to depend on $`f`$.

## 4. Matching constructions

The [compact filter](construction.md) uses $`H=0`$ and separate gain/loss, so it is admissible. A constant rescaling adjusts the per-momentum cap to the pair cap. Its analytic whole-register upper bound supplies the stated tight time order whenever its radius fits. At full radius, Fourier-transform the amplitude masks $`\sqrt{\Gamma/2}\,1_{\{\cos k>0\}}`$ for gain and $`\sqrt{\Gamma/2}\,1_{\{\cos k<0\}}`$ for loss back to real space. Each has support on the full ring, the pair cap holds, and the separate gain/loss population formula gives exact worst-input squared overlap $`(1-e^{-\Gamma t/2})^N`$.

## Attribution

[Reservoir Locality](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality) supplies the discrete root-deletion method and the compact filters. The [earlier gain/loss converse](time_converse.md) gives explicit finite-size constants under a per-momentum occupation-rate cap and uses a weighted root estimate. Here the stationary Gram inequality reduces pairing to scalar dissipative rates, pair parity gives a finite-time witness, and the short Taylor window yields the larger range converse. The [related-work account](../references/RELATED_WORK.md) compares the models and attribution. The [two-mode diagnostic](../verification/paired_reservoirs.py) checks the covariance and parity conventions against Fock-space evolution.
