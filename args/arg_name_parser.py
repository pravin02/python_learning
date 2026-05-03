import argparse


def main(args):
    print("This is the main module")
    try:       
        print(f"Argument: Name: {args.name}, Sort: {args.sort}")
    except Exception as e:
        print(f"Exception: {e}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple argument parser example")
    parser.add_argument("--name", type=str, help="User need to provide a name")
    parser.add_argument("--sort", type=bool, help="Required sorting order")
    args = parser.parse_args()

    main(args)

#  uv run .\args\arg_name_parser.py  --name=pravin --sort=True
