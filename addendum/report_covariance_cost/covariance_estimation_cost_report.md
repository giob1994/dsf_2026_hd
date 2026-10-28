---
title: "The cost of noise: covariance estimation error in Markowitz portfolio construction"
author: "GLM-5.3 (Perplexity Computer)"
date: "2026-10-28"
abstract: |
  Estimating return covariances becomes difficult when the investment universe
  approaches the length of its historical sample. Across three user prompts,
  this study assembled theoretical references, numerically checked a Gaussian
  minimum-variance benchmark, and translated excess risk into a monetary
  valuation. When the number of assets equals ninety percent of the
  observation count, the sample-based portfolio has approximately ten times
  the oracle variance. With equal expected returns, one billion dollars
  invested, eight percent oracle volatility, and mean-variance risk aversion
  of two, the unnecessary risk corresponds to an annual certainty-equivalent
  cost of 57.6 million dollars. A correctly specified structured estimator
  avoids this penalty in the benchmark. Covariance estimation can therefore
  carry substantial welfare costs, although these figures describe an
  unconstrained stylized model rather than predicted trading losses.
geometry: margin=2.5cm
fontsize: 11pt
colorlinks: true
linkcolor: RoyalBlue
urlcolor: RoyalBlue
---

# Introduction

Portfolio construction in the Markowitz tradition takes as inputs the expected
returns and the covariance matrix of asset returns, and outputs portfolio
weights that trade off return against risk. The covariance matrix is the
quantitative heart of the risk side of this trade-off, and estimating it
accurately is hard precisely when it matters most: modern applications involve
hundreds or thousands of assets ($N$) estimated from histories of comparable
length ($T$), so the aspect ratio $c = N/T$ is not small. The user's
objective was to assemble references and a simple, theoretically grounded
example communicating how expensive poor covariance estimation is in this
high-dimensional regime.

At the start of the session, no material had been collected: the request was
framed as a search for references and/or a worked example illustrating the
importance of the high-dimensional covariance estimation problem.

The gap motivating the interaction was twofold. First, the literature on
estimation error in portfolio optimization is vast, and spans practitioner
essays, empirical sensitivity studies, and rigorous random-matrix-theory
analyses; a nonspecialist needs a curated, verified entry point. Second, and
more importantly, the theoretical results in this literature are stated in
asymptotic statistical language; the user needed them translated into a
quantity a decision-maker cares about, namely a dollar cost. The specific
questions addressed were: (i) what is the cleanest analytical illustration of
the cost of estimating the covariance matrix poorly, (ii) what are the
canonical references, and (iii) what is the economic, ideally
dollar-denominated interpretation when $N$ and $T$ are both large with
$c$ close to 1?

This report contributes a self-contained answer to all three questions: an
exact finite-sample formula for the out-of-sample risk inflation of the
plug-in minimum-variance portfolio, presented and numerically checked rather
than derived; a curated and verified reference list [1-4]; and a
certainty-equivalent calibration translating the statistical inflation into an
annual welfare cost.

# Methods

## Interaction protocol

The session comprised 3 turns between the user and GLM-5.3 on 2026-10-28.
Prompts were interpreted as a progressive research task: first a request for
references and a simple example, then a request for economic interpretation and
dollar quantification, and finally a request to compile the findings into a
report. References were located by web search and verified against their
primary landing pages and abstracts; the analytical result was checked by an
independent Monte Carlo simulation in Python (NumPy), and the economic
calibration was verified arithmetically. All substantive claims were
additionally reviewed by a stronger reviewer model before delivery.

| Item | Detail |
|------|--------|
| Session ID | 52f9ef8c-b838-4b4b-8f42-e67918660437 |
| Model | GLM-5.3 (Perplexity Computer) |
| User | Anonymous (Perplexity Computer session) |
| Turns / prompts | 3 / 3 |
| Final status | Resolved |

## Prompt register

| # | Turn | Intent | Outcome |
|---|------|--------|---------|
| P1 | 1 | Find references and/or a simple example of the theoretical cost of poor covariance estimation for Markowitz portfolio construction | Delivered exact risk-inflation formula, Monte Carlo validation, and four verified references |
| P2 | 2 | Give the results an intuitive economic interpretation; quantify the hypothetical dollar cost of the plain sample covariance estimator versus a structured one when c is close to 1 | Delivered zero-alpha-gamble interpretation and certainty-equivalent dollar calibration |
| P3 | 3 | Compile the findings into a report using the provided template | This report |

