import argparse
import json

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
    )
    args = parser.parse_args()
    
    with open(args.first_file) as file:
        first_data = json.load(file)

    with open(args.second_file) as file:
        second_data = json.load(file)

    print(first_data)
    print(second_data)

if __name__ == "__main__":
    main()

