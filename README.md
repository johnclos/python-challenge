# Python Homework - Py Me Up, Charlie

## PYBANK EXERCISE
# it first imports the needed libraries.
# it then creates the needed integers, strings, dictionaries and lists.
# Next, it creates the path to collect data from the Resources folder, opens it and reads it in.
# After read the first row as a header, it loops through the data to:
  # The net total amount of "Profit/Losses" over the entire period
  # find the current row value and the difference and then store the current value as the previous value        
  # The greatest increase in profits (date and amount) over the entire period
  # The greatest decrease in losses (date and amount) over the entire period
  # The total number of months included in the dataset
  # The average of the changes in "Profit/Losses" over the entire period
# It then prints the summary to the screen and creates the text file with the same


## PYPOLL EXERCISE
# Your task is to create a Python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
# As an example, your analysis should look similar to the one below:
    # Financial Analysis
    #----------------------------
    # Total Months: 86
    # Total: $38382578
    # Average  Change: $-2315.12
    # Greatest Increase in Profits: Feb-2012 ($1926159)
    # Greatest Decrease in Profits: Sep-2013 ($-2196167)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv
import numpy as np


months = 0
total = 0
line = 0
rowvalue1 = 0
rowvalue2 = 0
SumAvgChg = 0
Diff = 0
GreatInc = -1000000000
GreatDec = 1000000000
AvgChg = 0
DivAvgChg = 0       
firstvalue = 0
line_val_times = 0

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #headline = lst.next()
    header = next(csvreader)
 
    # Loop through the data
    for row in csvreader:
        rowvalue = row[1]
        
        # The net total amount of "Profit/Losses" over the entire period
        total = np.add(total, float(rowvalue))

        #find the current row value and the difference and then store the current value as the previous value        
        rowvalue1 = row[1]
        Diff = np.subtract(float(rowvalue1), float(rowvalue2))
        rowvalue2 = rowvalue1
        
        # The greatest increase in profits (date and amount) over the entire period
        if Diff > GreatInc:
            GreatInc = Diff
            GreatIncDate = row[0]
        else:
            GreatInc = GreatInc

        # The greatest decrease in losses (date and amount) over the entire period
        if Diff < GreatDec:
            GreatDec = Diff
            GreatDecDate = row[0]
        else:
            GreatDec = GreatDec

        # The total number of months included in the dataset
        months = np.add(months, 1)
        
        line_value = float(row[1])
        if line_value != 0 and line_val_times < 1:
            firstvalue = row[1]
            line_val_times = np.add(line_val_times, 1)
        else:
            firstvalue = firstvalue
 
        # The average of the changes in "Profit/Losses" over the entire period
        SumAvgChg = np.subtract(float(rowvalue2), float(firstvalue))
        DivAvgChg = np.subtract(months, 1)
        AvgChg = np.divide(SumAvgChg, DivAvgChg)

# print it out

#print(PyBankSummary)

# create the text file

#save the data to the text file

