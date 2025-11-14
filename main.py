import argparse

from src.scripts.explore_data import explore_data


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("explore")

    args = parser.parse_args()

    if args.command == "explore":
        explore_data()


if __name__ == "__main__":
    main()
