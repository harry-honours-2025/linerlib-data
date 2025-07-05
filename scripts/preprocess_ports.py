"""
Script for preprocessing the LINERLIB ports CSV.
Does not depend on the execution of any other scripts in advance.

Discards all ports where both:
    - The UNLOCODE does not appear as the origin or destination for any demand, and
    - Any of the transshipment, fixed port call, or variable port call fields are null.
"""

import argparse
import pandas
import pathlib


def preprocess_ports():
    args = construct_and_parse_args()
    args.output_directory.mkdir(parents=True, exist_ok=True)
    demands_data = pandas.concat(
        (pandas.read_csv(file) for file in args.demands_directory.rglob("*.csv")),
        ignore_index=True,
    )
    port_codes = pandas.concat([
        demands_data["Origin (UNLOCODE)"],
        demands_data["Destination (UNLOCODE)"],
    ])
    ports_data = pandas.read_csv(args.ports_csv_file)
    cost_fields = [
        "Transshipment Cost Per FFE (USD)",
        "Fixed Port Call Cost (USD)",
        "Variable Port Call Cost Per FFE (USD)",
    ]
    ports_data = ports_data[
        ports_data["UNLOCODE"].isin(port_codes) |
        ports_data[cost_fields].notna().all(axis=1)
    ]
    ports_data.to_csv(args.output_directory / args.ports_csv_file.name, index=False)


def construct_and_parse_args():
    def resolved_path(path):
        return pathlib.Path(path).resolve()

    parser = argparse.ArgumentParser()
    parser.add_argument("ports_csv_file", type=resolved_path)
    parser.add_argument("distances_csv_file", type=resolved_path)
    parser.add_argument("demands_directory", type=resolved_path)
    parser.add_argument("output_directory", type=resolved_path)
    return parser.parse_args()


if __name__ == "__main__":
    preprocess_ports()
