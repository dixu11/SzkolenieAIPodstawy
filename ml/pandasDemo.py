import pandas as pd

df = pd.DataFrame({
    "name": ["Anna", "Jan"],
    "age": [25, 30],
    "score": [88.5, 92.0]
})

print(type(df))
print(type(df['age']))
print(type(df['age'].values))
print('----------')
print(df)
print(df['age'])
print(df['age'].values)

df = pd.read_csv('brfss_10cols_clean.csv')
print(df)
print('---')
print(df.head())
print(df.info())
print(df.describe())