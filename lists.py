# # Below code show how to play list
numbers = [10, 1, 2, 3, 4, 5, 6, 7, 8]

print(numbers)

print("\n Looping numbers")
for num in numbers:
    print(num)

print("\nEnumerating numbers by index")
for i, num in enumerate(numbers):
    print(f"{i} = {numbers[i]}")


# # List conprehensions
print("Loop + filter the list")
filtered_numbers = [n for n in numbers if n < 5]
print("Filtered Numbers: ", filtered_numbers)

print("Find the even elements from the list: ", [n for n in numbers if n % 2 == 0])
print("Find the odd elements from the list: ", [n for n in numbers if n % 2 != 0])

# Lists can contains different types of data types

lists = [1, "one", 1.0]
print("\n", lists)
print(f"Finding 'one' text in list {'one' in lists}")

print(f"'one' text should not present in list {'one' not in lists}")

print(f"Count number of items {len(lists)}")

print("\n Code to check data type of its content")
for i, data in enumerate(lists):
    print(f"{i} --- {data} --- {type(data).__name__}")


lists = ["one", "two", "three", "Four", "Five"]
print("\n", lists)
print("Print list from two: ", lists[1:])
print("Print list from two to three: ", lists[1:3])
print("reverse list without altering content: ", lists[::-1])
lists.reverse()
print("reverse list and alter the content: ", lists)
print("Count the present of element in the list: ", lists.count("one"))
lists.remove("one")
print("Remove the 'one' from the list: ", lists)
print("Pop out last element from the list: ", lists.pop())
print("List after poping out: ", lists)
lists.sort(reverse=True)
print("Sort list in natural order: ", lists)

print("\n Program which takes input from user")

total_items = int(input("Please Enter How many element you want to add in List: "))
custom_list = []
for i in range(0, total_items):
    try:
        data = input(f"Index: {i+1} -- Content: ")
        custom_list.append(data)
    except Exception as e:
        print(f"Exception: {e}")
        if not i == 0:
            i -= 1
print(f"Data Inserted in the list is : {custom_list}")

while True:
    try:
        index = int(input("Enter Index for Look Up: "))
        if abs(index) == 0:
            print("No element at index 0")
            continue
        elif abs(index) > len(custom_list):
            print("Index is greater than list length")
            continue
        elif index < 0:
            index += 1
        # elif index - 1 >= len(custom_list):
        #     print("Index is greater than available records in custom_list")
        #     continue

        print(f"Data on Index: {index} is : {custom_list[index-1]}")
    except Exception as e:
        print(f"Exception: {e}")
