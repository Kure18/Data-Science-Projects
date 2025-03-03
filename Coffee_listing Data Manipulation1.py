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