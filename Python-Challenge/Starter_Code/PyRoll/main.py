#import the mods required
import os
import csv

#creating path to the file needed
csvpath = os.path.join("Starter_Code/PyRoll/Resources/election_data.csv")

#initializing the variables i need
totalVotes = []
votesPerCanidate = []

#creating a loop to open file and storing the header
with open(csvpath, newline="") as csvfile:

    csvReader = csv.reader(csvfile, delimiter=",")
    csvHeader = next(csvReader)

    #looping through each row and storing who they voted for
    for row in csvReader:
        
        totalVotes.append(row[2])

    #creating a list of the unique answers in the voted for column
    canidates = list(set(totalVotes))
    
    #counting how many votes each canidate got
    for canidate in canidates:

        votesPerCanidate.append(totalVotes.count(canidate))

#Printing results to terminal
print("Election Results")
print("-------------------------------------------")
print("Total Votes: " + str(len(totalVotes)))
print("-------------------------------------------")
print(f'{canidates[0]}: {round((votesPerCanidate[0] / len(totalVotes)) * 100, 3)}% ({votesPerCanidate[0]})')
print(f'{canidates[1]}: {round((votesPerCanidate[1] / len(totalVotes)) * 100, 3)}% ({votesPerCanidate[1]})')
print(f'{canidates[2]}: {round((votesPerCanidate[2] / len(totalVotes)) * 100, 3)}% ({votesPerCanidate[2]})')      
if(votesPerCanidate[0] > votesPerCanidate[1] and votesPerCanidate[0] > votesPerCanidate[2]):

    print("Winner: " + str(canidates[0]))

elif(votesPerCanidate[1] > votesPerCanidate[0] and votesPerCanidate[1] > votesPerCanidate[2]):

    print("Winner: " + str(canidates[1]))

else:

    print("Winner: " + str(canidates[2]))


exportPath = os.path.join('Starter_Code', 'PyRoll', 'Analysis', 'Election_Results.txt')
#printing results to a txt file 
with open(exportPath,'w') as textfile:

    textfile.write("Election Results")
    textfile.write("\n-------------------------------------------")
    textfile.write("\nTotal Votes: " + str(len(totalVotes)))
    textfile.write("\n-------------------------------------------")
    textfile.write(f'\n{canidates[0]}: {round((votesPerCanidate[0] / len(totalVotes)) * 100, 3)}% ({votesPerCanidate[0]})')
    textfile.write(f'\n{canidates[1]}: {round((votesPerCanidate[1] / len(totalVotes)) * 100, 3)}% ({votesPerCanidate[1]})')
    textfile.write(f'\n{canidates[2]}: {round((votesPerCanidate[2] / len(totalVotes)) * 100, 3)}% ({votesPerCanidate[2]})')
    if(votesPerCanidate[0] > votesPerCanidate[1] and votesPerCanidate[0] > votesPerCanidate[2]):

        textfile.write("\nWinner: " + str(canidates[0]))

    elif(votesPerCanidate[1] > votesPerCanidate[0] and votesPerCanidate[1] > votesPerCanidate[2]):

        textfile.write("\nWinner: " + str(canidates[1]))

    else:

        textfile.write("\nWinner: " + str(canidates[2]))
