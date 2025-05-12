#Anlysing Election Results

import pandas as pd

n = int(input("Enter Number of Election Entries: "))
constituencies = []
parties = []
candidates =[]
votes = []

for i in range(n):
    print(f'Entry {i+1}:')
    constituency = input("Enter Constituency Name: ")
    party = input("Enter Party Name: ")
    candidate = input("Enter Candidate Name: ")
    vote = int(input("Enter Number of Votes: "))
    
    constituencies.append(constituency)
    parties.append(party)
    candidates.append(candidate)
    votes.append(vote)
    
#Sample Data
Data = {'Constituency':constituencies,
        'Party':parties,
        'Candidate':candidates,
        'Votes':votes}
df = pd.DataFrame(Data)

#Calculating Total Votes Per Party

Total_votes_per_party = df.groupby('Party')['Votes'].sum()
print(Total_votes_per_party)

#Identifying Winning party in each constituency

def get_winning_party(x):
    return x.loc[x['Votes'].idxmax(), 'Party']
winning_party_by_constituency = df.groupby('Constituency').apply(get_winning_party)
print("\nWinning Party by constituency: \n",winning_party_by_constituency)

#Overall results
overall_winner = Total_votes_per_party.idxmax()
print("\nOverall Winner Party: ", overall_winner)

#Vote Share percentage
total_votes = df['Votes'].sum()
df['Vote Share (%)'] = (df['Votes']/total_votes) * 100
print("\nVotes Share: \n", df)

#Identifying constituency with close contest
def close_contest(x):
    vote_counts = x['Votes'].values
    if len(vote_counts)>1:
        vote_counts.sort()
        margin = (vote_counts[-1]-vote_counts[-2])/vote_counts[-1] * 100
        return margin<12.0
    else:
        return False
close_constituencies = df.groupby('Constituency').filter(close_contest)['Constituency'].unique()
print("\nConstituency with close contest:",close_constituencies)