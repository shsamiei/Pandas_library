import pandas as pd 

df = pd.read_csv("Titanic.csv")

for index, row in df.iterrows():
    print(row)

    