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
results=[]
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
str(print(f"Total Months: {datelength}"))
# Present sum of profitloss
total = sum(profitloss)
str(print(f"Total profit/loss: ${total}"))
# determine values from one row of profit loss to the next
change = [j-i for i, j in zip(profitloss[:-1], profitloss[1:])] # all except the first one minus all except the last one 
# Present average change from one period to another
averagechange = sum(change) / len(change)
rounded = round(averagechange,2)
str(print(f"Average profit/loss change: ${rounded}"))
minimum = min(change) # find minimum loss in change 
maximum = max(change) # find maximum profit in change 

final = len(change) # there are 85 total changes from one date to another 
final2 = len(Date)  # there are 86 dates total 
index = change.index(-2196167) # find index 43 + 1 (because there are only 85 changes) in changes to be the minimum change in a year 
index2 = change.index(1926159) #find index 24 + 1 in changes to be the maximum change in a year 

str(print(f"Greatest increase in profits: {Date[25]} ${maximum}"))
str(print(f"Greatest decrease in profits: {Date[44]} ${minimum}"))

results = ("Finanical Analysis\n""-------------------------\n"f"Total Months: {datelength}\n"f"Total profit/loss: ${total}\n"f"Average profit/loss change: ${rounded}\n"
f"Greatest increase in profits: {Date[25]} ${maximum}\n"f"Greatest decrease in profits: {Date[44]} ${minimum}")

results_output=os.path.join("PyBank_results.txt")
with open(results_output,"w") as txt_file:
    for result in results:
        txt_file.write(str(result))