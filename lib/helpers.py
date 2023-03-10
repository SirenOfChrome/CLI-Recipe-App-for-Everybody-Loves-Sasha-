import argparse

def addFirstName():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', type=str, required=True,
                        help='Enter your name')
    args = parser.parse_args()
    print(f"Hello, {args.name}!")