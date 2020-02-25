#INSTRUCTIONS
#The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Create a Python script that analyzes the votes and calculates each of the following:

    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote

# Import modules
import os
import csv  

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV reader and skip header
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Create list to store data and initialize variables
    total_votes = 0
    candidate_list = []
    unique_candidate = []
    vote_tally = []
    vote_percent = []

    for row in csvreader:

        #The total number of votes cast
        total_votes = total_votes + 1

        #Apply candidate names to candidate list
        candidate_list.append(row[2])

    #Create a set to get unique candidate names
    for name in set(candidate_list):
        unique_candidate.append(name)

        #Votes per candidate
        candidate_votes = candidate_list.count(name)
        vote_tally.append(candidate_votes)

        #Percent per candidate
        candidate_percent = round((candidate_votes/total_votes)*100, 3)
        vote_percent.append(candidate_percent)

    #Determine winner    
    winning_count = max(vote_tally)
    winner = unique_candidate[vote_tally.index(winning_count)]

#Print results to terminal 
print("Election Results")   
print("-------------------------")
print("Total Votes:" + str(total_votes))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_tally[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#Print output file in txt format
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_tally[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")



