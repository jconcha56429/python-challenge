import os
import csv
import pandas as pd 

# set path 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("..","Resources", "election_data.csv")
        
id = []
candidate = []
county = []

# id, county, candidate 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Final product
print(f"Total Number of Votes: {totalvotes}")