#modules
import csv
import math

#get data file path
data_file_path = "PyBank/Resources/budget_data.csv"

#set variables
total_months = 0
total_amount = 0
changes = []
average_change = 0
greatest_p_increase = 0
greatest_p_increase_date = ("")
greatest_p_decrease = 0
greatest_p_decrease_date = ("")
header_line = []

#open results
with open (data_file_path,"r") as budget:
    #read results
    budget_reader=csv.reader(budget)
    for entry in budget_reader:
        if (budget_reader.line_num ==1):
            header_line = entry
        else:
            #set categores for vote based on header_line
            date = entry [0]
            profit_losses = float(entry [1])
            #add a entry to the month count
            total_months +=1
            #calculate total
            total_amount += float(profit_losses)
            #calculate change
            if (budget_reader.line_num >2):
                change = (float(profit_losses)-float(prev_profit_losses))
                changes.append (change)
                #calculate greatest profit increase and decrease
                if change>greatest_p_increase:
                    greatest_p_increase = change
                    greatest_p_increase_date = date
                if change<greatest_p_decrease:
                    greatest_p_decrease = change
                    greatest_p_decrease_date = date
            #set current profit/losses to previous profit/losses
            prev_profit_losses = profit_losses

#calculate total change
total_change = 0
for change in changes:
    total_change +=float(change)

#calculate average change using total change
average_change = (float(total_change)/float(len(changes)))

#print results in terminal
print ("")
print ("Financial Analysis")
print ("")
print ("----------------------------")
print ("")
print (f'Total Months: {total_months}')
print ("")
print (f'Total: ${total_amount}')
print ("")
print (f'Average Change: ${average_change}')
print ("")
print (f'Greatest Increase in Profits: {greatest_p_increase_date} (${greatest_p_increase})')
print ("")
print (f'Greatest Decrease in Profits: {greatest_p_decrease_date} (${greatest_p_decrease})')
print ("")

#export results to text file

#get results file path
results_file_path="PyBank/Analysis/PyBank_Analysis.txt"

#open results file
with open(results_file_path,"w") as results_file:
    
    #write to results file
    results_file.write ("\n")
    results_file.write ("Financial Analysis\n")
    results_file.write ("\n")
    results_file.write ("----------------------------\n")
    results_file.write ("\n")
    results_file.write (f'Total Months: {total_months}\n')
    results_file.write ("\n")
    results_file.write (f'Total: ${total_amount}\n')
    results_file.write ("\n")
    results_file.write (f'Average Change: ${average_change}\n')
    results_file.write ("\n")
    results_file.write (f'Greatest Increase in Profits: {greatest_p_increase_date} (${greatest_p_increase})\n')
    results_file.write ("\n")
    results_file.write (f'Greatest Decrease in Profits: {greatest_p_decrease_date} (${greatest_p_decrease})\n')
    results_file.write ("\n")