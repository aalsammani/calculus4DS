# Appendix D · Answers to Selected Exercises

How to use the book's answer infrastructure: **every chapter** answers all of its Quick Checks in a collapsible dropdown immediately below them, and provides at least one fully worked solution per exercise set inline. This appendix supplements those with **final answers** to a further selection of Basic and Intermediate exercises — enough to confirm your work, not enough to replace it. All numerical values below were verified computationally during the book's construction. (Where an exercise asks for a derivation, plot, or explanation, no short answer can be meaningful and none is listed.)

## Part 0 — Foundations

**Ch. 1.** Domain of $\sqrt{x-4}$: $[4,\infty)$. Composition order matters: $f(g(x)) \ne g(f(x))$ in general — test with $f = x^2$, $g = x+1$.

**Ch. 2.** $135° = \frac{3\pi}{4}$; $\ \frac\pi5 = 36°$. $\log$ laws convert products to sums only; $\ln(a+b)$ has no expansion. Every exponential with base $> 1$ eventually beats every fixed power of $x$.

## Part I — Differential Calculus

**Ch. 3.** QC4-style limit: $\lim_{h\to0}\frac{(2+h)^2-4}{h} = 4 = f'(2)$ for $f = x^2$.

**Ch. 4.** With $f(2) = 3, f'(2) = -1, g(2) = 5, g'(2) = 4$: $(fg)'(2) = 7$, $\left(\frac fg\right)'(2) = -\frac{17}{25}$.

**Ch. 5.** $\frac{d}{dx}\ln 2x = \frac1x$; $\ \frac{d}{dx}\cos^3 x = -3\cos^2x\sin x$; $\ \frac{d}{dx}3^x = 3^x\ln3$.

**Ch. 6.** $L(x) = 8 + 12(x-2)$ for $x^3$ at $2$. Newton on $x^2 - 9$ from $x_0 = 4$: $x_1 = 3.125$.

## Part II — Integral Calculus

**Ch. 7.** $\int_1^3 2x\,dx = 8$; $\ \frac{d}{dx}\int_0^x e^{-t^2}dt = e^{-x^2}$.

**Ch. 8.** $\int(2x+7)^{10}dx = \frac{(2x+7)^{11}}{22}+C$; definite substitutions transform the limits.

**Ch. 9.** Area between $y = 4 - x^2$ and $y = x + 2$: $\frac92$. Disk check: cylinder $45\pi$.

**Ch. 10.** $\int x\cos x\,dx = x\sin x + \cos x + C$; $\ \int_1^e\ln x\,dx = 1$.

**Ch. 11.** Trapezoid error drops $4\times$ per doubling; Simpson is exact on cubics.

## Part III — Series

**Ch. 12.** $\sum_{k=0}^\infty(\tfrac34)^k = 4$ — geometric with $|r| < 1$. Harmonic partial sums: $H_{10} = 2.9290$, $H_{100} = 5.1874$, $H_{200} = 5.8780$ vs. $\ln 200 + \gamma = 5.8755$.

**Ch. 13.** $T_2$ of $e^x$: $1 + x + \frac{x^2}2$, giving $e^{0.1}\approx1.105$ (true $1.10517$). $\lim_{x\to0}\frac{1-\cos x}{x^2} = \frac12$. $|e - T_7(1)| = 2.73\times10^{-6}$, just under the next-term scale $\frac{1}{9!} = 2.756\times10^{-6}$ — tail estimates are sharp.

**Ch. 14.** Sawtooth $b_k = \frac{2(-1)^{k+1}}{k}$; parabola $a_k = \frac{4(-1)^k}{k^2}$; square wave $b_k = \frac{2(1-(-1)^k)}{\pi k}$. Basel payoff: $\sum\frac1{k^2} = \frac{\pi^2}6$; Parseval on $x^2$: $\sum\frac1{k^4} = \frac{\pi^4}{90}$. Gibbs overshoot at 100 terms: $1.17899$ (theory $1.17898$).

## Part IV — Linear Algebra

**Ch. 15.** Ex. 5: $\vb a + \vb b = \langle4,2,2\rangle$; $\|\vb a\| = 3$; $\|\vb b\| = 5$; $\hat{\vb a} = \frac13\langle1,2,-2\rangle$. Ex. 8: total $\langle20,55\rangle$, magnitude $\approx 58.5$ km. Ex. 11: (a) parallel ($c = -\frac32$); (b) not.

**Ch. 16.** Ex. 5: $\vb u\cdot\vb v = -5$; $\theta \approx 109.5°$; $\operatorname{proj}_{\vb v}\vb u = \langle-0.6,-0.8,0\rangle$; $\vb u\times\vb v = \langle-8,6,10\rangle$. Ex. 7: $\langle1,2,3\rangle\times\langle2,0,1\rangle = \langle2,5,-4\rangle$; area $\sqrt{45} = 3\sqrt5 \approx 6.708$. Ex. 22: $m = \frac{\vb x\cdot\vb y}{\vb x\cdot\vb x} = \frac{19}{14} \approx 1.357$.

