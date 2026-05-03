import sys
import json

def format_json(json_string):
    try:
        parsed_json = json.loads(json_string)
        formatted_json = json.dumps(parsed_json, indent=4, sort_keys=True)
        return formatted_json
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None


def main(path: str):
    try:
        with open(path, "r") as file:
            print(format_json(file.read()))
    except Exception as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python json_formatter.py <path_to_json_file>")
    else:
        main(sys.argv[1])

# command to run this script is
# python json_formatter.py dataset/users.json
