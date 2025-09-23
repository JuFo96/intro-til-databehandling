import pandas as pd
import os
import argparse
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pandas CSV Reader")
    parser.add_argument("--file", type=str, default="Data/DKHousingPricesSample100k.csv")
    parser.add_argument("--outdir", type=str, default="plots")
    args = parser.parse_args()
    FILE_PATH = args.file
    df = pd.read_csv(FILE_PATH)
    print(df.columns)
    #print(df.head(10))
    # Groups
    regional_prices = df.groupby("region")["purchase_price"].mean()
    print(regional_prices)
    home_types = df["house_type"].value_counts()
    print(home_types)
    
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    
    plt.figure()
    regional_prices.plot(kind="bar")
    plt.title("Average Housing Price by Region")
    plt.xlabel("Region")
    plt.ylabel("Average Price")
    plt.tight_layout()
    plt.savefig("plots/average_price_by_region.png")

    plt.figure()
    home_types.plot(kind="bar")
    plt.title("Distribution of House Types")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("plots/house_type_distribution.png")