# Import the os and the csv dependencies
import os
import csv

budgetData_csv = os.path.join ("Resources","budget_data.csv")
pyBank = []

#Defining PyBank variables
months = []
profits = []
profit_losses = []
total_profits = 0
profit_table_row = 0
profit_change = 0

with open (budgetData_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvfile)
    
    for bank in csvreader:
        pyBank.append(bank)

#Finding the total number of months included in the dataset
for Final in pyBank:
    months.append(str(Final[0]))
total_months = len(months)

#Finding the total amount of "Profits/Losses" over the entire period 
for Final in pyBank:
    profits.append(int(Final[1]))
total_profits = sum(profits)

#Finding the changes in "Profit/Losses" over the entire period, and then the average of those changes

for profit_table_row in pyBank:
    profit_change = profit_change +int(profit_table_row[1])

last_row = profits[0]
for profit_table_row in profits:
    change = int(profit_table_row) - int(last_row)
    profit_losses.append(change)
    last_row = profit_table_row

total_change = sum(profit_losses)
average_change = round(total_change/(total_months - 1), 2)

current_row = 0
increase_profits = 0
for profit_table_row in profits:
    last_row = profit_table_row
if current_row > increase_profits:
        increase_profits = current_row

#Finding the greatest increase in profits (date and amount) over the entire period
greatest_months = list(zip(months, profit_losses))

increase_profits = max(profit_losses)
for Final in greatest_months:
    if Final[1] == increase_profits:
        greatest_month = Final[0]
greatest_month_increase = [{greatest_month},{increase_profits}]

#Finding the greatest decrease in profits (date and amount) over the entire period
decrease_profits = 0
decrease_profits = min(profit_losses)
for Final in greatest_months:
    if Final[1] == decrease_profits:
        least_month = Final[0]
        #print(least_month)
greatest_month_decrease = [{least_month},{decrease_profits}]

output = ["Financial Analysis",
"-----------------------",
f"Total Months: {total_months}",
f"Total: ${total_profits}",
f"Average Change: ${average_change}",
f"Greatest Increase in Profits: {greatest_month}, ${increase_profits}",
f"Greatest Decrease in Profits: {least_month}, ${decrease_profits}"]

for Final in output:
    print(Final)

#Export the text file with the results
budgetData_csv = os.path.join("analysis", "budget_data.txt")
with open (budgetData_csv,'w') as text:
    for Final in output:
        text.write(Final)
        text.write('\n')