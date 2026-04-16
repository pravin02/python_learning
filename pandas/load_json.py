import pandas as pd
try:
    data = pd.read_json("dataset/users.json")
    print(data)
except FileNotFoundError as fnfe:
    print(f"File Not Found {fnfe}")
    