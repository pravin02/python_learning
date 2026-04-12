# Dictionry is like a map the data with keys
simple_dict = {"1": "one", "2": "Two"}
print(f"{simple_dict}")
print(f"Get Value by key: {simple_dict["1"]}")
print(simple_dict.get("1"))
print(f"Keys in the dictionary : {simple_dict.keys()}")

# Loop over the dictionary by keys
for item in simple_dict.keys():
    print(item)

# Loop over the dictionary by values
for item in simple_dict.values():
    print(item)

# Loop over the dictionary by key & value
for key, value in simple_dict.items():
    print(f"{key} == {value}")


copy_dict = simple_dict.copy()
print("Copied dictionary: ", copy_dict)
copy_dict.update({"1": "nine"})
print("Copied dictionary after update ", copy_dict)
print("Original dictionary after copied dictionary update ", simple_dict)

# override dictionary record
simple_dict.update({"1": "twenty"})
print(simple_dict)
print(f"Pop thr element by key {simple_dict.pop("1")}")
print("Dictionary after poping out ", simple_dict)
if simple_dict:
    print("Some records in dictionary")
else:
    print("Dictionary is empty")
simple_dict.clear()
print("Clearing the dictionary ", simple_dict)

if simple_dict:
    print("Some records in dictionary")
else:
    print("Dictionary is empty")
