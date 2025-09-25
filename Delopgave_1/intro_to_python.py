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
    # Removes whitespace around individual names by looping over each name
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
            # Skips empty strings and non-alphabetical characters
            if letter.isalpha(): 
                letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count


def get_path(filepath: str) -> Path:
    """Returns the path object from an input string, this ensures compatibility across different OS paths.

    Args:
        filepath: The relative path from script directory to file

    Returns:
        The path object of the file
    """
    script_dir = Path(__file__).parent
    normalised_path = (script_dir / filepath).resolve() # resolve to get absolute path and remove any ../ or ./ parts
    return normalised_path
    
    
def main():
    parser = argparse.ArgumentParser(description="Process names from a file")
    parser.add_argument("-c", "--count", action="store_true", 
                       help="show character count")
    parser.add_argument("-a", "--alphabetical", action="store_true", 
                       help="show names sorted alphabetically")
    parser.add_argument("-l", "--length", action="store_true", 
                       help="show names sorted by length")
    parser.add_argument("-f", "--file", type=str, default="../Data/Navneliste.txt",
                       help="path to the file containing names")
    
    # Extract commandline arguments as booleans
    args = parser.parse_args()
    
    try:
        data_path = get_path(args.file)
        list_of_names = read_names(data_path)

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
        
        print(f"Successfully read names from file: {data_path}")
     
    except FileNotFoundError as e:
        print(f"Error: {e}")

    except ValueError as e:
        print(f"Error: {e}")

    except IOError as e:
        print(f"Error: {e}")
        print(f"File permissions of {data_path} ")
        print(f"Read: {os.access(data_path, os.R_OK)}, Write: {os.access(data_path, os.W_OK)}, Execute: {os.access(data_path, os.X_OK)}")

if __name__ == "__main__":
    main()



