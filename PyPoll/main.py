import os
import csv

print("Election Results")
print("-------------------------------")

#Open the text file to write results to
f = open("pollresults.txt", "w")
f.write("Election Results\n")
f.write("------------------------------\n")

# Path to collect data from the Resources folder
#election_data_csv = os.path.join('..','..', 'Resources', 'election_data.csv')
election_data_csv = "C:\\Users\\dawnb\\Desktop\\python-challenge\\Resources\\election_data.csv"

# Create lists
#profit_change = []
#date_change = []

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    electionData = csv.reader(csvfile, delimiter=',')

    # The total number of months included in the dataset


    #skip header
    header = next(electionData)

    # total number of votes cast
    totalVotes = 0
    candidates = []
    percanditate = []
    for i in electionData:
        if i[2] not in candidates:
            candidates.append(i[2])
            percanditate.append(1)
        else:
            index = candidates.index(i[2])
            percanditate[index] += 1
        totalVotes += 1
    print("Total Votes: " + str(totalVotes))
    f.write("Total Votes: " + str(totalVotes) + "\n")
        
    print(candidates)
    print(percanditate)
    print(electionData)

        

     # total number of votes cast for each candidate
#### DAWN's QUESTIONABLE CODE
"""

    candidates = []
    for row in electionData:
        if row[2] not in candidates:
            candidates.append(row[2])
    print(candidates)

#    from collections import Counter
#    z = list(electionData)
#    Counter(z)


#>>> z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
#>>> Counter(z)
#Counter({'blue': 3, 'red': 2, 'yellow': 1})


#A complete list of candidates who received votes

   
#The percentage of votes each candidate won
for row in electionData:

#The total number of votes each candidate won
#The winner of the election based on popular vote.
"""