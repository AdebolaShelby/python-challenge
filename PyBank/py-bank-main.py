# import the os module
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('../..', 'Resources', 'budget_data.csv')

print("Financial Analysis")
print("------------------------")

dates = []
profit_loss = []

with open('Resources/budget_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    for row in csvreader:
        dates.append(row[0])
        profit_loss.append(int(row[1]))

# total number of months
total_months = len(dates)
print("Total Months: ", total_months)

# net total
net_total = sum(profit_loss)

# calculating the changes
changes = []
greatest_increase_in_profits = -float('inf')
greatest_increase_in_profits_date = ""
greatest_decrease_in_profits = float('inf')
greatest_decrease_in_profits_date = ""


for i in range(1, len(profit_loss)):
    change = profit_loss[i] - profit_loss[i-1]
    changes.append(change)

    if change > greatest_increase_in_profits:
        greatest_increase_in_profits = change
        greatest_increase_in_profits_date = dates[i]

    if change < greatest_decrease_in_profits:
        greatest_decrease_in_profits = change
        greatest_decrease_in_profits_date = dates[i]

print(f"Total: ${net_total}")
average = int(sum(changes)/len(changes))
print(f'Average Change: ${average}')
print(f"Greatest Increase in Profits: {greatest_increase_in_profits_date} (${greatest_increase_in_profits})")
print(f"Greatest Decrease in Profits: {greatest_decrease_in_profits_date} (${greatest_decrease_in_profits})")
















