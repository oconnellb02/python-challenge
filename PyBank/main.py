import os
import csv

budget_data = os.path.join("..", "..", "Instructions", "PyBank", "Resources", "budget_data.csv")

#def financial_analysis(budget):

        #proloss = int(budget[1])
   
        #total_money = sum(proloss)    
   
        #print(f"Average Change: ")
        #print(f"Greatest Increase in Profits: ")
        #print(f"Greatest Decrease in Profits: ")


with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = " ")

    csv_header = next(csvfile)

    print("Financial Analysis")
    print("--------------------------------")

    date_rows = 0
    for row in csvreader:
        date_rows += 1
    print(f"Total Months: {str(date_rows)}")
    
    
    
    #lines = len(list(csvreader))

    
    #print(f"Total Months: {str(lines)}")
    
    
    #print(f"Total: {str(total_money)}")

    

    