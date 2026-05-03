import sys

if __name__ == "__main__":
    print("This is the main module")
    try:    
        print(f"Argument: {sys.argv[1]}")
    except IndexError as e:
        print(f"Error: {e}. Expected an argument.")

    