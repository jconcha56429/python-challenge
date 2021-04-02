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
    for row in csvreader:
        # add dates to list
        Date.append(row[0]) 
        
        
        # add profit loss to list 
        profitloss.append(row[1])

        
        
#finishing touches
datelength = len(Date)
print(f"Total Months: {datelength}")
