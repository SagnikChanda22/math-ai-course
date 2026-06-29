"""
Simple scripts to sample and visualize different types of measures.
Run: python visualize_measures.py
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

RNG = np.random.default_rng()
OUTPUT_DIR = Path(__file__).with_name('images')
OUTPUT_DIR.mkdir(exist_ok=True)

def plot_hist(samples, title, filename, bins=50):
    plt.figure(figsize=(6,3))
    plt.hist(samples, bins=bins, density=True, alpha=0.7)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename)
    plt.close()

def sample_die(n=10000):
    # finite atomic probability
    faces = np.arange(1,7)
    return RNG.choice(faces, size=n)

def sample_uniform(n=10000):
    # Lebesgue-absolutely-continuous probability on [0,1]
    return RNG.random(n)

def sample_gaussian(n=10000):
    return RNG.normal(loc=0.0, scale=1.0, size=n)

def sample_dirac(n=10000, x0=0.0):
    # all mass at x0
    return np.full(n, x0)

def sample_cantor(n=10000, depth=20):
    # Random series method: sum of digits 0 or 2 scaled by 3^{-k}
    choices = RNG.integers(0,2,size=(n,depth)) * 2  # 0 or 2
    powers = 3 ** np.arange(1, depth+1)
    samples = (choices / powers).sum(axis=1)
    return samples

if __name__ == '__main__':
    n = 20000

    die = sample_die(n)
    plot_hist(die, 'Fair die (atomic discrete)', 'fair_die.png')

    u = sample_uniform(n)
    plot_hist(u, 'Uniform [0,1] (continuous)', 'uniform_0_1.png')

    g = sample_gaussian(n)
    plot_hist(g, 'Gaussian (continuous)', 'gaussian.png')

    d = sample_dirac(n, x0=0.0)
    plt.figure(figsize=(6,1))
    plt.plot(d[:200], np.zeros(200), '|')
    plt.title('Dirac at 0 (point mass) — shown as ticks')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'dirac.png')
    plt.close()

    c = sample_cantor(n, depth=12)
    plot_hist(c, 'Cantor-sample (singular) — empirical', 'cantor.png')

    print(f'Saved images to {OUTPUT_DIR.resolve()}')
