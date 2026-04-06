text = "learning python"

print("Length of the string ", len(text))

print("String starts with ", text.startswith("l"))
print("String ends with ", text.endswith("on"))
print("contains index", text.find("ng"))
print("contains ", "ng" in text)
print("3rd index character ", text[3])


print("Round ", round(2.9))
print("abs ", abs(-2.9))

import math

print("ceil ", math.ceil(2.9))
print("factor ", math.factorial(3))

print("bool(-1) is True  ", bool(-1));
print("bool(0) is False ", bool(0));
print("bool(1) is True  ", bool(1));
print("bool(24) is True  ", bool(24));
print("bool(True) is True  ", bool(True));
print("bool(False) is False  ", bool(False));
print("bool("") is True  ", bool(""));
print("bool(\"False\") is True  ", bool("False"));

no1 = input("Enter no1: ")
no2 = input("Enter no2: ")

print("Y+9*/ou have entered ", no1, no2)
print("Addition ", no1 + no2)

print("Addition ", int(no1) + int(no2))