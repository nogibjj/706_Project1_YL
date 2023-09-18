[![Format](https://github.com/nogibjj/706_Project1_YL/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/706_Project1_YL/actions/workflows/format.yml)

[![Install](https://github.com/nogibjj/706_Project1_YL/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/706_Project1_YL/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/706_Project1_YL/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/706_Project1_YL/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/706_Project1_YL/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/706_Project1_YL/actions/workflows/test.yml)

# 706_Project_YL

This repository includes the main tasks for Project 1:

# 706_Week03_YL

This repository includes the main tasks for week 3-Polar Descriptive Statistics:

* `Makefile` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.
* `.devcontainer` includes a Dockerfile and `devcontainer.json`. The `Dockerfile` within this folder specifies how the container should be built, and other settings in this directory may control development environment configurations.
* `Workflows` includes GitHub Actions, which contain configuration files for setting up automated build, test, and deployment pipelines for your project.
* `.gitignore` is used to specify which files or directories should be excluded from version control when using Git.
* `README.md` is the instruction file for the readers.
* `main.py` is a Python file that contains the main function for summary statistics and visualization for the chosen dataset `nba-teams-2017.csv`.
* `test_main.py`  is a test file for `main.py` that can successfully run in IDEs.
* `requirements.txt` is to specify the dependencies (libraries and packages) required to run the project.
* Jupyter Notebook 
* Scripts and visualizations calculating the descriptive statistics of the chosen dataset `nba-teams-2017.csv`
* `lib.py` sharing common code between the Python script and Jupyter Notebook
* `test_script.py`
* `test_lib.py`

## Project description

The project adapts from the project template from Week 01, and add Pandas scripts to output the summary statistics and visualizations of certain features within a given dataset. I used the `nba-teams-2017.csv` dataset, a dataset describing the wins, losses and game statistics for all the NBA teams during the 2016-17 Regular Season.

* I calculated the summary statistics (mean/median/standard deviation) of the column `Price`, the log price of red wine.

* I created two visualizations: a histogram of log wine price; a pairplot of all the quantitative variables in the dataset.

## Project environment

* Use codespace for scripting
* Container built in `devcontainers` and virtual environment activated via `requirements.txt`
* To run the code, use the command `python lib.py` in the terminal

## Check format & errors

1. make format

2. make lint

3. make test

## Summary statistics

See `report.md` for details.

## Video Explanation

Link: 