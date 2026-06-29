#!/usr/bin/env python3
"""This script plots partial sums for n=1,3,5,10 against the target function
and shows the L2 error as a function of n.
"""

#%%
import argparse
import numpy as np
import matplotlib.pyplot as plt

#%% Define the target functions and their partial sums for Fourier series approximations.
def square_target(x: np.ndarray) -> np.ndarray:
    """Periodic square wave on (-pi, pi]: 1 on (0,pi], -1 on (-pi,0]."""
    x_mod = ((x + np.pi) % (2 * np.pi)) - np.pi
    return np.where(x_mod >= 0, 1.0, -1.0)


def partial_sum_square(x: np.ndarray, n_terms: int) -> np.ndarray:
    """Compute the nth partial sum (n_terms terms) of the square-wave series.

    The series uses the odd harmonics: 4/pi * sum_{k=1..n_terms} sin((2k-1)x)/(2k-1)
    """
    s = np.zeros_like(x, dtype=float)
    for k in range(1, max(0, int(n_terms)) + 1):
        m = 2 * k - 1
        s += (4.0 / np.pi) * np.sin(m * x) / m
    return s


def saw_target(x: np.ndarray) -> np.ndarray:
    """Standard sawtooth wave on (-pi, pi]."""
    x_mod = ((x + np.pi) % (2 * np.pi)) - np.pi
    return x_mod


def partial_sum_saw(x: np.ndarray, n_terms: int) -> np.ndarray:
    """Compute the nth partial sum of the sawtooth-wave Fourier series."""
    s = np.zeros_like(x, dtype=float)
    for k in range(1, max(0, int(n_terms)) + 1):
        s += 2.0 * ((-1) ** (k + 1)) * np.sin(k * x) / k
    return s

#%% Define a function to compute the L2 error between the target function and the partial sum approximation.
def l2_error(f_target, s_func, x: np.ndarray, n: int) -> float:
    """Return L2 error (root of integral of squared error) on grid x."""
    diff = s_func(x, n) - f_target(x)
    return float(np.sqrt(np.trapezoid(diff ** 2, x)))


def plot_partial_sums(wave: str = "square") -> None:
    x = np.linspace(-np.pi, np.pi, 2001)

    if wave == "square":
        f_target = square_target
        s_func = partial_sum_square
    else:
        f_target = saw_target
        s_func = partial_sum_saw

#%% Plot the target function and the partial sums for n=1,3,5,10.
    plt.figure(figsize=(9, 4))
    plt.plot(x, f_target(x), color="k", lw=2, label="target")
    for n in [1, 3, 5, 10]:
        s = s_func(x, n)
        plt.plot(x, s, label=f"n={n}")
    plt.xlim(-np.pi, np.pi)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"{wave.capitalize()} wave: partial sums vs target")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"week2/{wave}_partial_sums.png", dpi=150, bbox_inches="tight")

#%% Compute and plot the L2 error as a function of n.
    max_n = 100
    ns = np.arange(1, max_n + 1)
    errors = np.array([l2_error(f_target, s_func, x, int(n)) for n in ns])

    plt.figure(figsize=(7, 4))
    plt.plot(ns, errors, marker=".")
    plt.xlabel("n (number of terms)")
    plt.ylabel("L2 error")
    plt.title(f"L2 error between partial sum and target ({wave})")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"week2/{wave}_l2_error.png", dpi=150, bbox_inches="tight")
    print(f"\nPlots saved:")
    print(f"  - week2/{wave}_partial_sums.png")
    print(f"  - week2/{wave}_l2_error.png")

#%% Main function to parse command-line arguments and call the plotting function.
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave", choices=["square", "saw"], default="square",
                        help="Choose target waveform (square or saw)")
    args = parser.parse_args()
    plot_partial_sums(args.wave)

#%% Run the main function when the script is executed.
if __name__ == "__main__":
    main()



# %%
