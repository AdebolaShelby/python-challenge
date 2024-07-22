# Python-Challenge: PyBank

In this Challenge, I was tasked with creating a Python script to analyze the financial records of PyBank. I was given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

    The task is to create a Python script that analyzes the records to calculate each of the following values:

    The total number of months included in the dataset

    The net total amount of "Profit/Losses" over the entire period

    The changes in "Profit/Losses" over the entire period, and then the average of those changes

    The greatest increase in profits (date and amount) over the entire period

    The greatest decrease in profits (date and amount) over the entire period



# Python-Challenge: PyPoll
In this Challenge, I was tasked with helping a small, rural town modernize its vote-counting process.

I was given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". I was tasked with creating a Python script that analyzes the votes and calculates each of the following values:

    The total number of votes cast

    A complete list of candidates who received votes

    The percentage of votes each candidate won

    The total number of votes each candidate won

    The winner of the election based on popular vote


# Financial Analysis: PyBank
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# Election Results: PyPoll
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------




# PyBank_Challenge

import os and csv
create csv path

print the initial text
'Financial Analysis'

set variables for dates and profit_loss

Reading the CSV File:
Read the CSV file and populate the dates and profits_losses lists.

Calculating the Total Number of Months:
The total number of months is simply the length of the dates list.
Print the total number of months.

Calculating Net Total Profit/Losses:
net_profit_losses is calculated by summing up all values in the profits_losses list using sum(profits_losses).

Calculating the Average Change:
Calculate the average change by dividing the sum of changes by the number of changes.


Calculating Changes and Tracking the Greatest Increase:
while calculating each change, check if it is the greatest increase seen so far.
If it is, update the greatest_increase and greatest_increase_date.

Initialization:
greatest_increase is initialized to -float('inf') to ensure that any profit increase calculated will update this variable correctly.
greatest_increase_date is initialized as an empty string.


Printing Results:
Print net total
Print the average change.
Print the greatest increase in profits along with the corresponding date.
Print the greatest decrease in profits along with the corresponding date.


# PyPoll_Challenge

import os and csv
create csv path

print the initial text 
Election Results

set variables for ballot id, candidate, candidate votes, the winner and max votes

Reading the CSV File:
Read the CSV file and populate the dates and profits_losses lists.

use a conditional to count no of votes

calculate the total votes cast and percentage 
print result

use a conditional to determine the winner
promt the winner