Verbatim prompts are reproduced in Appendix A; prompt references below
(e.g. "P2") point to this register. Prompt timestamps were not recorded.

## Conversation summary

The session began with a request for references and a simple example of the
theoretical cost of poor covariance estimation in Markowitz portfolio
construction. The work isolated covariance error from expected-return error
by working with the global minimum-variance (GMV) portfolio in a Gaussian
benchmark where the true covariance is proportional to the identity. In that
setting the exact finite-sample inflation of out-of-sample variance is a
Wishart calculation, and it was checked by Monte Carlo simulation before any
economic claims were attached to it (P1).

The second turn asked for an economic interpretation and a dollar cost. The
statistical inflation was decomposed as a zero-expected-return side bet that
the optimizer places on sampling noise, and translated into an annual
certainty-equivalent loss for an illustrative investor. A reviewer-model check
tightened several points: the zero-expected-return reading requires all assets
to share the same true expected return; the in-sample risk forecast shrinks by
a factor $1-c$ relative to the oracle (not relative to the realized risk);
the dollar figure is a welfare-equivalent valuation, not a predicted trading
loss; and within El Karoui's elliptical model class the Gaussian case yields
the least risk underestimation, so the Gaussian benchmark is favorable rather
than alarmist. The comparison against a structured estimator was made
explicit: a correctly specified structured estimator recovers the oracle
weights in the benchmark world, so the full inflation counts as the cost of
using the sample matrix (P2).

The session ended with the present compilation request (P3). One citation
error made in P1 (a link for El Karoui 2013 pointing to an unrelated 2026
paper) was identified during the P2 review and corrected.

# Results

The headline finding is that the cost of plugging the sample covariance matrix
into a minimum-variance optimizer is a simple function of the aspect ratio
$c = N/T$ alone: expected out-of-sample variance is inflated by a factor
converging to $1/(1-c)$, so at $c = 0.9$ the "minimum-variance" portfolio
carries ten times the variance of the naive equal-weight portfolio it was
supposed to improve upon. The subsections below give the exact result, the
mechanism, and the dollar translation.

## Exact risk inflation of the plug-in GMV portfolio

Consider $N$ assets with i.i.d. Gaussian returns, true covariance
$\Sigma = I$, short selling allowed, and full investment. The oracle
portfolio is the equal-weight portfolio $w_* = \mathbf{1}/N$ with variance
$V_* = 1/N$. Estimating the covariance by the sample matrix $S$ from
$T$ demeaned observations ($\nu = T - 1$ degrees of freedom) and solving
the GMV program yields weights
$\hat w = S^{-1}\mathbf{1} / (\mathbf{1}^\top S^{-1}\mathbf{1})$. The
sample covariance is invertible when $T > N$, and the finite expectation
below requires $T > N + 1$. The expected inflation of realized variance has
the exact finite-sample form

$$
\mathbb{E}\!\left[\frac{\hat w^\top\Sigma\,\hat w}{V_*}\right]
= 1 + \frac{N-1}{\nu - N},
$$

which converges to $1/(1-c)$ as $N/T \to c < 1$ (P1). A Monte Carlo
simulation with $T = 250$ confirms the formula: at $N = 200$ the measured
mean ratio is 5.09 against an exact value of 5.06 and the asymptotic 5.00; at
$N = 225$ the measured 10.30 matches the exact 10.33 (Appendix B.1). The
practical reading is that at $c = 0.5$ the optimized portfolio has twice
the oracle variance, and at $c = 0.9$ it has ten times the oracle variance,
at which point careful optimization is an order of magnitude worse than not
optimizing at all.

![Figure 1: Out-of-sample risk inflation and welfare cost of the sample-covariance GMV portfolio as a function of the aspect ratio c = N/T. Panel (a) shows the variance multiplier (exact finite-sample curves for T = 250 and T = 2500, and the asymptotic 1/(1-c)); panel (b) shows the annual certainty-equivalent loss for a USD 1 billion portfolio with risk aversion 2 and oracle volatility 8%.](fig1.png)

## The mechanism: a zero-alpha bet on noise

The inflation has an exact decomposition that supplies the economic
interpretation (P2). Assume all assets share the same true expected return,
$\mu = m\mathbf{1}$, so that every fully invested portfolio has the same
expected return. Writing the estimated weights as the oracle weights plus an
error, $\hat w = w_* + \delta$ with $\mathbf{1}^\top\delta = 0$, and using
the optimality condition $\Sigma w_* = V_*\mathbf{1}$, the realized risk is

