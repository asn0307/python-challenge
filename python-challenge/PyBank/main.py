# import modules
import os
import csv

#path to csv
budgetcsv = os.path.join('C:\\Users\\asn03\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv')

#set output
output = "output.txt"

#set variables
months = 0
totalrevenue = 0
revenue = []
pastrevenue = 0
monthchange = []
revenuechange = 0
greatestincrease = ["", 0]
greatestdecrease = ["", 0]
changelist = []
average = 0

#open file
with open(budgetcsv) as csvfile:
    csvreader = csv.DictReader(csvfile)

#date count
    for row in csvreader:
        months += 1

    #total revenue
        totalrevenue = totalrevenue + int(row["Profit/Losses"])

    #average change
        revenuechange = float(row["Profit/Losses"]) - pastrevenue
        pastrevenue =float(row["Profit/Losses"])
        changelist = changelist + [revenuechange]
        monthchange = [monthchange] + [row["Date"]]

    #greatest increase
        if revenuechange>greatestincrease[1]:
            greatestincrease[1] = revenuechange
            greatestincrease[0] = row['Date']

        if revenuechange<greatestdecrease[1]:
            greatestdecrease[1] = revenuechange 
            greatestdecrease[0] = row['Date']                         
    average = sum(changelist)/len(changelist)
              
# export to csv
with open(output, 'w') as file:
    file.write(f"Financial Analysis")
    file.write(f"--------------------------")
    file.write(f"Total Months: %d\n" % months)
    file.write(f"Total Revenue: $%d\n" % totalrevenue)
    file.write(f"Average Revenue Change $%d\n" % average)
    file.write(f"Greatest Increase in Revenue: %s ($%s)\n" % (greatestincrease[0], greatestincrease[1]))
    file.write(f"Greatest Decrease in Revenue: %s ($%s)\n" % (greatestdecrease[0], greatestdecrease[1]))