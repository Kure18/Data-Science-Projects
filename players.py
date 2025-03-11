import pandas as pd
players = pd.read_csv("players.csv")
print(players.head())

print(players.info)

print(players.columns)

print(players.shape)

print(players.index)

print(players.describe)

players["minutes_value"] = players["ict_index_rank"]*players["value_form"]
print(players["minutes_value"].head())

print(players.head())

print(players["now_cost"]>42)

print(players[players["now_cost"]>42])

print(players[players["now_cost"]>42].sort_values("ict_index_rank",ascending=False))

print(players["minutes_value"].mean())

print(players["now_cost"].cumsum())

print(players["ict_index_rank"].cummin())

print(players["ict_index_rank"].cummax())

print(players["ict_index_rank"].cumprod())

print(players["minutes_value"].agg(["mean","max"]))