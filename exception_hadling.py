# This program demonstrates how to handle exceptions in python

print("This program takes inputs from user converts them into integers and devides first number with second number")

try:
    no1 = input("Enter First Number: ")

    no2 = input("Enter Second Number: ")

    div = int(no1) / int(no2)

    print(f"{no1}/{no2} = {div}")

except ValueError:
    print("Excption: Inputs must be integer number's only")
except ZeroDivisionError as e:
    print(f"Exception Occured: {e}")