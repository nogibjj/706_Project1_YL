import pandas as pd
import lib

def run_summary(data_):
    return lib.lib_describe(data_)

def run_scatter(data_):
    return lib.build_scatterplot(data_)

def run_histogram(data_):
    return lib.build_histogram(data_)

if __name__ == "__main__":
    nba = pd.read_csv("nba-teams-2017.csv")
    summary = run_summary(data_=nba)
    run_scatter(nba)
    run_histogram(nba)