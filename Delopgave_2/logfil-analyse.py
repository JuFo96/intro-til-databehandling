from os import path
import os
import argparse 


def read_file(filepath: str) -> list[str]:
    """Reads a file and returns its lines as a list of strings."""
    with open(filepath, "r") as file:
        messages = [message for message in file.read().strip().split("\n")]
    return messages

def seperate_log_by_type(log: list[str]) -> dict[str, list[str]]:
    """Separates log messages by their type (INFO, WARNING, ERROR)."""
    log_dict = {"INFO": [], "WARNING": [], "ERROR": [], "SUCCESS": []}
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

def write_dict_to_files(data: dict[str, list[str]], dirpath: str) -> None:
    """Writes each key's messages in the dictionary to separate files."""
    if not path.exists(dirpath):
        os.makedirs(dirpath)
    for key, messages in data.items():
        with open(path.join(dirpath, f"{key.lower()}_log.txt"), "w") as file:
            for message in messages:
                file.write(f"{message}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log file analysis")
    parser.add_argument("--file", type=str, default="../Data/app_log (logfil analyse) - random.txt")
    parser.add_argument("--outdir", type=str, default="logs")
    args = parser.parse_args()
    log_messages = read_file(args.file)
    separated_logs = seperate_log_by_type(log_messages)
    write_dict_to_files(separated_logs, args.outdir)


