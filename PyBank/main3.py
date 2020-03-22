import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader) 

    print("Financial Analysis")
    print("-----------------------------") 
    
    months = 0
    total = 0
    total_change = 0

    dates = []
    changes = []

    for row in csvreader:
        months += 1
        total += int(row[1])

        if months == 1:
            previous_value = int(row[1])
        change = int(row[1]) - previous_value
        previous_value = int(row[1])
        total_change += change

        dates.append(row[0])
        changes.append(change)

    average = round(total_change / (months-1),2)

    greatest_inc = changes.index(max(changes))
    greatest_dec = changes.index(min(changes))
    greatest_inc_date = dates[greatest_inc]
    greatest_dec_date = dates[greatest_dec]

    #print(dates[greatest_inc])
    #print(dates[greatest_dec])

    print(f"Total Months: {(months)}")
    print(f"Total: $ {(total)}")
    print(f"Average Change: $ {(average)}")
    print(f"Greatest Increase in Profits: {(greatest_inc_date)} (${(max(changes))})")
    print(f"Greatest Decrease in Profits: {(greatest_dec_date)} (${(min(changes))})")

