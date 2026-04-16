import pandas as pd

csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"

# """ Pandas library has inbuild support to laod various types of files """
df = pd.read_csv(csv_url, index_col=0)

print(df.head())

print("-------------")
new_df = df[df["rating"]>90]
print(new_df)
print("-------------")

print("="*50)

# print(df.describe())

# print(df.info())

print(new_df.sort_values(by="name", ascending=True).head())

new_df["rating"].plot.hist()