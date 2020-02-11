title = "Financial Analysis"
print(title)

print("--------------------------------")

import os
import csv

data = os.path.join("budgetdata.csv")

#create list for use later

monthly_changes_list = []
profit_loss = []
date = []

#set variables

months = 0 
total = 0 
total_change = 0 

#must use 867884 so that the for loop has an appropriate place to start.

initial= 867884

#read in csvfile

with open(data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #for loops are fun!

    for row in csvreader:
        months = months + 1

        date.append(row[0])

        
        
    print("Total Months: " +str(months))


final = int(row[1])


