import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def readfile(file):
    '''read the nba-teams-2017.csv'''
    df = pd.read_csv(file)
    return df

def lib_describe(df):
    '''output the summary for the data'''
    return df.describe()

# visualization 1
def build_pairplot(df):
    return sns.pairplot(df)

# visualization 2
def build_scatterplot(df):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x=df["wins"], y=df["points"], s=60, alpha=0.7, edgecolors="k")
    
    a, b = np.polyfit(df["wins"], df["points"], deg=1)
    xseq = np.linspace(0, 80, num=100)
    ax.plot(xseq, b+a*xseq, color="k", lw=2.5)
    ax.set_xlabel("Wins")
    ax.set_ylabel("Points")
    plt.show()
    return