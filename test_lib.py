import pandas as pd
from lib import readfile, lib_describe, build_histogram, build_scatterplot

csv_dir = "nba-teams-2017.csv"


def test_readfile():
    nba = readfile(csv_dir)
    assert isinstance(nba, pd.DataFrame)
    assert nba.shape[0] == 30

def test_describe():
    nba = readfile(csv_dir)
    assert lib_describe(nba) is not None
    assert lib_describe(nba).shape == (8, 26)


def test_histogram():
    nba = readfile(csv_dir)
    assert build_histogram(nba) is not None


def test_scatter():
    nba = readfile(csv_dir)
    assert build_scatterplot(nba) is not None