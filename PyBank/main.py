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

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
# Open the file
budget_data_myfile = open(budget_data_csv, "r")
# Read all the lines into a List
lst = list(budget_data_myfile.readlines())
# Close the file
budget_data_myfile.close()
# Get just the last line
lastline = lst[len(lst)-1]
# Locate the start of the label you want, 
# and set the start position at the end 
# of the label:
intStart = lastline.find('location="') + 10
# snip off a substring from the 
# target value to the end (this is called a slice):
sub = lastline[intStart:]
# Your ending marker is now the 
# ending quote (") that is located 
# at the end of your target value.
# Get it's index.
intEnd = sub.find('"')
# Finally, grab the value, using 
# another slice operation.
finalvalue = sub[0:intEnd]
print (finalvalue)
print (lastline)

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
