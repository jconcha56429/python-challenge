import os
import csv
import pandas as pd 
import numpy as np
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

qq = np.unique(candidate) # find candidate names
# print(qq)
totalvotes = len(id) # find total votes 
Kahn = candidate.count("Khan") # find how many voted for Kahn
Correy = candidate.count("Correy") # find how many voted for Correy
Li = candidate.count("Li") # find how many voted for Li
Otooley = candidate.count("O'Tooley") # find how many voted for O'tooley
# find percentage of people that voted for:
Kpercent = "{:.2%}".format(Kahn/totalvotes)  
Cpercent = "{:.2%}".format(Correy/totalvotes) 
Lpercent = "{:.2%}".format(Li/totalvotes) 
Opercent = "{:.2%}".format(Otooley/totalvotes) 

# finishing touches 

results = ("Election Results\n""-----------------------\n"f"Total Votes: {totalvotes}\n""-----------------------\n"f"Kahn: {Kpercent}({Kahn})")
results_output=os.path.join("PyPoll_results.txt")
with open(results_output,"w") as txt_file:
    for result in results:
        txt_file.write(str(result))
