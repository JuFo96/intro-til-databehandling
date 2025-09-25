# Python Introduction at Specialisterne Academy
The repository contains four Python assignments demonstrating file handling, data wrangling, and visualization skills with clean, well-documented code.

## Description
The repository contains 4 scripts corresponding to the four assignments given in the [project description](./python-intro.pdf)

- `Delopgave_1/intro_to_python.py` - File reading
- `Delopgave_2/logfile_analysis.py` - File parsing and writing  
- `Delopgave_3/error_handling.py` - Error handling
- `Delopgave_4/intro_pandas.py` - Data wrangling and visualisation
 

## Getting Started

### Dependencies
- Python >= 3.10
- matplotlib >= 3.10.6
- pandas >= 2.3.2


### Installing
The project can be cloned from github with the following command.
```bash
git clone https://github.com/JuFo96/intro-til-databehandling.git
cd intro-til-databehandling
```
#### Option 1: [uv](https://docs.astral.sh/uv/getting-started/installation/) (modern Python package manager)

```bash 
uv sync 
```
#### Option 2: venv and pip
```bash
python -m venv .venv
source .venv/bin/activate # .venv/Scripts/activate.ps1 on Windows
pip install -r requirements.txt
```
## Running the program
The scripts accept a couple of optional command line arguments to modify their behaviour
```bash
uv run Delopgave_1/intro_to_python.py --count --input Data/Navneliste.txt
```
prints the count of each letter in the file "Data/Navneliste.txt"


### Command line arguements
Each script can be supplied with the --help flag
```bash
uv run Delopgave_3/error_handling.py --help
```
which gives the following output
```bash
usage: error_handling.py [-h] [-i INPUT_FILE] [-o OUTPUT_FILE_NAME] [-d] [-v]

File Reader for Data Migration

options:
  -h, --help            show this help message and exit
  -i, --input-file INPUT_FILE
                        (default: ../Data/source_data.csv)
  -o, --output-file-name OUTPUT_FILE_NAME
                        (default: output_data.csv)
  -d, --drop-rows       drops rows containing invalid ids and rows containing empty values
  -v, --verbose         prints contents of the csv to the terminal
```
## Author
Julius Foverskov: julius.foverskov@specialisterne.dk