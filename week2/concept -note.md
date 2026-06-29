# Taylor Series
A Taylor series expresses a function as an infinite power series centered at a point. If a function $f$ is infinitely differentiable at $a$, its Taylor series around $a$ is:

$$
\displaystyle f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}\, (x-a)^n,
$$

where $f^{(n)}(a)$ denotes the $n$-th derivative of $f$ evaluated at $a$, and $n!$ is the factorial of $n$. When $a=0$, this becomes the Maclaurin series:

$$
\displaystyle f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}\, x^n.
$$

## Worked example: $f(x)=e^x$

For $f(x) = e^x$, all derivatives equal $e^x$. Evaluating at $x=0$ gives $f^{(n)}(0)=1$ for every $n$. Thus the Maclaurin series is:

$$
\displaystyle e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots.
$$

A third-degree Taylor polynomial approximation around $a=0$ is:

$$
\displaystyle T_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}.
$$

For example, at $x=0.5$:

$$
\displaystyle e^{0.5} \approx 1 + 0.5 + \frac{0.5^2}{2} + \frac{0.5^3}{6} = 1.645833\ldots
$$

The exact value is $e^{0.5} \approx 1.64872$, so the Taylor polynomial gives a close approximation.
