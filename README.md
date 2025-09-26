# Python Introduction at Specialisterne Academy
The repository contains four Python assignments demonstrating file handling, data wrangling, and visualization skills with clean, well-documented code. The project is described in depth in the [project description](./python-intro.pdf). 

My reflections about the project can be found [here](./reflections.md) (in danish)
## Description
Each script corresponds to one part of the assignment and is structured as follows
### Scripts
- `Delopgave_1/intro_to_python.py` - File reading
- `Delopgave_2/logfile_analysis.py` - File parsing and writing  
- `Delopgave_3/error_handling.py` - Error handling
- `Delopgave_4/intro_pandas.py` - Data wrangling and visualisation
- `Delopgave_4/plots.ipynb` - Similar to `intro_pandas.py` with results shown inline in a jupyter notebook

### Output
- `intro_to_python.py` - prints results to the console, if --wordcloud flag is chosen an image is saved to `plots/`
- `logs/` - contains the default output of `logfile_analysis.py` and `error_handling.py`
- `plots/` - contains the default output of `intro_pandas.py`

## Getting Started

### Dependencies
- Python >= 3.10
- matplotlib >= 3.10.6
- pandas >= 2.3.2
- wordcloud >= 1.9.4
- ipykernel >= v6.30.1 (optional for jupyter notebooks)

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
uv run Delopgave_1/intro_to_python.py --count --input ../Data/Navneliste.txt
```
prints the count of each letter in the file "Data/Navneliste.txt", note that the path is relative to the script and not the location of the shell executing it.


### Command line arguments
Each script can be supplied with the --help flag
```bash
uv run Delopgave_3/error_handling.py --help
```
which gives will show the available command line arguments.
## Author
Julius Foverskov: julius.foverskov@specialisterne.dk