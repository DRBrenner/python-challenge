import os
import csv

print("Financial Analysis")
print("-------------------------------")

#Open the text file to write results to
f = open("results.txt", "w")
f.write("Financial Analysis\n")
f.write("------------------------------\n")

# Path to collect data from the Resources folder
#budget_data_csv = os.path.join('..','..', 'Resources', 'budget_data.csv')
budget_data_csv = "C:\\Users\\dawnb\\Desktop\\python-challenge\\Resources\\budget_data.csv"

# Creating profit_change and date_change lists
profit_change = []
date_change = []

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    budgetdata = list(csv.reader(csvfile, delimiter=','))

    # The total number of months included in the dataset
    header = budgetdata[0]
    number_months = 0

    # Count the number of months
    for i in range(1, len(budgetdata)):
        number_months += 1

    print("Total months: " + str(number_months))
    f.write(("Total months: " + str(number_months) + "\n"))

    # The net total amount of "Profit/Losses" over the entire period
    net_profit = 0 
    for i in range(1, len(budgetdata)):
        net_profit = net_profit + int(budgetdata[i][1]) 

    print("Total = $" + str(net_profit))
    f.write("Total = $" + str(net_profit) + "\n")

    # Appending the profit_change list
    for i in range(2,len(budgetdata)):
        change = float(budgetdata[i][1]) - float(budgetdata[i-1][1])
        profit_change.append(change)  #add new amount to list
        date_change.append(str(budgetdata[i][0])) #add

    # Average the profit_change list
    profit_average = sum(profit_change)/len(profit_change)
    print("Average Change: $" + str(round(profit_average,2)))
    f.write("Average Change: $" + str(round(profit_average,2)) + "\n")

    greatest_change = 0
    least_change = 0

    # Determine the greatest and least change
    for i in range(0,len(profit_change)):
        
        if profit_change[i] > greatest_change:
            greatest_change = int(profit_change[i])
            date_greatest_change = date_change[i]          
        elif profit_change[i] < least_change:
            least_change = int(profit_change[i])
            date_least_change = date_change[i]
    
    print("Greatest Increase in Profits: " + date_greatest_change + " $" + str(greatest_change))
    f.write("Greatest Increase in Profits: " + date_greatest_change + " $" + str(greatest_change) + "\n")
    print("Greatest Decrease in Profits: " + date_least_change + " $" + str(least_change))
    f.write("Greatest Decrease in Profits: " + date_least_change + " $" + str(least_change))

f.close()
