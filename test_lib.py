# import pandas as pd
from lib import readfile, lib_describe, build_histogram, build_scatterplot

csv_dir = "nba-teams-2017.csv"

nba = readfile(file=csv_dir)

def test_describe():
    data = nba
    lib_describe(data)


def test_histogram():
    build_histogram(nba)

def test_scatter():
    build_scatterplot(nba)