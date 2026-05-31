---
marp: true
theme: default
paginate: true
class: lead
---

# Solution of $m$ Linear Equations in $n$ Variables

#### Definitions and goals

We study systems of $m$ linear equations in $n$ variables with $m>1$ and $n>1$. Each equation has the form $a_{i1}x_1+\cdots+a_{in}x_n=b_i$ (for $i=1,\dots,m$), and a solution is any $n$-tuple $(x_1,\dots,x_n)$ that satisfies all equations.

---

## General form (display)

A typical equation in the system appears as the display equation below:

$$
a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n = b_i,
\qquad i = 1,2,\dots,m.
$$

This single display emphasizes the linear structure shared by all rows.

---

## Matrix notation

Writing the coefficient matrix $A=[a_{ij}]$, unknown vector $x$ and right-hand side $b$, we compress the whole system into the matrix equation

$$
Ax=b
$$

which captures all $m$ scalar equations at once.

---

## Example system

Consider this concrete example with $m=3$, $n=3$:

$$
\begin{aligned}
2x_1 - x_2 + 3x_3 &= 5, \\
x_1 + 4x_2 - x_3 &= -1, \\
-x_1 + 2x_2 + 2x_3 &= 3
\end{aligned}
$$

Or, as a short inline example: the first equation is $2x_1 - x_2 + 3x_3 = 5$.

---

## Cases and solution types

- If $m<n$ (underdetermined) there are typically infinitely many solutions (free parameters).
- If $m=n$ (square) there may be a unique solution, none, or infinitely many depending on $A$.
- If $m>n$ (overdetermined) the system can be inconsistent; consistency requires that all equations agree.

---

## Summary

- **Problem:** Find all $x\in\mathbb{R}^n$ with $Ax=b$.
- **Methods:** Gaussian elimination / row reduction on the augmented matrix $[A\mid b]$.
- **Outcomes:** unique solution, infinite family (parametrized), or no solution.

Questions or follow-up: run a worked Gaussian-elimination example or include geometric interpretation?
