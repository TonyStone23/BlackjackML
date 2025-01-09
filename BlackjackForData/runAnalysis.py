import timeit
import matplotlib.pyplot as plt
import numpy as np

x_val = []
y_val = []

last = 0
rounds = 10
for i in range(20):
    toTime = f"""
import pandas as pd
from strategyOne import game
games = []
for i in range({rounds}):
    game_df = pd.DataFrame(game())
    games.append(game_df)
df = pd.concat(games)
df.to_csv('StrategyOne.csv', index_label = 'Rounds')
"""
    
    rounds += 10
    t = timeit.Timer(stmt = toTime)
    x_val.append(rounds)
    y_val.append(t.timeit(number = 10))

plt.figure(figsize = [10, 8])
plt.xlabel("10's of games")
plt.ylabel("seconds")
plt.plot(x_val[1:-1], y_val[1:-1])
plt.grid(True)
plt.show()

print("Done :)")