**Ch. 17.** Ex. 5: $\mathit A\vb v = \langle-1,4\rangle$; $\mathit{AB}$ is $2\times2$, $\mathit{BA}$ is $3\times3$. Ex. 12: $\vb x_1 = \langle0.9,0.1\rangle$, $\vb x_2 = \langle0.83,0.17\rangle$, limit $\langle\frac23,\frac13\rangle$.

**Ch. 18.** Ex. 5: (a) $(2,3)$; (b) $(1,2,1)$. Ex. 8: unique iff $k\ne4$; infinitely many at $k = 4$. Ex. 10: parabola $y = 3 - 2x + x^2$ i.e. $(a,b,c) = (3,-2,1)$. Ex. 22: Leontief output $\vb x = (210,\ 226.67)$.

**Ch. 19.** Ex. 5: (a) $9$; (b) $0$ (dependent rows); (c) $-9$. Ex. 7: singular at $t = \pm2$. Ex. 8: area $5$. Ex. 10: $\det\mathit B = -12$.

**Ch. 20.** Ex. 5: (a) $\lambda = 4,2$, vectors $\langle1,1\rangle,\langle1,-1\rangle$; (b) $\lambda = 2,5$; (c) $\lambda = 0,5$; (d) no real eigenvalues (rotation by $90°$). Ex. 10: $\lambda = 1, 0.3$; steady state $\langle\frac47,\frac37\rangle$; transient below $1\%$ after $k = 4$ months ($0.3^{3.82} = 0.01$). Ex. 8/21: Fibonacci eigenvalues $\varphi \approx 1.618$, $\psi\approx-0.618$; $F_{10} = 55$. Ex. 22: Laplacian eigenvalues $2-\sqrt2,\ 2,\ 2+\sqrt2$.

## Part V — Multivariable Calculus

**Ch. 21.** Ex. 5: speed $\sqrt{13}$, length $2\pi\sqrt{13}$. Ex. 6: tangent line $\langle1+2s,\ 1+3s\rangle$. Ex. 9: $45°$ is optimal; the $50°$ launch's $40.20$ m trails the optimal $\frac{v_0^2}{g} = 40.82$ m. Ex. 11: one arch has length $8$. Ex. 22: catenary arc length $\sinh 1 \approx 1.1752$.

**Ch. 22.** Ex. 7: $L(1.05,1.9) = 7.1$ vs. exact $7.0875$. Ex. 13: limit along $y = mx$ is $\frac{m}{1+m^2}$ — path-dependent, no limit; yet $f_x(0,0) = f_y(0,0) = 0$. Ex. 21: fitted line $y = x + \frac56$. Ex. 23: Newton iterates $(2,1)\to(2, 0.5)\to(1.9333, 0.5167)$, residuals shrinking.

**Ch. 23.** Ex. 5: $\nabla f(2,0) = \langle 1, 2\rangle$ (from $f_x = e^y$, $f_y = xe^y + 2y$); max rate $\sqrt5$. Ex. 7: (a) min at $(2,-3)$; (b) $(1,1)$ is a local max, the other three critical points saddles; (c) $(0,0)$ saddle, $(\pm1,\pm1)$ (same signs) minima. Ex. 11: threshold $\eta < \frac15$; at $\eta = 0.15$ factors $-0.5$ and $0.7$. Ex. 12: max of $xy$ on the circle: $1$ at $\pm(1,1)$.

**Ch. 24.** Ex. 5: (a) $e - 2$; (b) $\frac\pi2$; (c) $\frac\pi2 - 2$. Ex. 6: volume $\frac{100}{3}$; average height $\frac{25}3$. Ex. 7: $\frac83$. Ex. 9: (a) $\frac{2\ln2}{3}$; (b) $2$. Ex. 11: normalization ✓; $P(X>Y) = \frac25$; independent — $6xy^2 = (2x)(3y^2)$ factors into the two marginals. Ex. 20: $\mathbb E|X-Y| = \frac13$.

**Ch. 25.** Ex. 5: (a) $\frac\pi2$; (b) $\pi(1 - e^{-4})$; (c) $\frac23$; (d) $4\pi$. Ex. 6: $\frac{8\pi}3$. Ex. 7: petal area $\frac\pi{12}$. Ex. 8: $\frac\pi4$. Ex. 10: $\bar r = \frac23$. Ex. 11: $\frac\pi4 + 2$. Ex. 12: $\bar y = \frac{4R}{3\pi}$. Ex. 13: $\sqrt{\pi/2}$. Ex. 21: $\int x^2e^{-x^2}dx = \frac{\sqrt\pi}2$; variance $1$.
