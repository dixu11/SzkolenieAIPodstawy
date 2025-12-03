import pandas as pd

df = pd.read_csv('brfss_sample.csv')
df_cleared = pd.read_csv('brfss_10cols_clean.csv')


# print(df.shape)
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df_cleared.columns)
# for column in df.columns:
#     print(column)

df_small = df[['SLEPTIM1', '_BMI5', 'GENHLTH', '_AGEG5YR', 'SEX1',
       '_SMOKER3', 'EXERANY2', 'DIABETE3', 'MENTHLTH']].copy()
print(df_cleared.head())
print(df_small.head())
