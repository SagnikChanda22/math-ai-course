## Solution of $m$ Linear Equations in $n$ Variables

When we study a system of $m$ linear equations in $n$ variables with $m>1$ and $n>1$, we are looking for all ordered $n$-tuples $\left(x_1, x_2, \dots, x_n\right)$ that satisfy each equation simultaneously. In general, a single equation in the system has the form

$$
a_{i1} x_1 + a_{i2} x_2 + \cdots + a_{in} x_n = b_i$$


for $i = 1, 2, \dots, m$. Here the coefficients $a_{ij}$ and constants $b_i$ are given numbers, and the unknowns are the variables $x_1, x_2, \dots, x_n$.

A solution of the entire system is any vector $x = (x_1, x_2, \ldots, x_n)$ such that each equation holds. For example, the system

$$\begin{aligned}
2 x_1 - x_2 + 3 x_3 &= 5, \\
x_1 + 4 x_2 - x_3 &= -1, \\
- x_1 + 2 x_2 + 2 x_3 &= 3
\end{aligned}
$$



is a concrete case with $m = 3$ and $n = 3$. In this case, any triple $(x_1, x_2, x_3)$ that satisfies all three equations is a solution. When the set of all such triples is nonempty, the system is called consistent; otherwise, it is inconsistent.

A more compact way to write the system uses matrix notation. If $A$ is the $m \times n$ coefficient matrix with entries $a_{ij}$, and if $b = (b_1, b_2, \ldots, b_m)^T$, then the system becomes the matrix equation

$$
A x = b.
$$

This single display equation captures all $m$ linear equations at once. The unknown vector $x$ is an $n$-dimensional column vector, and solving the system means finding $x$ so that the product $Ax$ equals $b$.

In many cases, we can encounter three different categories of solution behavior. If $m < n$, the system is underdetermined and often has infinitely many solutions. For example,

$$
x_1 + 2 x_2 - x_3 = 4, \qquad 3 x_1 - x_2 + 5 x_3 = 7
$$

has $m=2$ equations and $n=3$ variables. Because there are more variables than equations, one variable can usually be treated as free, giving a family of solutions rather than a single point.

If $m = n$, the system is square and may have a unique solution, no solutions, or infinitely many solutions depending on the structure of the coefficient matrix. When $m > n$, the system is overdetermined and may be inconsistent if the equations conflict. For example, the four equations

$$
\begin{aligned}
x_1 + x_2 &= 2, \\
2 x_1 - x_2 &= 1, \\
x_1 + 3 x_2 &= 5, \\
4 x_1 - x_2 &= 6
\end{aligned}
$$

must be satisfied by only two variables, so consistency is not guaranteed.

Solving such systems often uses row reduction or Gaussian elimination, where we transform the augmented matrix $[A|b]$ into a simpler form. The final solution may be a unique point, a parametric family of vectors, or there may be no solution at all. The general concept of a solution of $m$ linear equations in $n$ variables is fundamental in linear algebra, and it appears across engineering, physics, economics, and data science.
