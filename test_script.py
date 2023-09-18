from lib import readfile, lib_describe, build_pairplot, build_scatterplot

def test_main():
    nba = readfile("nba-teams-2017.csv")
    lib_describe(nba)
    build_pairplot(nba)
    build_scatterplot(nba)

if __name__ == "__main__":
    test_main()