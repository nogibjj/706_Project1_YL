import pandas as pd
from main import run_summary, run_scatter, run_histogram

nba = pd.read_csv("nba-teams-2017.csv")

def test_main():
    run_summary(data_=nba)
    run_scatter(data_=nba)
    run_histogram(data_=nba)