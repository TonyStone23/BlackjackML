import pandas as pd
from strategyOne import StrategyOne

strats = {
    1: 'Data/StrategyOne_35.csv',
    2: 'Data/StrategyOne_40.csv',
    3: 'Data/StrategyOne_45.csv',
    4: 'Data/StrategyOne_50.csv',
    5: 'Data/StrategyOne_55.csv',
    6: 'Data/StrategyOne_60.csv',
    7: 'Data/StrategyOne_65.csv',
    8: 'Data/StrategyOne_70.csv', 
    9: 'Data/StrategyOne_75.csv',
    10:'Data/StrategyOne_80.csv',
}
safeAt = {
    1: .35,
    2: .40,
    3: .45,
    4: .50,
    5: .55,
    6: .60,
    7: .65,
    8: .70,
    9: .75,
    10:.80
}
games = []

for ii in range(1, 11):
    for i in range(5000):
        game_df = pd.DataFrame(StrategyOne(safeAt.get(ii)))
        games.append(game_df)
    df = pd.concat(games)
    df.to_csv(strats.get(ii), index = False)
    print(f"done with {ii}")



#Need to run a lot of hands!!!!