import argparse
import pandas
import pathlib


def restructure_csvs():
    args = construct_and_parse_args()
    if not args.parent_directory.is_absolute():
        args.parent_directory = pathlib.Path.cwd() / args.parent_directory
    for csv_file in args.parent_directory.rglob("*.csv"):
        pandas.read_csv(csv_file, sep="\t").to_csv(csv_file, index=False)


def construct_and_parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("parent_directory", type=pathlib.Path)
    return parser.parse_args()


if __name__ == "__main__":
    restructure_csvs()
