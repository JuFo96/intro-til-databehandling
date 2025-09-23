import argparse
import numpy as np
import os

def read_csv(filepath: str) -> list[list[str]]:
    """Reads a csv file and returns its content as a numpy array."""
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("The file must be a .csv file.")
        with open(filepath, "r") as file:
            return [line.split(",") for line in file.read().strip().split("\n")]
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except IOError as ioe:
        print(f"I/O Error: {ioe}")

def write_csv(data: list[list[str]], dirpath: str) -> None:
    """Writes a list of lists to a csv file."""
    try:
        if not os.path.exists(dirpath):
            os.makedirs(dirpath) 
        with open(os.path.join(dirpath, "output_data.csv"), "w") as file:
            for row in data:
                file.write(",".join(row) + "\n")
    except IOError as ioe:
        print(f"I/O Error: {ioe}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Reader for Data Migration")
    parser.add_argument("--file", type=str, default="Data/source_data.csv")
    parser.add_argument("--outdir", type=str, default="logs")
    args = parser.parse_args()
    FILE_PATH = args.file
    file_lines = read_csv(FILE_PATH)
    write_csv(file_lines, args.outdir)
    print(file_lines)