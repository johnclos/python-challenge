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
from collections import Counter
from collections import defaultdict

r = 0
candidate_list = []
cand_lst_len = 0
total = 0
candidate1 = str
vote_cand_dict = {}
vote_cand_perc_list = []
vote_cand_perc =  "{:.3%}".format(0.0)
winner = str
vote_cand_values = []
vote_cand_keys = []
vote_cand_print = str
vote_cand_summary = []

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

#headline = lst.next()
# csvrow2 = [row[2] for row in csvreader]
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    header = next(csvreader)

    # get the candidate column only
    
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
        
        # get the number of candidates
        cand_lst_len = len(candidate_list)

        # The total number of votes each candidate won
        # every time we come across a new name not already in dictionary, add a new key for the candidates name
        if candidate1 not in vote_cand_dict.keys():
            vote_cand_dict[candidate1] = 1
        #if they are in the dictionary, increase their vote count by one
        else:
            vote_cand_dict[candidate1] += 1

# loop through the values and convert then to percent
for x in vote_cand_dict.values():
    #calculate the percent of the total votes that each candidate received
    vote_cand_perc = ("{:.3%}".format(x/total))
    vote_cand_perc_list.append(vote_cand_perc)

# create a list of the votes
vote_cand_values = list(vote_cand_dict.values())
# create a list of the candidates
vote_cand_keys = list(vote_cand_dict.keys())

#find the maximum num of votes
m = max(vote_cand_values)

# find the index for the winner based on the maximum number of votes
winner = vote_cand_values.index(m)

print ("Election Results")
print("-------------------------")
print("Total Votes: " + str(total))
print("-------------------------")
# loop through the candidates and print their name, their vote percent and their number of votes
for i in range(cand_lst_len):
    print(f'' + str(vote_cand_keys[i]) + ':  ' + str(vote_cand_perc_list[i]) + ' (' + str(vote_cand_values[i]) + ')')
    vote_cand_print = (f'' + str(vote_cand_keys[i]) + ':  ' + str(vote_cand_perc_list[i]) + ' (' + str(vote_cand_values[i]) + ')')
    vote_cand_summary.append(vote_cand_print)

print("-------------------------")
print(f'Winner: ' + vote_cand_keys[winner])
print("-------------------------")

# create the text file
PyPollSummary = ["Election Results",
    "-------------------------",
    "Total Votes: " + str(total),
    "-------------------------",]
for i in range(cand_lst_len):
    PyPollSummary.append(vote_cand_summary[i])
PyPollSummary.extend(   
    ["-------------------------",
    f'Winner: ' + vote_cand_keys[winner],
    "-------------------------"])

open("PyPollSummary.txt", "w")
# save the data to the text file
with open("PyPollSummary.txt", "w") as txt_file:
    for line in PyPollSummary:
        txt_file.write(line + "\n")
