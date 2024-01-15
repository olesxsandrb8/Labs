import pandas as pd

file_path = "velos_comptage.csv"
df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)

print(df.head())

most_popular_month = df.groupby(df['Date'].dt.month)['Berri1'].sum().idxmax()

print(f"Найбільш популярний місяць у велосипедистів: {most_popular_month}")
