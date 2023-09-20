from lib import readfile, lib_describe, build_histogram, build_scatterplot
import pandas as pd


def test_main():
    nba = readfile("nba-teams-2017.csv")
    lib_describe(nba)
    build_histogram(nba)
    build_scatterplot(nba)

    assert isinstance(lib_describe(nba), pd.DataFrame)