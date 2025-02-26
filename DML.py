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