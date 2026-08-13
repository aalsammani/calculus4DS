# Appendix B · Formula Sheet

One page per part; the formulas the course expects at your fingertips, with chapter references.

## Differential calculus (Chs. 3–6)

**Definition.** $f'(x) = \lim_{h\to0}\dfrac{f(x+h) - f(x)}{h}$.

**Rules.** $(cf)' = cf'$; $(f+g)' = f' + g'$; product $(fg)' = f'g + fg'$; quotient $\left(\frac fg\right)' = \frac{f'g - fg'}{g^2}$; chain $\frac{d}{dx}f(g(x)) = f'(g(x))\,g'(x)$.

**Catalog.**

$$
\frac{d}{dx}x^n = nx^{n-1}, \quad
\frac{d}{dx}e^x = e^x, \quad
\frac{d}{dx}\ln x = \frac1x, \quad
\frac{d}{dx}\sin x = \cos x, \quad
\frac{d}{dx}\cos x = -\sin x,
$$

$$
\frac{d}{dx}\tan x = \sec^2 x, \quad
\frac{d}{dx}\arctan x = \frac{1}{1+x^2}, \quad
\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}, \quad
\frac{d}{dx}a^x = a^x\ln a.
$$

**Linearization.** $L(x) = f(a) + f'(a)(x-a)$. **Newton.** $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$.

## Integral calculus (Chs. 7–11)

**FTC.** $\displaystyle\int_a^b f(x)\,dx = F(b) - F(a)$ where $F' = f$; $\ \dfrac{d}{dx}\displaystyle\int_a^x f(t)\,dt = f(x)$.

**Catalog.** $\displaystyle\int x^n dx = \frac{x^{n+1}}{n+1}\ (n \ne -1)$; $\displaystyle\int\frac{dx}{x} = \ln|x|$; $\displaystyle\int e^x dx = e^x$; $\displaystyle\int \sin = -\cos$; $\displaystyle\int\cos = \sin$; $\displaystyle\int\frac{dx}{1+x^2} = \arctan x$ (constants $+C$ throughout).

**Techniques.** Substitution: $\displaystyle\int f(g(x))g'(x)\,dx = \int f(u)\,du$. Parts: $\displaystyle\int u\,dv = uv - \int v\,du$. Trig substitution: $\sqrt{a^2 - x^2}\to x = a\sin\theta$; $\sqrt{a^2 + x^2}\to x = a\tan\theta$.

**Applications.** Area between curves $\int(\text{top} - \text{bottom})$; disks $V = \pi\int R(x)^2dx$; shells $V = 2\pi\int x\,h(x)\,dx$; average $\frac{1}{b-a}\int_a^b f$.

**Numerics.** Trapezoid error $O(n^{-2})$; Simpson $O(n^{-4})$.

## Series (Chs. 12–14)

Geometric: $\sum_{k=0}^\infty ar^k = \frac{a}{1-r}$ for $|r| < 1$. Divergence test: terms must $\to 0$. Ratio test: $\lim|a_{k+1}/a_k| < 1$ converges. Alternating error ≤ first omitted term.

**Taylor at $a$:** $\displaystyle\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k$. Standards (at 0): $e^x = \sum\frac{x^k}{k!}$; $\sin x = \sum(-1)^k\frac{x^{2k+1}}{(2k+1)!}$; $\cos x = \sum(-1)^k\frac{x^{2k}}{(2k)!}$; $\frac{1}{1-x} = \sum x^k$; $\ln(1+x) = \sum(-1)^{k+1}\frac{x^k}{k}$.

**Fourier on $[-\pi,\pi]$:** $f \sim \frac{a_0}2 + \sum(a_k\cos kx + b_k\sin kx)$, $\ a_k = \frac1\pi\int f\cos kx$, $b_k = \frac1\pi\int f\sin kx$.

## Linear algebra (Chs. 15–20)

$\|\vb v\| = \sqrt{\sum v_i^2}$; $\ \vb u\cdot\vb v = \sum u_iv_i = \|\vb u\|\|\vb v\|\cos\theta$; $\ \operatorname{proj}_{\vb a}\vb b = \frac{\vb a\cdot\vb b}{\vb a\cdot\vb a}\vb a$; $\ \|\vb u\times\vb v\| = \|\vb u\|\|\vb v\|\sin\theta$ (area), direction right-hand rule.

$(\mathit{AB})_{ik} = \sum_j a_{ij}b_{jk}$; $(\mathit{AB})^{\mathsf T} = \mathit B^{\mathsf T}\mathit A^{\mathsf T}$; $(\mathit{AB})^{-1} = \mathit B^{-1}\mathit A^{-1}$.

$\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$; $\ \det(\mathit{AB}) = \det\mathit A\det\mathit B$; $\det(c\mathit A) = c^n\det\mathit A$; triangular det = diagonal product; $\det = 0 \iff$ singular.

Eigen: $\mathit A\vb v = \lambda\vb v$; $\ \det(\mathit A - \lambda\mathit I) = 0$; $\ \sum\lambda_i = \operatorname{tr}\mathit A$, $\prod\lambda_i = \det\mathit A$; $\ \mathit A = \mathit P\mathit D\mathit P^{-1}\Rightarrow\mathit A^k = \mathit P\mathit D^k\mathit P^{-1}$; symmetric $\Rightarrow$ real $\lambda$, orthogonal eigenvectors.

## Multivariable (Chs. 21–25)

$\vb r'(t)$ componentwise; speed $\|\vb r'\|$; arc length $\int\|\vb r'\|dt$.

$\nabla f = \langle f_x, f_y\rangle$; $\ D_{\vb u}f = \nabla f\cdot\vb u$ (unit $\vb u$); steepest ascent along $\nabla f$ at rate $\|\nabla f\|$; $\nabla f \perp$ level sets. Tangent plane $L = f + f_x\Delta x + f_y\Delta y$. Chain rule $\frac{dz}{dt} = f_x x' + f_y y'$.

Critical: $\nabla f = \vb 0$; Hessian eigenvalues $+{+}$ min, $-{-}$ max, mixed saddle. Gradient descent $\vb x \leftarrow \vb x - \eta\nabla f$; factors $1 - \eta\lambda_i$.

Fubini: $\iint_R f\,dA = \int\!\!\int f\,dy\,dx$ (inner limits may depend on outer variable). Polar: $x = r\cos\theta$, $y = r\sin\theta$, $dA = r\,dr\,d\theta$; polar area $\frac12\int r(\theta)^2d\theta$; $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}dx = \sqrt\pi$.
