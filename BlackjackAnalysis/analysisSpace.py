import pandas as pd
from analysisFunc import regression
from genAnalysisFunc import average, standardDeviation
strats = {
    1: 'StrategyOne_35.csv',
    2: 'StrategyOne_40.csv',
    3: 'StrategyOne_45.csv',
    4: 'StrategyOne_50.csv',
    5: 'StrategyOne_55.csv',
    6: 'StrategyOne_60.csv',
    7: 'StrategyOne_65.csv',
    8: 'StrategyOne_70.csv', 
    9: 'StrategyOne_75.csv',
    10:'StrategyOne_80.csv',
}

df = pd.read_csv(f'C:/Users/apsto/VSC/blackjack_ML/DataFiveK/{strats.get(1)}')
regression(df)

'''
avEarn = average(df, 'Round Earnings')
print(avEarn)

sd = standardDeviation(df, 'Round Earnings')
print(sd)
'''