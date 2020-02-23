#INSTRUCTIONS
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
    # average_change = total_MoM_Change/Number of months
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# DataSet Example
        #Date,Profit/Losses
        #Jan-2010,867884
        #Comma-delimited
            #index 0 - Mon-Year
            #index 1 - Profit/Losses

# Import modules
import os
import csv  

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Create list to store data
    date = []  
    monthly_change = []

    #Initialize variables
    profit_loss = 0
    previous_profit = 0
    
    for row in csvreader:

        #Total number of months in dataset
        date.append(row[0])
        total_months = len(date)

        #Net total amount of "Profit/Losses"
        profit_loss += int(row[1])

        #Calculate MoM change
        current_profit = float(row[1])
        mom_change = current_profit - previous_profit
        
        #Store monthly changes in list and re-set previous profit
        monthly_change.append(mom_change)
        previous_profit = float(row[1])

    #Calculate total MoM change and average change
    monthly_change.pop(0)
    total_change = int(sum(monthly_change))
    average_change = round(total_change / (len(date) - 1),2)  

    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase_profits = int(max(monthly_change))
    increase_date = date[monthly_change.index(greatest_increase_profits)+1]

    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease_profits = int(min(monthly_change))
    decrease_date = date[monthly_change.index(greatest_decrease_profits)+1]    
        
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months: {total_months}") 
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits:, {increase_date}, (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits:, {decrease_date}, (${greatest_decrease_profits})")

with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("Total Months: " + str(total_months) + "\n")
    text.write("Total Profits: " + "$" + str(profit_loss) +"\n")
    text.write("Average Change: " + '$' + str(float(average_change)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")