$$
V_{\mathrm{out}} = V_* + \delta^\top\Sigma\,\delta .
$$

The optimizer's deviation from the oracle is a zero-investment,
zero-expected-return gamble: it does not change the portfolio's expected
return, it only adds variance. The mechanism is that sampling noise creates
directions in which the estimated variance is artificially low, and inverting
the sample covariance causes the optimizer to concentrate weight in these
apparently safe directions, which are in fact noise. Asymptotically the
deviation adds variance approximately $V_*\, c/(1-c)$. The mirror-image
effect is that the in-sample risk forecast shrinks to approximately
$(1-c)V_*$, so the portfolio looks safest to its own risk model precisely
when it is most contaminated; the ratio of forecast to realized variance is
approximately $(1-c)^2$.

## The dollar cost: a 5.8% invisible annual fee at c = 0.9

For an investor with mean-variance preferences and risk-aversion parameter
$\gamma$, the annual certainty-equivalent value of a portfolio is
$CE = \mu - \tfrac{\gamma}{2}\sigma^2$, exact for conditionally Gaussian
returns under CARA utility with absolute risk aversion $\gamma/W$. For an
arbitrary structured estimator the welfare-equivalent annual cost of using the
sample covariance matrix is

$$
L = \frac{\gamma W}{2}\left(V_{\mathrm{sample}} - V_{\mathrm{struct}}\right).
$$

In the benchmark world, a correctly specified structured estimator recovers
the oracle weights (this holds, for example, for a spherical or
compound-symmetry estimator when the truth is of that form), so
$V_{\mathrm{struct}} = V_*$ and

$$
L \approx \frac{\gamma W}{2}\,\sigma_*^2\,\frac{c}{1-c}.
$$

Calibrated to $W$ = USD 1 billion, oracle volatility $\sigma_* = 8\%$
annualized, and $\gamma = 2$, for an illustrative investor (P2):

| c = N/T | Sample portfolio volatility | Annual CE cost | Percent of AUM |
|---------|-----------------------------|----------------|----------------|
| 0.50 | 11.3% | USD 6.4 million | 0.64% |
| 0.80 | 17.9% | USD 25.6 million | 2.56% |
| 0.90 | 25.3% | USD 57.6 million | 5.76% |
| 0.95 | 35.8% | USD 121.6 million | 12.16% |

At $c = 0.9$ the noise lifts portfolio volatility from 8% to about 25%, and
eliminating that risk would be worth roughly USD 58 million per year to this
investor, equivalent to an invisible 5.8% annual fee on assets. As $c$
approaches 1 from below the cost diverges, and once $N$ reaches $T$ the
demeaned sample matrix is singular and the plug-in approach fails outright.
Two qualifications are essential: this is a welfare-equivalent valuation of
unnecessary risk, not a predicted trading loss (expected arithmetic returns
are unchanged in this benchmark); and it is an expectation across estimation
samples, not a guarantee for every fitted portfolio.

## The verified literature

