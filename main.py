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
    # This is the generated report for summary statistics and visualization for [nba-teams-2017.csv](https://github.com/nogibjj/706_Project1_YL/blob/main/nba-teams-2017.csv).
    ## Descriptive statistics 

    {summary.to_markdown()} 

    ## Here are some plots to visualize relations between the important variables described in README. 
    ### Histogram for Cumulative Points for all the teams during the season 
     ![Alt text](figures/points_hist.png) 
     ### Scatterplot for number of games won versus cumulative points for all teams during the season 
     ![Alt text](figures/scatter.png)
    '''

    file_path = "./report.md"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(string)