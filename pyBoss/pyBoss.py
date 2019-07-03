import os
import csv

# Path to collect data from the Resources folder
employee_data_csv = os.path.join('..', 'Resources', 'employee_data.csv')
#election_data_csv = "C:\\Users\\dawnb\\Desktop\\python-challenge\\Resources\\election_data.csv"

# Create lists to store

employeeId = []
name = []
dob = []
ssn = []
state = []
firstName = []
lastName = []
correctDOB = []
correctSSN = []
correctStates = []

# Load state abbreviation dictionary
stateDictionary = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'Washington, DC': 'DC',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',}

#date_change = []

# Read in the CSV file
with open(employee_data_csv, 'r') as csvfile:

    # Split the data on commas
    employeeData = csv.reader(csvfile, delimiter=',')

    # Remove header for data
    header = next(employeeData)
    for i in employeeData:
        employeeId.append(i[0])
        name.append(i[1])
        dob.append(i[2])
        ssn.append(i[3])
        state.append(i[4])

    
        splitName = i[1].split(" ")
        firstName.append(splitName[0])
        lastName.append(splitName[1])

        splitDOB = i[2].split("-")
        correctDOB.append(splitDOB[1] + "/" + splitDOB[2] + "/" + splitDOB[0])

        splitSSN = i[3].split("-")
        correctSSN.append("***-**-" + splitSSN[2])

        stateAB = stateDictionary[i[4]]
        correctStates.append(stateAB)

# Zip lists together
improved_csv = zip(employeeId,firstName,lastName,correctDOB, correctSSN, correctStates)


# Set variable for output file
output_file = os.path.join("employee_data_improved.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(improved_csv)
