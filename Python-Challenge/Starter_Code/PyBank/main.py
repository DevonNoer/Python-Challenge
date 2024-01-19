#importing required mods
import os
import csv

#creating path to resources file
budget_data = os.path.join("Starter_Code/PyBank/Resources/budget_data.csv")

#setting starting variables
totalProfLoss = 0
changeProfLoss = []
valPrevRow = 0
avgProfLoss = 0

#Starting loop with the file open
with open(budget_data, newline="") as csvfile:

    #creating the reader and skipping the header row
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    #creating and initalizing variables
    budgetData = [next(csv_reader)]
    totalProfLoss = int(budgetData[0][1])
    valPrevRow = totalProfLoss

    #looping through each row in the read in file
    for row in csv_reader:

        #storing variables to the corresponding data in the file
        budgetData.append(row)
        totalProfLoss = totalProfLoss + int(row[1])
        changeProfLoss.append(int(row[1]) - valPrevRow)

        valPrevRow = int(row[1])

#max change index
indexMaxProf = changeProfLoss.index(max(changeProfLoss))

#min change index
indexMaxLoss = changeProfLoss.index(min(changeProfLoss))
        
#average change in profit loss
avgProfLoss = round(sum(changeProfLoss)/len(changeProfLoss), 2)

#Printing results to terminal
print("Financial Analysis")
print("-------------------------------------")
print("Total Months: " + str(len(budgetData)))
print("Total: $" + str(totalProfLoss))
print("Average Change: $" + str(avgProfLoss))
print(f'Greatest Increase in Profits: {budgetData[indexMaxProf + 1][0]} (${max(changeProfLoss)})')
print(f'Greatest Decrease in Profits: {budgetData[indexMaxLoss + 1][0]} (${min(changeProfLoss)})')

#printing results to a text file and exporting it
csvpath = os.path.join('Starter_Code', 'PyBank', 'Analysis', 'Financial_Analysis.txt')
with open(csvpath,'w') as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n-------------------------------------")
    textfile.write("\nTotal Months: " + str(len(budgetData)))
    textfile.write("\nTotal: $" + str(totalProfLoss))
    textfile.write("\nAverage Change: $" + str(avgProfLoss))
    textfile.write(f'\nGreatest Increase in Profits: {budgetData[indexMaxProf + 1][0]} (${max(changeProfLoss)})')
    textfile.write(f'\nGreatest Decrease in Profits: {budgetData[indexMaxLoss + 1][0]} (${min(changeProfLoss)})')
