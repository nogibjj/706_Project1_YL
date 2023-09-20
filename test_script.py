from lib import readfile, lib_describe, build_histogram, build_scatterplot


def test_main():
    nba = readfile("nba-teams-2017.csv")
    lib_describe(nba)
    build_histogram(nba)
    build_scatterplot(nba)

    assert "count" in lib_describe(nba)
    assert "mean" in lib_describe(nba)
    assert "std" in lib_describe(nba)
    assert "min" in lib_describe(nba)
    assert "max" in lib_describe(nba)