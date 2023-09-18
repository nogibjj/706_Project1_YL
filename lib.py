import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def readfile(file):
    '''read the nba-teams-2017.csv'''
    df = pd.read_csv(file)
    return df

def lib_describe(df):
    '''output the summary for the data'''
    return df.describe()

# visualization 1


# visualization 2