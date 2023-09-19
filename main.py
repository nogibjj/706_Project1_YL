import pandas as pd
import lib

def run_summary(data_):
    return lib.lib_describe(data_)

def run_scatter(data_):
    return lib.build_scatterplot(data_)

def run_histogram(data_):
    return lib.build_histogram(data_)

if __name__ == "__main__":
    nba = pd.read_csv("nba-teams-2017.csv")
    summary = run_summary(data_=nba)
    run_scatter(nba)
    run_histogram(nba)

    string = f'''
    ## Descriptive statistics 
    {summary.to_markdown()} 
    ### Histogram for Cumulative Points
     ![Alt text](figures/points_hist.png) 
     ### Scatterplot for games won versus cumulative points 
     ![Alt text](figures/scatter.png)
    '''

    file_path = "./report.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(string)