import os
import csv

# Path to collect data from the Resources folder
py_paragraph_txt = os.path.join('..', 'Resources', 'pyParagraph.txt')
#election_data_csv = "C:\\Users\\dawnb\\Desktop\\python-challenge\\Resources\\election_data.csv"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(py_paragraph_txt, 'r') as text:

    # This stores a reference to a file stream
    #print(text)

    # Store all of the text inside a variable called "fullParagraph"
    fullParagraph = text.read()

    # Print the contents of the text file and titles
    print("My paragraph is: \n" + fullParagraph + "\n" + "------------------------------")

    print("Paragraph Analysis")
    print("------------------------------")

    #Split words by " " and print the count of the resulting words
    splitWords = fullParagraph.split(" ")
    print("Approximate Word Count: " + str(len(splitWords)))

    #Split words by ". " and print the count of the resulting sentences
    splitSentences = fullParagraph.split(". ")
    print("Approximate Sentence Count: " + str(len(splitSentences)))

    #Determine and print average letters in words by summing the length of words over splitWords and dividing by Word Count
    lettersInWord = 0
    for i in splitWords:
        lettersInWord += len(i) 
    print("Average Letter Count: " + str(round((lettersInWord / len(splitWords)),1)))

    #Determine and print average words in sentences by summing the length of words over splitSentences and dividing by Sentence Count
    splitSentences = fullParagraph.split(". ")
    words_in_sentences = []
    for item in splitSentences:
        split = item.split(" ")
        words_in_sentences.append (len(split))
    print("Average Sentence Length: " + str(sum(words_in_sentences)/len(words_in_sentences)))

