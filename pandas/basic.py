import pandas as pd

data = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]

columns = ["apples", "bananas", "oranges"]
index = ["Monday", "Tuesday", "Wensday"]

df = pd.DataFrame(data, index, columns)
print(df)
