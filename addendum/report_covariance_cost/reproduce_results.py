"""Reproduce all numerical results and Figure 1 of the report.

Run with: python3 reproduce_results.py
Requires: numpy, matplotlib
Tested with: Python 3.14.8, NumPy 2.5.4
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def simulate(N, T, trials=4000):
    """Monte Carlo mean of out-of-sample variance ratio for plug-in GMV
    portfolio, true Sigma = I, vs exact finite-sample formula."""
    rng = np.random.default_rng(0)
    nu = T - 1
    ratios = np.empty(trials)
    for i in range(trials):
        X = rng.standard_normal((T, N))
        X = X - X.mean(axis=0)
        Sinv = np.linalg.inv(X.T @ X)
        w = Sinv.sum(axis=1) / Sinv.sum()
        ratios[i] = N * (w @ w)  # w' Sigma w / V*, Sigma = I
    exact = 1 + (N - 1) / (nu - N)
    return ratios.mean(), exact


def main():
    print('B.1 Monte Carlo check of the risk-inflation formula')
    for N in [25, 50, 100, 200, 225]:
        m, ex = simulate(N, T=250)
        print(f'  N={N:3d} T=250 N/T={N/250:.2f}  MC mean={m:.3f}  '
              f'exact={ex:.3f}')

    print('\nB.2 Certainty-equivalent dollar calibration')
    sigma_star, gamma, W = 0.08, 2.0, 1e9
    for c in [0.5, 0.8, 0.9, 0.95]:
        vol = sigma_star / (1 - c) ** 0.5
        loss = (gamma / 2) * W * sigma_star ** 2 * c / (1 - c)
        print(f'  c={c}: vol {vol:.1%}, CE loss {loss/1e6:.1f}M/yr '
              f'({loss/W:.2%} of AUM)')

    # B.3 Figure
    c = np.linspace(0.01, 0.95, 400)
    asym = 1 / (1 - c)

    def exact_curve(T, c):
        nu = T - 1
        N = np.ceil(c * T)
        return 1 + (N - 1) / (nu - N)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

    ax = axes[0]
    ax.plot(c, asym, 'k--', lw=1.5, label=r'asymptotic $1/(1-c)$')
    ax.plot(c, exact_curve(250, c), lw=1.8, label=r'exact, $T=250$')
    ax.plot(c, exact_curve(2500, c), lw=1.8, label=r'exact, $T=2500$')
    for cv, m in [(0.5, 2), (0.8, 5), (0.9, 10)]:
        ax.plot(cv, m, 'o', color='crimson', ms=5, zorder=5)
        ax.annotate(f'{m:.0f}x', (cv, m), textcoords='offset points',
                    xytext=(6, -10), fontsize=9, color='crimson')
    ax.set_xlabel(r'aspect ratio $c = N/T$')
    ax.set_ylabel('variance multiplier (out-of-sample vs oracle)')
    ax.set_title('(a) Risk inflation of the sample-covariance GMV portfolio')
    ax.set_ylim(0.9, 12)
    ax.legend(frameon=False, fontsize=9)
    ax.grid(alpha=0.3)

    ax = axes[1]
    W_, sig, g = 1e9, 0.08, 2.0
    L = (g / 2) * W_ * sig ** 2 * c / (1 - c) / 1e6
    ax.plot(c, L, lw=1.8, color='steelblue')
    for cv in [0.5, 0.8, 0.9, 0.95]:
        lv = (g / 2) * W_ * sig ** 2 * cv / (1 - cv) / 1e6
        ax.plot(cv, lv, 'o', color='crimson', ms=5)
        ax.annotate(f'${lv:.1f}M', (cv, lv), textcoords='offset points',
                    xytext=(6, -4), fontsize=9, color='crimson')
    ax.set_xlabel(r'aspect ratio $c = N/T$')
    ax.set_ylabel('annual certainty-equivalent loss ($M, W=$1bn)')
    ax.set_title('(b) Welfare cost of the noise gamble '
                 '($\\gamma=2$, oracle vol 8%)')
    ax.set_ylim(0, 140)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig('figures/fig1.png', dpi=160, bbox_inches='tight')
    print('\nB.3 Figure written to figures/fig1.png')


if __name__ == '__main__':
    main()
