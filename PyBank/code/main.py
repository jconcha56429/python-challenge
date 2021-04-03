# module import
import os
import csv
print(os.getcwd())
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
NewDate = Date[1:]
datelength = len(NewDate)
print(f"Total Months: {datelength}")
# Present sum of profitloss
total = sum(profitloss)
print(total)


