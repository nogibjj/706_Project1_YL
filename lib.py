import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def readfile(file):
    """read the nba-teams-2017.csv"""
    df = pd.read_csv(file)
    return df


def lib_describe(df):
    """output the summary for the data"""
    return df.describe()


# visualization 1
def build_histogram(df):
    plt.hist(df["points"], bins=35, edgecolor="k")
    plt.xlabel("Points")
    plt.ylabel("Frequency")
    plt.title("Frequency distribution of Points across Teams")
    plt.show()
    plt.savefig("figures/points_hist.png")
    return


# visualization 2
def build_scatterplot(df):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x=df["wins"], y=df["points"], s=60, alpha=0.7, edgecolors="k")
    a, b = np.polyfit(df["wins"], df["points"], deg=1)
    xseq = np.linspace(0, 80, num=100)
    ax.plot(xseq, b + a * xseq, color="k", lw=2.5)
    ax.set_xlabel("Wins")
    ax.set_ylabel("Points")
    ax.set_xlim(15, 70)
    ax.set_ylim(90, 120)
    fig.show()
    plt.savefig("figures/scatter.png")
    return
