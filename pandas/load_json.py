import pandas as pd
try:
    data = pd.read_json("dataset\\users.json")
    print("File read successfully")
    #print(data)
except FileNotFoundError as fnfe:
    print(f"File Not Found {fnfe}")
except Exception as e:
    print(f"Exception: {e}")
    