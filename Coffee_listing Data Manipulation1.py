import pandas as pd
coffee_listing=pd.read_csv("C:\\Users\\007\\Documents\\GitHub\\Data Science Projects\\Data-Science-Projects\\coffee-listings-from-all-walmart-stores.csv")
print(coffee_listing)

print(coffee_listing.head())

print(coffee_listing.info())

print(coffee_listing.shape)

print(coffee_listing.describe())

print(coffee_listing.values)

print(coffee_listing.columns)

print(coffee_listing.index)

print(coffee_listing.sort_values(["price","rating"],ascending=[True,False]))

print(coffee_listing["rating"]>3.7)

print(coffee_listing[coffee_listing["rating"]>3.7])

print(coffee_listing[coffee_listing["weight_formatted_to_gramms"]==272.2])

print(coffee_listing[coffee_listing["coffee_type"].isin(["medium roast","caramel"])])

coffee_listing["price per gram"]=coffee_listing["price"]*coffee_listing["weight_formatted_to_gramms"]
print(coffee_listing["price per gram"])

print(coffee_listing["price per gram"].min())

print(coffee_listing["price per gram"].max())

print(coffee_listing["price per gram"].cumsum())

print(coffee_listing["price per gram"].median())

print(coffee_listing["price per gram"].std())

print(coffee_listing["price per gram"].var())

print(coffee_listing["coffee_type"].value_counts(sort=True))

print(coffee_listing["coffee_type"].value_counts(normalize=True))

print(coffee_listing.drop_duplicates(subset="coffee_type"))

print(coffee_listing.groupby("coffee_type")["price per gram"].mean())

print(coffee_listing.groupby("title")["coffee_type"].agg([min,max,sum]))

print(coffee_listing.head(10))

print(coffee_listing.pivot_table(values="price per gram",index="title"))

print(coffee_listing.pivot_table(values="rating",index="coffee_type",columns="price per gram"))

print(coffee_listing.pivot_table(values="rating",index="coffee_type",columns="price per gram",fill_value=0,margins=True))

print(coffee_listing.head(20))

coff_list=coffee_listing.set_index("coffee_type")

print(coff_list)

print(coff_list.reset_index())

print(coff_list.reset_index(drop=True))

print(coff_list.sort_index())

print(coffee_listing.head())

coff_ind=coffee_listing.set_index("weight").sort_index()
print(coff_ind)

coff_ind_rate=coffee_listing.set_index("rating").sort_index()
print(coff_ind_rate)

print(coff_ind_rate.iloc[2:5])

import matplotlib.pyplot as plt
coff_ind_rate["price per gram"].hist(bins=20)
plt.show()

avg_price=coff_ind_rate.groupby("coffee_type")["price per gram"].mean()
print(avg_price)

print(avg_price.plot(kind="bar",title="Mean",rot=90))
plt.show()

print(avg_price.plot(kind="bar",rot=90))
plt.show()

print(coffee_listing.plot(x="coffee_type",y="price per gram",kind="line",rot=45,title="Prices by kilogram"))
plt.show()

print(coffee_listing.isna())

print(coffee_listing.isna().any())

print(coffee_listing.isna().sum())

print(coffee_listing.fillna(0))

print(coffee_listing.isna().sum())

print(coffee_listing.fillna(0))