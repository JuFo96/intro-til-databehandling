from pathlib import Path
import argparse
import os


def read_names(filepath: Path) -> list[str]:
    """Reads a file containing names separated by commas and returns a list of names.
    
    Args:
        filepath: The Path object pointing to the file containing comma-separated names.
        
    Returns:
        A list of cleaned, lowercase names with whitespace stripped.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file is empty or contains no valid names.
        IOError: If there are issues reading the file.
    """
    if not filepath.exists():
        raise FileNotFoundError(f"File not found at: {filepath}")
    if not filepath.is_file():
        raise ValueError(f"Path is not a file: {filepath}")
    if not os.access(filepath, os.R_OK):
        raise IOError(f"No read permissions for file: {filepath}")
    
    with open(filepath, "r") as file:
        file_content = file.read().strip()

    if not file_content:
        raise ValueError(f"File is empty: {filepath}")
    
    list_of_names = file_content.lower().split(",")
    # Removes whitespace around individual names
    stripped_list_of_names = [name.strip() for name in list_of_names]

    return stripped_list_of_names


def count_letters_in_names(names: list[str]) -> dict[str, int]:
    """Counts the occurrences of each letter in the list of names.
    
    Args:
        names: A list of name strings
        
    Returns:
        A dictionary mapping each letter to its count across all names.
        
    Raises:
        ValueError: If the names list is empty.
    """
    if not names:
        raise ValueError(f"names list can't be empty")
    letter_count = {}
    for name in names:
        for letter in name:
            if letter.isalpha(): 
                letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count


def get_data_file_path(filepath: str) -> Path:
    """Returns the path object of the data

    Args:
        filepath: The relative path from project root directory to the data file

    Returns:
        The path object of the data path
    """
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    return project_root / filepath
    

def main() -> int:
    parser = argparse.ArgumentParser(description="Process names from a file")
    parser.add_argument("-c", "--count", action="store_true", 
                       help="show character count")
    parser.add_argument("-a", "--alphabetical", action="store_true", 
                       help="show names sorted alphabetically")
    parser.add_argument("-l", "--length", action="store_true", 
                       help="show names sorted by length")
    parser.add_argument("-f", "--file", type=str, default="Data/Navneliste.txt",
                       help="relative path from project root to the file containing names")
    
    # Extract commandline arguments as booleans
    args = parser.parse_args()

    try:
        DATA_PATH = get_data_file_path(args.file)
        list_of_names = read_names(DATA_PATH)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except IOError as e:
        print(f"Error: {e}")
        print(f"File permissions of {DATA_PATH} ")
        print(f"Read: {os.access(DATA_PATH, os.R_OK)}, Write: {os.access(DATA_PATH, os.W_OK)}, Execute: {os.access(DATA_PATH, os.X_OK)}")
        return 1
    
    if args.count:
        print("Number of occurences of alphabetical characters")
        sorted_dict = count_letters_in_names(sorted(list_of_names))
        print(sorted_dict)
    if args.alphabetical:
        print("List of names sorted alphabetically")
        print(sorted(list_of_names))
    if args.length:
        print("List of names sorted by length")
        print(sorted(list_of_names, key=len))

    return 0


if __name__ == "__main__":
    main()



