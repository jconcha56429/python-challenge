# module import
import os
import csv
import pandas as pd 
import numpy as np
# set path 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("..", "Resources", "budget_data.csv")
# list for data 
Date=[]
profitloss=[]

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        # add dates to list
        Date.append(row[0]) 
        # add profits to list 
        profitloss.append(int(row[1]))
       
#finishing touches
# Present total number of months
datelength = len(Date)
print(f"Total Months: {datelength}")
# Present sum of profitloss
total = sum(profitloss)
print(f"Total profit/loss: ${total}")
# determine values from one row of profit loss to the next
change = [j-i for i, j in zip(profitloss[:-1], profitloss[1:])] # all except the first one minus all except the last one 
# Present average change from one period to another
averagechange = sum(change) / len(change)
rounded = round(averagechange,2)
print(f"Average profit/loss change: ${rounded}")
minimum = min(change)
maximum = max(change)
print(minimum)
print(maximum)

final = len(change) # there are 85 total changes from one date to another 
print(final)
final2 = len(Date)  # there are 86 dates total 
print(final2)
# print(maximum) 
# index +/-1 to get the value 
index = change.index(-2196167) # find row 43 + 1 (because there are only 85 changes) in changes to be the minimum change in a year 
print(index)
index2 = change.index(1926159) #find row 24 + 1 in changes to be the maximum change in a year 
print(index2)
for x in range(len(Date)): # locate corresponding dates to changes 
    print(x,end = " ")
    print(Date[x])
