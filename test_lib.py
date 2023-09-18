from lib import readfile, lib_describe, build_pairplot, build_scatterplot
import pandas as pd

csv_dir = "nba-teams-2017.csv"

nba = readfile(file=csv_dir)

def test_describe():
    data = nba
    res1 = lib_describe(data)
    assert res1.loc["mean", "wins"] == 41.000000	
    assert res1.loc["max", "wins"] == 67.000000
    assert res1.loc["min", "wins"] == 20.000000	
    assert res1.loc["std"] == 11.188048

def test_pairplot():
    build_pairplot(nba)

def test_scatter():
    build_scatterplot(nba)