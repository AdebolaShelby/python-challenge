# import the os module
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('../..', 'Resources', 'election_data.csv')

print("Election Results")
print("------------------------")

ballot_id = []
candidates = set()
candidate_votes = {}
winner = ""
max_votes = 0

with open('Resources/election_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in csvreader:
        ballot_id.append(row[0])
        candidate = row[2]
        candidates.add(candidate)

        # count no of votes
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# total votes cast result
total_votes = len(ballot_id)
print(f'Total Votes: {total_votes}')
print('----------------------------------')

# total number and percentage
total_votes = sum(candidate_votes.values())
print("Candidate, Percentage, Total Votes")
for candidate, candidate_votes in candidate_votes.items():
    percentage = candidate_votes / total_votes * 100
    print(f'{candidate}, {percentage:.3f}%, ({candidate_votes})')


# calculate the winner

    if candidate_votes > max_votes:
            max_votes = candidate_votes
            winner = candidate
print("-------------------------------------")
print(f'Winner: {winner}')
print("-------------------------------------")
















