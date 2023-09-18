# import pandas as pd
from lib import readfile, lib_describe, build_pairplot, build_scatterplot

csv_dir = "nba-teams-2017.csv"

nba = readfile(file=csv_dir)

def test_describe():
    data = nba
    lib_describe(data)


def test_pairplot():
    build_pairplot(nba)

def test_scatter():
    build_scatterplot(nba)