# set up modules
import os
import csv

# file path
csvpath = os.path.join('C:\\Users\\asn03\\Desktop\\Starter_Code\\PyPoll\\Resources\\election_data.csv')
output = "electionresults.txt"

# declare variables
totalvotes = 0
candidates = {"names":[]}
winnercount = 0
winner = ""

# open file
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)

    # loop to find total votes
    for row in csvreader:

        #total vote count
        totalvotes += 1

        #candidate variable
        candidate = row["Candidate"]

                #candidate list
        if candidate not in candidates["names"]:
            candidates["names"].append(candidate)
            
        candidatevotes = {}

        for name in candidates["names"]:
            candidatevotes[name] = 0
            if row["Candidate"] == name:
                candidatevotes[name] += 1

        candidatevotes[candidate] = candidatevotes[candidate] + 1

# create output
with open(output, 'w') as txt_file:
    header = (
        f"Election Results\n"
        f"-----------------\n")
    txt_file.write(header)

    for candidate in candidatevotes:
        votes = candidatevotes[candidate]
        votepercentage = float(votes)/float(totalvotes)*100
        if (votes > winnercount):
            winnercount = votes
            winner = candidate
        voteroutput = f"{candidate}: {votepercentage:.3f}% ({votes})\n"
        print(voteroutput)
        txt_file.write(voteroutput)

    summary = (f"Winner: {winner}")

    print(summary)
    txt_file.write(summary)