Four canonical references were located and verified against their primary
landing pages and abstracts (P1, P2). El Karoui
[1](http://arxiv.org/abs/1211.2917) provides the rigorous
random-matrix-theory treatment of the plug-in Markowitz problem, showing that
the price of estimating the covariance matrix is a variance underestimation by
roughly a factor $1 - p/n$, with a clean separation between
mean-estimation and covariance-estimation error. El Karoui
[2](https://doi.org/10.1137/090774926) extends the analysis of realized risk
to elliptical distributions and finds that, within that model class, the
Gaussian case yields the least risk underestimation, so the Gaussian benchmark
used above is the favorable case rather than a scare figure. Ledoit and Wolf
[3](http://www.ledoit.net/honey.pdf) is the classic practitioner-facing
statement that nobody should use the sample covariance matrix for portfolio
optimization, and introduces shrinkage toward a structured target as the
standard remedy. Chopra and Ziemba
[4](https://people.duke.edu/~charvey/Teaching/BA453_2006/Chopra_The_effect_of_1993.pdf)
is the classic empirical sensitivity study, whose headline finding that errors
in means matter most is precisely why the GMV portfolio is the cleanest
vehicle for isolating covariance error. A citation error in which a link
intended for [2] pointed to an unrelated 2026 paper was identified and
corrected.

# Discussion

For the user's objective, the findings deliver a compact, defensible story:
the cost of ignoring the high-dimensional nature of covariance estimation is
not a vague qualitative concern but a specific, computable function of the
aspect ratio $c = N/T$, and it is economically enormous at the $c$ values
that arise in practice whenever the investment universe is large relative to
the estimation window. The zero-alpha-gamble decomposition gives an intuitive
one-sentence account for a nontechnical audience, and the certainty-equivalent
table gives a number for a decision-maker.

Several limitations bound the strength of these conclusions. All results hold
in an unconstrained Gaussian benchmark with i.i.d. returns, equal expected
returns, and a true covariance proportional to the identity; long-only
constraints, shrinkage, and other regularization dampen the inflation, and
real return data exhibit heavy tails, volatility clustering, and factor
structure that the benchmark omits. The "Gaussian is favorable" statement is
established within El Karoui's elliptical model class, not for every
distribution or constraint set. The dollar calibration depends on the assumed
risk aversion, oracle volatility, and wealth, and on the premise that the
structured comparator is correctly specified; for a mis-specified structured
estimator the comparison must use its actual risk rather than the oracle
value. The expectation is over estimation samples. Finally, secondary costs
that are real but unquantified here, such as turnover generated by unstable
weights, were deliberately excluded.

The conclusions would weaken if the aspect ratio were small (at $c = 0.1$
the inflation is about 11%, and it decreases continuously as $c$ falls), or
if the application involved portfolios where the expected-return channel
dominates the covariance channel in economic significance, as in the setting
of Chopra and Ziemba.

# Conclusions

1. **Lead with the aspect ratio.** The single number $c = N/T$ governs the
   cost: variance inflation $1/(1-c)$, so $c = 0.5$ doubles and
   $c = 0.9$ decuples out-of-sample variance. Next step: compute $c$ for
   the user's own application (universe size versus estimation window) as the
   entry point of any presentation.
2. **Translate to dollars for impact.** At $c = 0.9$, the noise gamble is
   worth about USD 58 million per year to a USD 1 billion investor, an
   invisible 5.8% annual fee. Next step: adapt the calibration
   ($\gamma$, $\sigma_*$, $W$) to the audience's balance sheet.
3. **Cite the canon.** El Karoui (2010, 2013) for theory, Ledoit-Wolf (2004)
   for the practitioner statement and the shrinkage remedy, Chopra-Ziemba
   (1993) for the empirical sensitivity context. Next step: pair the example
   with Ledoit-Wolf's shrinkage estimator as the constructive fix.

# References

1. El Karoui, N. High-dimensionality effects in the Markowitz problem and other quadratic programs with linear constraints: Risk underestimation. Annals of Statistics 38(6):3487-3566, 2010. http://arxiv.org/abs/1211.2917 (accessed 2026-10-28).
2. El Karoui, N. On the realized risk of high-dimensional Markowitz portfolios. SIAM Journal on Financial Mathematics 4(1):737-783, 2013. https://doi.org/10.1137/090774926 (accessed 2026-10-28).
3. Ledoit, O. and Wolf, M. Honey, I Shrunk the Sample Covariance Matrix. Journal of Portfolio Management 30(4):110-119, 2004. http://www.ledoit.net/honey.pdf (accessed 2026-10-28).
4. Chopra, V. K. and Ziemba, W. T. The effect of errors in means, variances, and covariances on optimal portfolio choice. Journal of Portfolio Management 19(2):6-11, 1993. https://people.duke.edu/~charvey/Teaching/BA453_2006/Chopra_The_effect_of_1993.pdf (accessed 2026-10-28).

# Appendix A: Verbatim user prompts

**P1** (turn 1, time not recorded). Request for references and a simple example of the cost of poor covariance estimation.

```text
Can you find some references for or can you provide some simple example of the theoretical costs incurred in poor estimation of a return covariance matrix for the purposes of Markowitz portfolio construction? I want to give an idea how important the high-dimensional covariance estimation problem is.
```

**P2** (turn 2, time not recorded). Request for economic interpretation and dollar quantification.

```text
Can we give these results an economic interpretation of some kind, possibly intuitive? What is the hypothetical dollar cost of using the plain sample covariance estimator when N and T are large and their aspect ratio is close to 1, instead of a structured one?
```

**P3** (turn 3, time not recorded). Request to compile this report.

```text
Compile a report with these findings using the following template.
```

# Appendix B: Code

The code below was run with Python 3.14.8 and NumPy 2.5.4 in the session
sandbox on 2026-10-28. Snippet B.1 checks the analytical risk-inflation
formula by Monte Carlo simulation; snippet B.2 computes the
certainty-equivalent dollar calibration reported in Results; snippet B.3
generates Figure 1.

## B.1 Monte Carlo check of the risk-inflation formula

Each trial draws $T$ observations of $N$ standard Gaussian assets, demeans
them, forms the sample covariance $S$, computes the plug-in GMV weights, and
records the realized variance ratio $N \cdot \hat w^\top \hat w$, since
$\Sigma = I$ and $V_* = 1/N$.

```python
import numpy as np
rng = np.random.default_rng(0)

def simulate(N, T, trials=4000):
    nu = T - 1                       # degrees of freedom, demeaned data
    ratios = np.empty(trials)
    for i in range(trials):
        X = rng.standard_normal((T, N))
        X = X - X.mean(axis=0)
        Sinv = np.linalg.inv(X.T @ X)
        w = Sinv.sum(axis=1) / Sinv.sum()
        ratios[i] = N * (w @ w)       # w' Sigma w / V*, Sigma = I
    exact = 1 + (N - 1) / (nu - N)
    return ratios.mean(), exact

for N in [25, 50, 100, 200, 225]:
    m, ex = simulate(N, T=250)
    print(f'N={N:3d} T=250 N/T={N/250:.2f}  MC mean={m:.3f}  exact={ex:.3f}')
```

**Output.**

```text
N= 25 T=250 N/T=0.10  MC mean=1.106  exact=1.107
N= 50 T=250 N/T=0.20  MC mean=1.247  exact=1.246
N=100 T=250 N/T=0.40  MC mean=1.659  exact=1.664
N=200 T=250 N/T=0.80  MC mean=5.090  exact=5.061
N=225 T=250 N/T=0.90  MC mean=10.299 exact=10.333
```

## B.2 Certainty-equivalent dollar calibration

Computes the annual welfare-equivalent loss
$L = \frac{\gamma W}{2}\sigma_*^2\frac{c}{1-c}$ and the resulting
sample-portfolio volatility, for $W$ = USD 1 billion, $\sigma_* = 8\%$,
$\gamma = 2$ (Figure 1b, table in Results).

```python
sigma_star, gamma, W = 0.08, 2.0, 1e9
for c in [0.5, 0.8, 0.9, 0.95]:
    vol = sigma_star / (1 - c) ** 0.5
    loss = (gamma / 2) * W * sigma_star ** 2 * c / (1 - c)
    print(f'c={c}: vol {vol:.1%}, CE loss {loss/1e6:.1f}M/yr '
          f'({loss/W:.2%} of AUM)')
```

**Output.**

```text
c=0.5: vol 11.3%, CE loss 6.4M/yr (0.64% of AUM)
c=0.8: vol 17.9%, CE loss 25.6M/yr (2.56% of AUM)
c=0.9: vol 25.3%, CE loss 57.6M/yr (5.76% of AUM)
c=0.95: vol 35.8%, CE loss 121.6M/yr (12.16% of AUM)
```

## B.3 Figure generation

Generates Figure 1: panel (a) plots the exact finite-sample multiplier
$1 + (N-1)/(\nu - N)$ for $T = 250$ and $T = 2500$ against the asymptotic
$1/(1-c)$; panel (b) plots the certainty-equivalent loss from B.2 with the
calibration points marked.

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

c = np.linspace(0.01, 0.95, 400)
asym = 1 / (1 - c)

def exact(T, c):
    nu = T - 1
    N = np.ceil(c * T)
    return 1 + (N - 1) / (nu - N)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
ax.plot(c, asym, 'k--', lw=1.5, label=r'asymptotic $1/(1-c)$')
ax.plot(c, exact(250, c), lw=1.8, label=r'exact, $T=250$')
ax.plot(c, exact(2500, c), lw=1.8, label=r'exact, $T=2500$')
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
W, sig, g = 1e9, 0.08, 2.0
L = (g / 2) * W * sig ** 2 * c / (1 - c) / 1e6
ax.plot(c, L, lw=1.8, color='steelblue')
for cv in [0.5, 0.8, 0.9, 0.95]:
    lv = (g / 2) * W * sig ** 2 * cv / (1 - cv) / 1e6
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
```

**Output.** See Figure 1.
