import argparse
import os
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    input_file: str = "../Data/source_data.csv"
    logs_dir: str = "../logs/Delopgave_3"
    output_file: str = "output_data.csv"
    drop_rows: bool = False
    verbose: bool = False

def read_csv(filepath: Path) -> list[list[str]]:
    """Reads a csv file and returns its content as a list of lists of strings.
    
    Args:
        filepath: The Path object pointing to the file containing log files.
        
    Returns: 
        A list of lists of strings.

    Raises:
        FileNotFoundError: If the file does not exist at the given path
        ValueError: If the given path is not a csv file or the csv file is empty.
        OSError: If there are no read permissions for the file.
    """
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found at: {filepath}")
    if not filepath.is_file():
        raise ValueError(f"Path is not a file: {filepath}")
    if not os.access(filepath, os.R_OK):
        raise OSError(f"No read permissions for file: {filepath}")
    if not filepath.suffix == ".csv":
        raise ValueError(f"File is not a .csv file: {filepath}")

    with open(filepath, "r") as file:
        # Double list comprehension to split lines by newline and then by comma finally stripping whitespace from each element in the csv file
        file_contents = [[element.strip() for element in line.split(",")] for line in file.read().split("\n")]

    if not file_contents:
        raise ValueError(f"File is empty: {filepath}")

    return file_contents

def drop_empty_rows(data: list[list[str]]) -> list[list[str]]:
    """Removes rows that contains any empty strings
    
    Args:
        data: a list of lists of strings
        
    Returns:
        A list of lists of strings with no empty strings in any row
    
    Raises:
        ValueError: If the data list is empty."""
    
    if not data:
        raise ValueError(f"Data can't be empty")
    data = [row for row in data if "" not in row]
    return data

def drop_invalid_id(data: list[list[str]]) -> list[list[str]]:
    """Removes rows where the first element is either negative or a nan value, the function skips the first row of data.
    
    Args:
        data: a list of lists of strings
         
    Returns:
        A list of lists of strings with no invalid ids in the first column

    Raises:
        ValueError: If the data list is empty."""
    
    if not data:
        raise ValueError(f"Data can't be empty")
    
    # Skips the header row, row[0] corresponds to the customer_id
    data = [row for row in data[1:] if row[0].isdigit()]
    return data

def write_csv(data: list[list[str]], file_output_name) -> None:
    """Writes a list of lists to a csv file.
    
    Args:
        data: a list of lists of strings

    Raises:
        OSError: If the directory can't be created.
    """
    
    # Checks if there is a "logs" directory in the project root directory, if not it creates one
    logs_dir = get_path("../logs/Delopgave_3")
    logs_dir.mkdir(exist_ok=True, parents=True) # raises OSError if directory cannot be created
    file_name = file_output_name

    with open(logs_dir / file_name, "w") as file:
        for row in data:
            file.write(",".join(row) + "\n") # Concatenates list elements with commas and adds a newline


def get_path(filepath: str) -> Path:
    """Returns the path object from an input string, this ensures compatibility across different OS paths.

    Args:
        filepath: The relative path from script directory to file

    Returns:
        The path object of the file
    """
    script_dir = Path(__file__).parent
    return script_dir / filepath


def setup_parser(config: Config) -> argparse.ArgumentParser:
    """Sets up the argument parser with the given configuration.

    Args:
        config: A Config dataclass instance containing default values.

    Returns:
        An argparse.ArgumentParser object with the configured arguments.
    """
    parser = argparse.ArgumentParser(description="File Reader for Data Migration")
    parser.add_argument("-i", "--input-file", type=str, default=config.input_file)
    parser.add_argument("-o", "--output-file", type=str, default=config.output_file)
    parser.add_argument("-d", "--drop-rows", action="store_true", help="drops rows containing invalid ids and rows containing empty values") 
    parser.add_argument("-v", "--verbose", action="store_true", help="prints contents of the csv to the terminal")
    return parser


def main():
    config = Config()
    parser = setup_parser(config)

    # Extract command line arguments
    args = parser.parse_args()
    
    try:
        file_path = get_path(args.input_file)
        file_content = read_csv(file_path)

        if args.drop_rows:
            file_content = drop_empty_rows(file_content)
            file_content = drop_invalid_id(file_content)
        
        if args.verbose:
            print(file_content)
    
        write_csv(file_content, args.output_file)
        print(f"Successfully read and wrote csv file to directory: {config.logs_dir}")

    except ValueError as ve:
        print(f"ValueError: {ve}")

    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
               
    except OSError as ose:
        print(f"OSError: {ose}")
        print(f"File permissions of input file: {file_path}")
        print(f"Read: {os.access(file_path, os.R_OK)}, Write: {os.access(file_path, os.W_OK)}")
        print(f"Output permissions {os.access(config.logs_dir, os.W_OK)}")


if __name__ == "__main__":
    main()
    
        