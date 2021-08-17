# Author

Chapman University, CS 532 - Computational Economics I

Tracy, J. D., James, K. A., Kaplan, H., & Rassenti, S. (2021). An investigation of health insurance policy and behavior in a virtual environment. Plos one, 16(4), e0248784.

Steve Vu

# 1. Introduction

Inspried by Tracy el at. 2021, the project aims at applying genetic algorithms to search for an optimal healthcare investment strategy of rational agents whose ultimate goals are to maximize their life enjoyment in the whole life. At inception, an agent is endowed an initial level of health that is a decreasing linear function of periods. In each period, an agent will earn money by working and decide how much to invest in healthcare, life enjoyment, and savings. An agent will die if his health is nonpositive or the experiment ends after specified periods.

# 2. 

$Income = v * T * M * max(0, M * (1 - y * \frac{100-CurrentHealth}{100}))$

hgh

$HealthRegain = 100 * \frac{\exp(k * HealthInvestment)}{\exp(k * 
HealthInvestment) + \frac{100 - HealthAfterHarvest}{HealthAfterHarvest}}$


hgfh

$LifeEnjoyment = c * \frac{CurrentHealth}{100} * \frac{LifeInvestment}{LifeInvestment + a}$


hgfhfg

$HealthAfterHarvest = CurrentHealth -(FixedPoint + DegenSlope * CurrentPeriod)$


gfg

|Parameters|Values|
|----------|------|
|c|700|
|a|45|
degen_slope|4|
|k|0.007|
|M|100|
|N|100|
|W|10|
|T|300|
|y|1|
|v|1|

# 3. Results

The maximum life enjoyment is over 1,400 units in the whole life. A rational agent invests heavily in health at the beginning, and gradually reduce it to closely zero. In contrast, the life investment ratio starts at low level before soaring to almost 100% at the end of the experiment. The savings ratio remains very low during the living periods.

![](https://github.com/SteveVu2212/Healthcare-Investment-Behavior/blob/main/images/subplots.png)
