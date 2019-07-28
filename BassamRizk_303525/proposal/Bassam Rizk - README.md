# Research Proposal


# Purpose
I would like to develop an option screening algorithm for stocks whose option Trees are likely to rally upward or downward due to a combination of corporate &/or market events.
That would be leveraged for a straddle* trading strategy.


# Approach
Download:
S&P 500 list of symbol (Wikipedia)
S&P 500 Stock historical (10 years) 
S&P 500 Option Tree historical data 
Greeks historical data
Consolidate & clean all 3 data sets
Divide data into test & training sets
Using training data sets:
Isolate historical straddle opportunities during the last 10 years (where stock price had a 5% increase with similar increase in option prices)
Clustering for optimal straddle opportunities using multi variables (strike price in the option tree, Greeks, market depths, beta, volatility)
Using testing data set:
Test the top 10 selection combinations

# Resources

A list of some of the libraries that I will be using a list of libraries:
https://cran.r-project.org/web/views/Finance.html

fOptions (Option pricing tool)
RQuantLib (Option pricing tool)
Quantmod (Option price & Greeks display tool from Yahoo)
Backtest (backtesting investment strategies)
PortfolioSim (Simulation tool)
fCertificates (embedded Options strategies functions)
GUIDE (calculators for Option pricing with 3D plots)
QuantTools (historical Stock/Option pricing download)
QuantMode (historical prices for Stocks / Options)
Quandl (historical prices for stocks / Options)

# Literature Review

Hedging volatility risk
M Brenner, EY Ou, JE Zhang - Journal of Banking & Finance, 2006 - Elsevier
Volatility risk plays an important role in the management of portfolios of derivative assets as well as portfolios of basic assets. This risk is currently managed by volatility “swaps” or futures. However, this risk could be managed more efficiently using options on volatility that were proposed in the past but were never introduced mainly due to the lack of a cost efficient tradable underlying asset.
The objective of this paper is to introduce a new volatility instrument, an option on a straddle, which can be used to hedge volatility risk. The design and valuation of such an instrument are the basic ingredients of a successful financial product. In order to value these options, we combine the approaches of compound options and stochastic volatility. Our numerical results show that the straddle option is a powerful instrument to hedge volatility risk. An additional benefit of such an innovation is that it will provide a direct estimate of the market price for volatility risk. 
 
 
Empirical properties of straddle returns
F Goltz, WN Lai - The Journal of Derivatives, 2009 - jod.iijournals.com
An at-the-money (ATM) straddle, ie, going long an ATM call and an ATM put with the same maturity, is generally thought of as a volatility trade. It is essentially delta-neutral, but a large price move in either direction or an increase in implied volatility will produce a profit. A delta-neutral straddle position also has zero beta, so under the CAPMit should earn the riskless rate. Research has shown, however, that straddles with stock index options tend to lose money, which may be attributed to a volatility risk premium: it is the cost of hedging against a rise in volatility. If buying straddles produces losses, writing straddles should yield excess profits. An important aspect of the trade is that the delta (and beta) of the position change when the underlying index moves away from its initial level, and rebalancing is necessary if one wishes to maintain neutrality.

In this article, Goltz and Lai examine the performance of buying and holding one-month straddles on the DAX index, with and without rebalancing, and find negative returns on average. If investors are entering the trade as a volatility hedge, one might expect the return to vary with other measures on volatility risk and potential hedging demand. They find that a widening credit spread on corporate bonds relative to government bonds, greater stock market turnover, and higher actual volatility all are related to straddle returns. But in considering what position an investor with constant relative risk aversion would take in straddles as part of an optimal portfolio including the underlying stock index and the riskless asset, they show that for risk aversion over a broad range, the optimal position would be to short straddles. That is, the “risk premium” in the market is too big to be consistent with utility maximization by investors with a reasonable level of risk aversion. The effect is most important for daily rebalancing, but that requires bearing heavy transaction costs, to the point that the potential improvement in utility would be largely wiped out in trying to capture it in the market.


Evaluating volatility forecasts in option pricing in the context of a simulated options market
E Xekalaki, S Degiannakis - Computational statistics & data analysis, 2005 - Elsevier
The performance of an ARCH model selection algorithm based on the standardized prediction error criterion (SPEC) is evaluated. The evaluation of the algorithm is performed by comparing different volatility forecasts in option pricing through the simulation of an options market. Traders employing the SPEC model selection algorithm use the model with the lowest sum of squared standardized one-step-ahead prediction errors for obtaining their volatility forecast. The cumulative profits of the participants in pricing 1-day index straddle options always using variance forecasts obtained by GARCH, EGARCH and TARCH models are compared to those made by the participants using variance forecasts obtained by models suggested by the SPEC algorithm. The straddles are priced on the Standard and Poor 500 (S & P 500) index. It is concluded that traders, who base their selection of an ARCH model on the SPEC algorithm, achieve higher profits than those, who use only a single ARCH model. Moreover, the SPEC algorithm is compared with other criteria of model selection that measure the ability of the ARCH models to forecast the realized intra-day volatility. In this case too, the SPEC algorithm users achieve the highest returns. Thus, the SPEC model selection method appears to be a useful tool in selecting the appropriate model for estimating future volatility in pricing derivatives.

Expected option returns
JD Coval, T Shumway - The journal of Finance, 2001 - Wiley Online Library
This paper examines expected option returns in the context of mainstream asset‐pricing theory. Under mild assumptions, expected call returns exceed those of the underlying security and increase with the strike price. Likewise, expected put returns are below the risk‐free rate and increase with the strike price. S&P index option returns consistently exhibit these characteristics. Under stronger assumptions, expected option returns vary linearly with option betas. However, zero‐beta, at‐the‐money straddle positions produce average losses of approximately three percent per week. This suggests that some additional factor, such as systematic stochastic volatility, is priced in option returns.

Laplace transforms and the American straddle
G Alobaidi, R Mallier - Journal of Applied Mathematics, 2002 - hindawi.com
We address the pricing of American straddle options. We use partial Laplace transform techniques due to Evans et al.(1950) to derive a pair of integral equations giving the locations of the optimal exercise boundaries for an American straddle option with a constant dividend yield.
Financial volatility trading using a self-organising neural-fuzzy semantic network and option straddle-based approach
WL Tung, C Quek - Expert Systems with Applications, 2011 - Elsevier
Financial volatility refers to the intensity of the fluctuations in the expected return on an investment or the pricing of a financial asset due to market uncertainties. Hence, volatility modeling and forecasting is imperative to financial market investors, as such projections …

