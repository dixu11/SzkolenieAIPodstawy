import pandas as pd

df = pd.read_csv("ml/orders.csv")

# Start from a copy to create a "raw" noisy version
raw = df.copy()

# Introduce some missing values
raw.loc[5, "Quantity"] = None
raw.loc[12, "Price"] = None
raw.loc[20, "Country"] = None
raw.loc[25, "CustomerName"] = None

# Introduce some obviously invalid numeric values
raw.loc[7, "Quantity"] = 0           # quantity zero
raw.loc[16, "Price"] = 0.0           # free order
raw.loc[30, "Quantity"] = -2         # negative quantity

# Slight inconsistencies in Category capitalization / spacing
raw.loc[0, "Category"] = "electronics"
raw.loc[10, "Category"] = "Furniture "
raw.loc[15, "Category"] = "home office"

# Duplicate a couple of rows to have duplicates in data
dupes = raw.loc[[2, 10]]
raw_with_dupes = pd.concat([raw, dupes], ignore_index=True)

# Save as a new "raw" file for the exercise
out_path = "orders_raw.csv"
raw_with_dupes.to_csv(out_path, index=False)

