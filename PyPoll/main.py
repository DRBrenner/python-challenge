import os
import csv

#os.chdir(os.path.dirname(__file__))

print('\n')
print("Election Results")
print("-------------------------------")

#Open the text file to write results to
f = open("pollresults.txt", "w")
f.write("\n")
f.write("Election Results\n")
f.write("------------------------------\n")



# Path to collect data from the Resources folder
election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')
#election_data_csv = "C:\\Users\\dawnb\\Desktop\\python-challenge\\Resources\\election_data.csv"

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
    print("-------------------------------")
    f.write("Total Votes: " + str(totalVotes) + "\n")
    f.write("------------------------------\n")
        


    # Create precent of total in new list for each candidate
    percentList = []
    for i in percanditate:
        percentTotal = (i / totalVotes) * 100
        percentList.append(percentTotal)

    # Zip all three lists together into tuple
    results = zip(candidates, percanditate, percentList)
    
    winningVotes = 0
    winner = ""
    for i in range(0,len(candidates)):
        print(candidates[i] + ": " + str(round(percentList[i],3)) + "% (" + str(percanditate[i]) + ")")
        f.write(candidates[i] + ": " + str(round(percentList[i],3)) + "% (" + str(percanditate[i]) + ")" + "\n")
        #print(candidates[i] + ": " + str(round(percentList[i],3)) + " (" + str(percanditate[i])) + ")"))

        # Calculate the winner
        if percentList[i] > winningVotes:
            winningVotes = percentList[i]
            winner = candidates[i]
    print("-------------------------------")
    print("Winner: " + winner) 
    print("-------------------------------")
    f.write("------------------------------\n")
    f.write("Winner: " + winner + "\n")
    f.write("------------------------------\n")
