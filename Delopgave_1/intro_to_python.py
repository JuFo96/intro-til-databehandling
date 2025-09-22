def read_names(filepath: str) -> list[str]:
    """Reads a file containing names separated by commas and returns a list of names."""
    with open(filepath, "r") as file:
        names = file.readlines()[0].strip().lower().split(",")
    return names
        
def sort_names_alphabetically(names: list[str]) -> list[str]:
    """Sorts a list of names alphabetically."""
    return sorted(names)

def sort_names_length(names: list[str]) -> list[str]:
    """Sorts a list of names by their length."""
    return sorted(names, key=len)

def count_letters_in_names(names: list[str]) -> dict[str, int]:
    """Counts the occurrences of each letter in the list of names."""
    letter_count = {}
    for name in names:
        for letter in name:
            if letter.isalpha(): 
                letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count


if __name__ == "__main__":
    FILE_PATH = "../Data/Navneliste.txt"
    list_of_names = read_names(FILE_PATH)
    sorted_list_of_names = sort_names_alphabetically(list_of_names)
    print(count_letters_in_names(sorted_list_of_names))


