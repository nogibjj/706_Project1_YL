from lib import readfile, lib_describe, build_histogram, build_scatterplot


def test_main():
    nba = readfile("nba-teams-2017.csv")
    lib_describe(nba)
    build_histogram(nba)
    build_scatterplot(nba)


if __name__ == "__main__":
    test_main()
