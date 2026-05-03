import sys

if __name__ == "__main__":
    print("This is the main module")
    try:
        for i in sys.argv:
            print(f"Argument: {i}")
    except IndexError as e:
        print(f"Error: {e}. Expected an argument.")

# uv run args/multi.py one two three
