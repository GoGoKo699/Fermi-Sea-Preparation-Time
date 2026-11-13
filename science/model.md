# Model and temporal preparation theorem

The task is to prepare an entire critical Fermi sea using one time-independent, translation-invariant Gaussian reservoir. The spatially economical reservoir class can stabilize an accurate stationary state, but the time required to reach that state is a separate resource.

## Register, target and physical inputs

There are $`N=4M+2`$ spinless fermion modes on a periodic ring, with

```math
c_k=N^{-1/2}\sum_{x\in\mathbb Z_N}e^{-ikx}c_x,
\qquad
K_N=\{2\pi m/N:m\in\mathbb Z_N\}.
```

The target $`|\mathrm{FS}_N\rangle`$ occupies exactly the modes with $`\cos k>0`$. It is the unique ground state of the nearest-neighbor hopping Hamiltonian

```math
H_{\mathrm{tar}}=-\sum_x(c_x^\dagger c_{x+1}+c_{x+1}^\dagger c_x).
```

The size convention avoids sampled Fermi points. Physical density matrices commute with total fermion parity; projectors onto odd-particle vectors are included. In particular, both the target and its complementary Fock state are physical. Initial states need not be Gaussian, pure or occupation diagonal.

## Allowed autonomous generators

The dynamics is

```math
\mathcal L(\rho)=-i[H,\rho]
+\sum_{\mu,x}\mathcal D[L^-_{\mu,x}](\rho)
+\sum_{\nu,x}\mathcal D[L^+_{\nu,x}](\rho),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\},
```

with separate loss and gain families

```math
L^-_{\mu,x}=\sum_{r=-R}^{R}u_{\mu,r}c_{x+r},
\qquad
L^+_{\nu,x}=\sum_{r=-R}^{R}v_{\nu,r}c_{x+r}^\dagger.
```

There may be any finite number of families and arbitrary size-dependent coefficients. The radius $`R`$ counts actual jump support before periodization. The Hamiltonian is any translation-invariant, number-conserving quadratic Hamiltonian. It is diagonal in the momentum occupations, so neither its coefficients nor its range can improve this task's occupation dynamics. Imposing a common range bound on the Hamiltonian as well leaves the theorem valid.

No additional persistent modes, time dependence, intermediate controls, measurements, feedback, nonlinear jumps or pairing Hamiltonians are allowed. A jump containing both creation and annihilation terms is outside this separate gain/loss class.

Fourier mixing of the translated jump labels gives nonnegative rates

```math
a(k)=\sum_\nu|v_\nu(k)|^2,
\qquad b(k)=\sum_\mu|u_\mu(k)|^2,
\qquad g(k)=a(k)+b(k),
```

where each amplitude is a Laurent polynomial of radius at most $`R`$. The finite-ring rate budget is

```math
\max_{k\in K_N}g(k)\le\Gamma,
\qquad \Gamma>0.
```

This is an effective occupation-rate normalization, rather than a microscopic bath or laboratory cost model. All elapsed evolution is charged to $`t`$. The number of jump families, ideal coefficient specification, bath synthesis and implementation complexity are not optimized. No computational quantum advantage is claimed.

## Complete-register score

For a fixed target overlap $`f\in(0,1)`$, define

```math
F_{\min}(t)=\inf_{\rho\ \mathrm{physical}}
\langle\mathrm{FS}_N|e^{t\mathcal L}(\rho)|\mathrm{FS}_N\rangle,
\qquad
t_{\mathrm{worst}}(f)=\inf\{t\ge0:F_{\min}(t)\ge f\}.
```

For a fixed rate budget $`\Gamma`$, let $`\mathfrak G(N,R_{\max},\Gamma)`$ be the allowed generators with jump radius at most $`R_{\max}`$. Define the optimized budgeted time by

```math
T_{\mathrm{opt}}(N,R_{\max},f)
=\inf_{\mathcal L\in\mathfrak G(N,R_{\max},\Gamma)}
 t^{\mathcal L}_{\mathrm{worst}}(f),
\qquad \inf\varnothing=+\infty.
```

The notation suppresses $`\Gamma`$, which is held fixed in this infimum. The infimum includes generators with infinite preparation time; an empty feasible set or absence of any successful generator gives $`T_{\mathrm{opt}}=+\infty`$.

This is squared pure-target fidelity at one common output time. It concerns the entire register, rather than energy density or a selected few-body observable. If the displayed set is empty, the preparation time is infinite.

The occupation algebra is a product of classical two-state gain/loss chains. When every $`g(k)>0`$, put

```math
n_\infty(k)=\frac{a(k)}{g(k)},\qquad
 e(k)=\begin{cases}1-n_\infty(k),&\cos k>0,\\n_\infty(k),&\cos k<0,\end{cases}
\qquad F_\infty=\prod_k(1-e(k)).
```

