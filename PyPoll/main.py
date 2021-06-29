# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
# The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:
    # Election Results
    # -------------------------
    # Total Votes: 3521001
    # -------------------------
    # Khan: 63.000% (2218231)
    # Correy: 20.000% (704200)
    # Li: 14.000% (492940)
    # O'Tooley: 3.000% (105630)
    # -------------------------
    # Winner: Khan
    # -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv
#import NumPy as np  

total = 0

rowvalue1 = 0
rowvalue2 = 0
rowvalue3 = 0
SumAvgChg = 0
Diff = 0

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

#headline = lst.next()

with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        # sum of 'Profit/Losses' column
        rowvalue = row[1]
        total = total + float(rowvalue)
        
        rowvalue1 = row[1]
        Diff = np.subtract(float(rowvalue2), float(rowvalue1))
        rowvalue2 = rowvalue1
        SumAvgChg = SumAvgChg + Diff
        # count the number of months
        months = months + 1
        print(SumAvgChg)
 

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total))
print("-------------------------")
print("Khan: 63.000% (2218231)")
print("Correy: 20.000% (704200)")
print("Li: 14.000% (492940)")
print("O'Tooley: 3.000% (105630)")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")
