import pandas as pd
df = pd.read_excel("Student_Performance_Data_Wide_Version.xlsx")
print(df.head(20))

print(df.info())
print(df.describe())
print(df.shape)
print(df.index)
print(df.values)
print(df.columns)

print(df["Paper 4"].sort_values(ascending=False))

print(df["Paper 3"]>55)
print(df[df["Paper 3"]>55])

print(df[["Paper 4", "Paper 5"]])

print(df[df["Paper 4"]==84.0])

g = df["Paper 3"]==85.0
f = df["Paper 4"]==44.0

print(df[g&f])

df["Total"] = df["Paper 1"] + df["Paper 2"] + df["Paper 3"] + df["Paper 4"] + df["Paper 5"] + df["Paper 6"] + df["Paper 7"]
print(df.head())

print(df["Total"].sum())
print(df["Total"].cumsum())
print(df["Total"].median())
print(df["Total"].mode())
print(df["Total"].quantile(0.3))
print(df["Total"].cummin())
print(df["Total"].cummax())
print(df["Total"].cumprod())

print(df.head(100))

print(df.drop_duplicates())

print(df["Paper 1"].value_counts(sort=True))

print(df["Total"].value_counts(normalize=True))

print(df.groupby("Student_ID")[["Paper 1"]].mean())

print(df.groupby("Student_ID")[["Paper 6","Paper 7"]].median())

print(df.pivot_table(values="Paper 1",index="Student_ID"))

print(df.pivot_table(index="Student_ID",values="Paper 6",columns= "Paper 7"))

print(df.pivot_table(index="Student_ID",values="Paper 6",columns= "Paper 7",fill_value=0))

print(df.pivot_table(index="Student_ID",values="Paper 6",columns="Paper 7",fill_value=0,margins=True))