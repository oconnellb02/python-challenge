import os
import csv

election_data = os.path.join("..", "Resources", "election_data.csv")

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader) 
    
    votes = {}
    candidates = []

    for row in csvreader:
        candidate = row[2]
        if not (candidate in candidates):
            candidates.append(candidate)
            votes[candidate]=0
        votes[candidate]=votes[candidate]+1

    total_votes = sum(votes.values())
    
    print("Election Results")
    print("-----------------------------")

    percentage = []
    output=(f'\nElection Results\n'
            f'-----------------------------\n')

    print(f"Total Votes: {(total_votes)}")
    print("-----------------------------")

    for candidate in votes:
        percentage = round(((votes[candidate] / total_votes)*100),4)

        print(f'{(candidate)}: {(percentage)}% ({(votes[candidate])})') 
        output+=(f'{(candidate)}: {(percentage)}% ({(votes[candidate])})')

    print("-----------------------------")

    for winner in votes.keys():
        if votes[winner] == max(votes.values()):
            candidate_winner = winner

    print(f'Winner: {(candidate_winner)}')
    output += (f'Winner: {(candidate_winner)}') 
    
    print("-----------------------------")

    text_path=os.path.join("election_data.txt")
    with open(text_path,"w") as txtfile:
        txtfile.write(output)


    
  


        
