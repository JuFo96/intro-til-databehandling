import pandas as pd
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Config:
    input_file: str = "../Data/DKHousingPricesSample100k.csv"
    plots_dir: str = "../plots/"
    show_plots: bool = True
    save_plots: bool = False
    verbose: bool = False

def setup_parser(config: Config) -> argparse.ArgumentParser:
    """Sets up the argument parser with the given configuration.

    Args:
        config: A Config dataclass instance containing default values.

    Returns:
        An argparse.ArgumentParser object with the configured arguments.
    """
    parser = argparse.ArgumentParser(description="Pandas CSV Reader")
    parser.add_argument("-i", "--input-file", type=str, default=config.input_file, help="(default: {config.input_file})")
    parser.add_argument("-o", "--output-directory", type=str, default=config.plots_dir, help="(default: {config.output_file})")
    parser.add_argument("-s", "--show-plots", action="store_true", help="shows the plots in a window")
    parser.add_argument("--save-plots", action="store_true", help="saves the plots as PNG files in the output directory")
    parser.add_argument("-v", "--verbose", action="store_true", help="prints contents of the dataseries to the terminal")
    return parser


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

def save_plot(plot_name: str, config: Config) -> None:
    """Saves the current plot to the plots directory with the given name.

    Args:
        plot_name: The name of the plot file
        config: A Config dataclass instance containing boolean flags for showing and saving plots.

    Raises:
        OSError: If directory cannot be created.
    """
    plots_path = get_path(config.plots_dir)
    plots_path.mkdir(exist_ok=True, parents=True) # raises OSError if directory cannot be created
    
    print(f"Saving plot as {plot_name} in {plots_path}")
    plt.savefig(plots_path / plot_name)

def plot_regional_prices(regional_prices: pd.Series, config: Config) -> None:
    """Plots the average housing prices by region and saves the plot as a PNG file.

     Args:
         data: A pandas Series with regions as index and average prices as values.
         config: A Config dataclass instance containing boolean flags for showing and saving plots.
    """
    plt.figure()
    plt.bar(regional_prices.index, regional_prices.values)
    plt.title("Average Housing Price by Region")
    plt.xlabel("Region")
    plt.ylabel("Average Price")
    plt.tight_layout()
    plt.show()

    if config.save_plots:
        file_name = "average_price_by_region.png"
        save_plot(file_name, config)
    if config.show_plots:
        plt.show()


def plot_home_types(home_types: pd.Series, config: Config) -> None:
    """Plots the distribution of house types and saves the plot as a PNG file.

     Args:
         home_types: A pandas Series with house types as index and their counts as values.
         config: A Config dataclass instance containing boolean flags for showing and saving plots.
    """
    plt.figure()
    plt.bar(home_types.index, home_types.values)
    plt.title("Distribution of House Types")
    plt.ylabel("")
    plt.tight_layout()

    if config.save_plots:
        file_name = "house_type_distribution.png"
        save_plot(file_name, config)
    if config.show_plots:
        plt.show()

def main() -> None:
    parser = setup_parser(Config())
    args = parser.parse_args()
    config = Config(
        input_file=args.input_file,
        plots_dir=args.output_directory,
        show_plots=args.show_plots,
        save_plots=args.save_plots,
        verbose=args.verbose
    )
    
    try:
        file_path = get_path(config.input_file)
        df = pd.read_csv(file_path)

        regional_prices = df.groupby("region")["purchase_price"].mean()
        plot_regional_prices(regional_prices, config)
        if config.verbose:
            print(regional_prices)

        home_types = df["house_type"].value_counts()
        plot_home_types(home_types, config)
        if config.verbose:
            print(home_types)
        
        print(f"Successfully read and processed csv file: {file_path}")

    except OSError as e:
        print(f"Error reading file: {e}")
        print("Check write permissions")
    
if __name__ == "__main__":
    main()