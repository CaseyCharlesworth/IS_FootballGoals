#s3132392 Casey-Ann Charlesworth
#Assignment 2 - Intro to Statistics
#Assignment due 23 April 2017


import pandas as pd

clubs = ["Scotland", "Germany", "England", "Greece", "Italy"]

for c in clubs:
    #import home/away goals from each file and rename
    file_a = c + "_2016_17.csv"
    file_b = c + "_2015_16.csv"
    var = ["FTHG", "FTAG"]
    a_goals = pd.read_csv(file_a,sep=",",header=0, usecols=var)
    b_goals = pd.read_csv(file_b,sep=",",header=0, usecols=var)
    #concatenate files
    frames = [a_goals, b_goals]
    result = pd.concat(frames)
    #drop NaNs and only write out 3 columns
    result.columns = [c + "_home", c + "_away"] 
    columns = [c + "_home", c + "_away"]
    result.dropna().to_csv(c + ".csv",sep=",", columns=columns, index=False, decimal=".")

print("Data preprocessing step complete")
