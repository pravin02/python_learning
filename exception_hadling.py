# This program demonstrates how to handle exceptions in python

print(
    "This program takes inputs from user converts them into integers and devides first number with second number"
)

try:
    no1 = input("Enter First Number: ")

    no2 = input("Enter Second Number: ")

    div = int(no1) / int(no2)

    print(f"{no1}/{no2} = {div}")

except ValueError:
    print("Excption: Inputs must be integer number's only")
except ZeroDivisionError as e:
    print(f"Exception Occured: {e}")


print("\n Raise exception example")
try:
    no1 = int(input("Enter First Number: "))
    no2 = int(input("Enter Second Number: "))

    if no2 == 0:
        raise RuntimeError("Number is 0")
    div = no1 + no2
    print(f"{no1}/{no2}={div}")

except RuntimeError as e:
    print(f"Runtime Exception: {e}")
except ValueError as e:
    print(f"Value Error: please enter intergers only. e: {e}")
except ZeroDivisionError:
    print("No2 must not be zero")


print("\n Catch multiple exceptions in except block example")
try:
    no1 = int(input("Enter First Number: "))
    no2 = int(input("Enter Second Number: "))

    if no2 == 0:
        raise RuntimeError("Number is 0")
    div = no1 + no2
    print(f"{no1}/{no2}={div}")

except (RuntimeError, ValueError, ZeroDivisionError) as e:
    print(f"Runtime Exception: {e}")
