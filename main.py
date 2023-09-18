import pandas as pd
import lib

def run_summary(data_):
    return lib.lib_describe(data_)

def run_plots(data_):
    lib.build_scatterplot(data_)
    lib.build_pairplot(data_)

if __name__ == "__main__":
    nba = pd.read_csv("nba-teams-2017.csv")
    summary = run_summary(data_=nba)
    run_plots(data_=nba)