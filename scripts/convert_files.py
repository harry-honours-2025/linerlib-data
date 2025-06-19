import argparse
import pathlib


def convert_files():

    def convert_file(child_path):
        child = child_path.name.lower()
        for substring, substitution in substitutions.items():
            child = child.replace(substring, substitution)
        child_path.rename(child_path.parent / child)

    args = construct_and_parse_args()
    # If a relative path is provided, treat it as relative to the current working directory.
    if not args.parent_directory.is_absolute():
        args.parent_directory = pathlib.Path.cwd() / args.parent_directory
    substitutions = {
        "dist": "distances",
        "rots": "rotations",
        "waf": "west-africa",
        "worldsmall": "world-small",
        "worldlarge": "world-large",
        "europeasia": "europe-asia",
        "transittime": "transit-time",
        "tt": "revised",
        "_": "-",
    }
    # Process relevant files first, then directories.
    for child_path in args.parent_directory.rglob("*"):
        if child_path.is_file() and child_path.suffix in {".csv", ".json"}:
            convert_file(child_path)
    for child_path in args.parent_directory.rglob("*"):
        if child_path.is_dir():
            convert_file(child_path)


def construct_and_parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("parent_directory", type=pathlib.Path)
    return parser.parse_args()


if __name__ == "__main__":
    convert_files()
