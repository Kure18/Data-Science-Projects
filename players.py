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

print(players.head(20))

print(players.drop_duplicates(subset="name"))

print(players["position"].value_counts(sort=True))

print(players["position"].value_counts(normalize=True))

print(players.groupby("position")["now_cost_rank_type"].mean())

print(players.groupby("team")["minutes"].agg(["min","max","mean"]))

print(players.groupby("name")["now_cost_rank"].mean())

print(players.groupby(["name","team"])[["minutes"]].mean())

print(players.pivot_table(index="position",values="minutes"))

print(players.pivot_table(index="team",values="total_points",columns="now_cost_rank_type",fill_value=0,margins=True))

import numpy as np
print(players.pivot_table(index="team",values="minutes",aggfunc=[np.mean,np.min,np.max]))

print(players.set_index("minutes"))

june = players.set_index("minutes")
print(june)

print(june.reset_index())

print(june.reset_index(drop=True))

july = players.set_index("team")

print(july)

print(july.loc["Liverpool"])

print(july.loc["Wolves"])

august = players.set_index(["team","name"])
print(august)

print(august.loc[["Liverpool","Brentford"]])

print(august.sort_index())