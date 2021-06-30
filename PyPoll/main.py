# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns:
        # Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes 
        # and calculates each of the following:
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
import pandas as pd  

r = 0
candidate_list = []
cand_lst_len = 0
total = 0
candidate1 = 'a'
# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

#headline = lst.next()

with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    header = next(csvreader)

    # get the first candidate
    
    # Loop through the data
    for row in csvreader:
        # The total number of votes cast
        total = total + 1

        # A complete list of candidates who received votes
        candidate1 = row[2]
        if candidate1 not in candidate_list:
            candidate_list.append(row[2])
        else:
            r = 1
        
        cand_lst_len = len(candidate_list)
        # The percentage of votes each candidate won


        # The total number of votes each candidate won


        # The winner of the election based on popular vote.


print ("Election Results")
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


print(candidate_list)
print(cand_lst_len)

# create the text file
PyPollSummary = ["Election Results",
    "-------------------------",
    "-------------------------"
    ]
print (PyPollSummary)

open("PyPollSummary.txt", "w")
# save the data to the text file
with open("PyPollSummary.txt", "w") as txt_file:
    for line in PyPollSummary:
        txt_file.write(line + "\n")


# close the text file
#PyPollSummary.close()
