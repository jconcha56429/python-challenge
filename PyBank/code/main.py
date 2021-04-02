# module import
import os
import csv
# set path 
file = "OneDrive/Desktop/python-challenge/PyBank/Resources/budget_data.csv"
# list for data 
Date=[]
profitloss=[]
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # add dates to list
        Date.append(row[0]) 
        
        
        # add profit loss to list 
        profitloss.append(row[1])
        
#finishing touches
datelength = len(Date)
print(f"Total Months: {datelength}")
