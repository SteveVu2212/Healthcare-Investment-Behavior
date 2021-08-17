# Author

Chapman University, CS 532 - Computational Economics I

Tracy, J. D., James, K. A., Kaplan, H., & Rassenti, S. (2021). An investigation of health insurance policy and behavior in a virtual environment. Plos one, 16(4), e0248784.

Steve Vu

# 1. Introduction

Inspried by Tracy el at. 2021, the project aims at applying genetic algorithms to search for an optimal healthcare investment strategy of rational agents whose ultimate goals are to maximize their life enjoyment in the whole life. At inception, an agent is endowed an initial level of health that is a decreasing linear function of periods. In each period, an agent will earn money by working and decide how much to invest in healthcare, life enjoyment, and savings. An agent will die if his health is nonpositive or the experiment ends after specified periods.

# 2. Equations governing agents' enjoyment maximization problem

Each agent is endowned an initial level of health at 60 that determines his income in the first period. In each period, he harvests in exchange of an amount of money. After harvests, his health degenerates following a linear function as below.

![](https://github.com/SteveVu2212/Healthcare-Investment-Behavior/blob/main/images/Health%20After%20Harvest.png)

However, he is able to regain health by making an investment. The amount of regained health depends on the health investment and health after harvest.

![](https://github.com/SteveVu2212/Healthcare-Investment-Behavior/blob/main/images/Health%20Regain.png)

His ultimate goal is to maximize his total enjoyment during his living periods. The life enjoyment is a function of life investment and health after being regained.

![](https://github.com/SteveVu2212/Healthcare-Investment-Behavior/blob/main/images/Life%20Enjoyment.png)

hgfhfg

$HealthAfterHarvest = CurrentHealth -(FixedPoint + DegenSlope * CurrentPeriod)$



# 3. Results

The total maximum life enjoyment is over 1,400 units in the whole life. A rational agent invests heavily in health at the beginning, and gradually reduce it to closely zero. In contrast, the life investment ratio starts at low level before soaring to almost 100% at the end of the experiment. The savings ratio remains very low during the living periods.

![](https://github.com/SteveVu2212/Healthcare-Investment-Behavior/blob/main/images/subplots.png)