To see why the occupation algebra closes, let $`F(n)`$ be any function of the commuting occupation projectors. The canonical anticommutation relations give

```math
\begin{aligned}
\mathcal D[c_k]^\dagger F(n)
&=n_k\left[F(n^{k\leftarrow0})-F(n)\right],\\
\mathcal D[c_k^\dagger]^\dagger F(n)
&=(1-n_k)\left[F(n^{k\leftarrow1})-F(n)\right].
\end{aligned}
```

Here $`n^{k\leftarrow b}`$ replaces the $`k`$th argument by $`b`$. The fermionic signs cancel between each jump and its adjoint, and the Hamiltonian commutes with every such $`F(n)`$. The restricted Heisenberg generator is therefore the sum of independent two-state generators. In particular, the evolved target projector remains in this diagonal algebra, so its expectation depends only on initial Fock-basis populations even for a non-Gaussian state with coherences.

For one mode, its correct-bit probability starting in the wrong bit is $`(1-e(k))(1-e^{-g(k)t})`$. Starting in the correct bit adds $`e^{-g(k)t}`$ to that probability. The diagonal transition kernel is the product of these two-state kernels, so every factor is minimized by the wrong initial bit.

The exact all-input curve is

```math
\boxed{
F_{\min}(t)=F_\infty\prod_{k\in K_N}(1-e^{-g(k)t}).
}
```

The complementary Fock state attains the infimum. Arbitrary coherences cannot lower it: the Heisenberg-evolved target projector is diagonal in the Fock basis, with its smallest eigenvalue at that state. If some rate is zero, a wrong occupation is never removed and $`F_{\min}(t)=0`$ at every finite time.

Consequently, a finite-time guarantee $`F_{\min}(t)\ge f`$ already implies

```math
F_\infty\ge f,\qquad
\sum_k e(k)\le E_f:=-\log f.
```

No separate high-fidelity stationary-state premise is needed in the converse. All logarithms in the scientific account are natural.

## Main result

For every fixed $`f\in(0,1)`$, there are positive constants $`c,C`$ and a size threshold depending on $`f`$ such that every allowed device attaining $`F_{\min}(t)\ge f`$ obeys

```math
\boxed{
\log(1+\Gamma t)+C R\ge c(\log N)^3.
}
```

The [explicit finite-size inequality](time_converse.md#finite-size-theorem) specifies all constants through elementary finite-grid quantities and $`\zeta(3)`$. In particular, for every fixed $`K`$, any sequence of successful devices with $`R\le K(\log N)^2`$ satisfies

```math
\liminf_{N\to\infty}
\frac{\log(\Gamma t)}{(\log N)^3}
\ge\frac{4}{27\pi^2}.
```

The coefficient is unoptimized. It is not claimed to be the optimal leading constant.

The previously established geometric-root gain/loss construction has radius $`O((\log N)^2)`$ and achieves fixed complete-register overlap in time with $`\log(\Gamma t)=O((\log N)^3)`$. Crediting that construction gives the matching order

```math
\boxed{
 t=\Gamma^{-1}\exp[\Theta((\log N)^3)]
 \quad\text{at the spatially optimal order }R=\Theta((\log N)^2).
}
```

Precisely, the lower bound holds for every fixed radius coefficient; an attaining construction exists for a sufficiently large fixed coefficient. This does not assert existence at every prescribed coefficient.

More generally, if a radius budget $`\mathcal R_N`$ is at least a sufficiently large constant times $`(\log N)^2`$ and satisfies $`\mathcal R_N=o((\log N)^3)`$, the optimized time satisfies $`\log(1+\Gamma T_{\mathrm{opt}}(N,\mathcal R_N,f))=\Theta((\log N)^3)`$. Increasing the allowed radius anywhere inside this window does not remove the leading cubic-logarithmic time order.

A second consequence is that polynomial preparation time requires $`R=\Omega((\log N)^3)`$. No matching polynomial-time construction at that radius is asserted. The result separates stationary feasibility from preparation time; it does not determine the complete time-versus-radius frontier.

## Proof route and attribution

The [weighted root budget](root_budget.md) turns the aggregate stationary error into a cubic-logarithmic root cost. The [time converse](time_converse.md) uses polynomial growth and Jensen's formula to turn that cost into a small physical damping rate, then applies the exact all-input curve.

The rational-filter representation, unweighted root-deletion method, spatial threshold and geometric-root upper construction are inherited from [Fermi-Sea Reservoir Locality, pinned scientific source](https://github.com/GoGoKo699/Fermi-Sea-Reservoir-Locality/tree/293b8e6914d8ff85ed3605d6c85dc95abfef4b61). The added conclusion is a temporal converse optimized over all reservoirs in the present separate gain/loss class. It is narrower than that source's full Gaussian spatial converse, which permits pairing when coherent range is charged.
