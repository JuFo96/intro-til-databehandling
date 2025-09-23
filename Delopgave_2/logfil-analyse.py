import os
import argparse 
from pathlib import Path


def read_file(filepath: Path) -> list[str]:
    """Reads a file log messages seperated by \n and returns a list of messages.
    
    Args:
        filepath: The Path object pointing to the file containing log files.
        
    Returns:
        A list of cleaned, log messages.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file is empty or or not a file.
        IOError: If there are issues reading the file.
    """
    if not filepath.exists():
        raise FileNotFoundError(f"File not found at: {filepath}")
    if not filepath.is_file():
        raise ValueError(f"Path is not a file: {filepath}")
    if not os.access(filepath, os.R_OK):
        raise IOError(f"No read permissions for file: {filepath}")
    
    with open(filepath, "r") as file:
        messages = [message.strip() for message in file.read().split("\n")]

    if not messages:
        raise ValueError(f"File is empty: {filepath}")
    
    return messages


def seperate_log_by_type(log: list[str]) -> dict[str, list[str]]:
    """Seperates log messages by type into a dictionary.
    
    Args:
        log: A list of log messages.

    Returns:
        A dictionary with log types as keys and lists of messages as values.
    Raises:
        ValueError: If the log list is empty.
    """
    log_dict = {"INFO": [], "WARNING": [], "ERROR": [], "SUCCESS": []}
    
    if not log:
        raise ValueError(f"log list can't be empty")
        
    for message in log:
        if "INFO" in message:
            log_dict["INFO"].append(message)
        elif "WARNING" in message:
            log_dict["WARNING"].append(message)
        elif "ERROR" in message:
            log_dict["ERROR"].append(message)
        elif "SUCCESS" in message:
            log_dict["SUCCESS"].append(message)
    return log_dict

def write_dict_to_files(data: dict[str, list[str]]) -> None:
    """Writes each key's messages in the dictionary to separate files.

    Args:
        data: A dictionary with log types as keys and lists of messages as values.

    Raises:
        ValueError: If the data dictionary is empty.
        OSError: If directory cannot be created.
    """
    if not data:
        raise ValueError("Data dictionary cannot be empty")
    
    # Checks if there is a "logs" directory in the project root directory, if not it creates one
    logs_dir = Path(__file__).parent.parent / "logs" / "Delopgave_2"
    logs_dir.mkdir(exist_ok=True, parents=True) # raises OSError if directory cannot be created

    for key, messages in data.items():
        log_file_path = logs_dir / f"{key.lower()}_log.txt"
        with open(log_file_path, "w") as file:
            for message in messages:
                file.write(f"{message}\n")


def get_data_file_path(filepath: str) -> Path:
    """Returns the path object of the data

    Args:
        filepath: The relative path from script directory to the data file

    Returns:
        The path object of the data path
    """
    script_dir = Path(__file__).parent
    return script_dir / filepath

def main() -> None:
    parser = argparse.ArgumentParser(description="Log file analysis")    
    parser.add_argument("-f", "--file", type=str, default="../Data/app_log (logfil analyse) - random.txt")
        
    # Extract commandline arguments as booleans
    args = parser.parse_args()

    try:
        LOG_PATH =  get_data_file_path(args.file)
        log_messages = read_file(LOG_PATH)
        separated_logs = seperate_log_by_type(log_messages)
        write_dict_to_files(separated_logs)
        
        print("Successfully processed log file and wrote to separate files.")

    except ValueError as ve:
        print(f"ValueError: {ve}")

    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}") 
    
    except IOError as e:
        print(f"Error: {e}")
        print(f"File permissions of {LOG_PATH}")
        print(f"Read: {os.access(LOG_PATH, os.R_OK)}, Write: {os.access(LOG_PATH, os.W_OK)}, Execute: {os.access(LOG_PATH, os.X_OK)}")
    
    except OSError as ose:
        print(f"OSError: {ose}")




    


    
    
    



if __name__ == "__main__":
    main()


