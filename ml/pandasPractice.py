import pandas as pd

df = pd.read_sas("LLCP2024.XPT")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.dtypes)
print('sleep:')
print([col for col in df.columns if 'SLE' in col.upper()])
# for col in df.columns:
#     print(col)

df_small = df[["SLEPTIM1", "BMI"]].copy()

print(df_small.head())