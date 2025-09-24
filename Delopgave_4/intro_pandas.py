import pandas as pd
import os
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Config:
    input_file: str = "../Data/DKHousingPricesSample100k.csv"
    plots_dir: str = "plots"
    show_plots: bool = True
    save_plots: bool = False

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
    return parser


def get_path(filepath: str) -> Path:
    """Returns the path object from an input string, this ensures compatibility across different OS paths.

    Args:
        filepath: The relative path from script directory to file

    Returns:
        The path object of the file
    """
    script_dir = Path(__file__).parent
    return script_dir / filepath

def save_plot(plot_name: str) -> None:
    """Saves the current plot to the plots directory with the given name.

    Args:
        plot_name: The name of the plot file

    Raises:
        OSError: If directory cannot be created.
    """
    plots_path = get_path(Config.plots_dir)
    plots_path.mkdir(exist_ok=True, parents=True) # raises OSError if directory cannot be created
    file_name = plot_name
    plt.savefig(plots_path / file_name)

def plot_regional_prices(regional_prices: pd.Series) -> None:
    """Plots the average housing prices by region and saves the plot as a PNG file.

     Args:
         data: A pandas Series with regions as index and average prices as values.
    """
    plt.figure()
    plt.bar(regional_prices.index, regional_prices.values)
    plt.title("Average Housing Price by Region")
    plt.xlabel("Region")
    plt.ylabel("Average Price")
    plt.tight_layout()
    plt.show()

    if Config.save_plots:
        file_name = "average_price_by_region.png"
        save_plot(file_name)
    if Config.show_plots:
        plt.show()


def plot_home_types(home_types: pd.Series) -> None:
    """Plots the distribution of house types and saves the plot as a PNG file.

     Args:
         home_types: A pandas Series with house types as index and their counts as values.
    """
    plt.figure()
    plt.bar(home_types.index, home_types.values)
    plt.title("Distribution of House Types")
    plt.ylabel("")
    plt.tight_layout()

    if Config.save_plots:
        file_name = "house_type_distribution.png"
        save_plot(file_name)
    if Config.show_plots:
        plt.show()

def main() -> None:
    

if __name__ == "__main__":
    parser = setup_parser(Config())

    args = parser.parse_args()
    file_path = args.input_file
    df = pd.read_csv(file_path)

    regional_prices = df.groupby("region")["purchase_price"].mean()
    plot_regional_prices(regional_prices)
    print(regional_prices)


    home_types = df["house_type"].value_counts()
    plot_home_types(home_types)
    print(home_types)
    

    
    

    
    

