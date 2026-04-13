# Function: A reusable block of code that performs a specific task. Defined using the keyword.
# Arguments: Values passed into a function when calling it. Allows customizing behaviour.
# Variable Arguments: Allows passing an arbitary number of arguments to a function.
# Keyword Arguments: Arguments passed by name rather than position. Can have default values.


def simple():
    print("Simple")

simple()


# Function example
def double(no):
    """Doubles a number"""
    return no * 2


print(double(20))


# Function with Arguments
def full_name(first_name, last_name):
    return first_name + " " + last_name


print(full_name("Pravin", "Patil"))


# Variable arguments
def running_sum(*numbers):
    sum = 0
    for no in numbers:
        sum += no
    return sum


print("Variable Argument ", running_sum(2, 3, 5, 1))


# Keyword argument
def greeting(name, greeting="Hello, "):
    print(greeting + name)


greeting(full_name("Pravin", "Patil"))

# Generator: A type of iterable like lists or tuples but does not store the funll sequence in memory at once.
# Uses yeild to generate one item at a time


def counter(start=0):
    # n = start
    while True:
        yield start
        start += 1


for i in counter(5):
    if i > 10:
        break
    print(i)

print("\nFibonacci Series")


# Infinite Fibonacci sequence generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for n in fib():
    if n > 1000:
        break
    print(n)


# Generator expression: More compact syntax like list comprehensions for inline lazy generation, uses() instead of []
numbs = (x**2 for x in range(11))
print(list(numbs))

# Infinite Sequence: Generators can be infinitely recursive/iterative or model data strams
import random

attacks = ["Kimura", "armbar", "triangle"]


def lazy_random_attacks():
    """Laxily yield random attacks forever"""
    while True:
        attack = random.choice(attacks)
        print("Yielding attack")
        yield attack


generator = lazy_random_attacks()

for _ in range(5):
    print(next(generator))
