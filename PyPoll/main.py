#import relevant libraries
import os
import csv

#To be safe set path for working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Set file path
csvpath = os.path.join("election_data.csv")

#List of stored data
voter_id = []
county = []
candidate = []
unique_list = [] 
khan_votes = 0
Correy_votes = 0
Li_votes = 0
O_Tooley = 0



#Open and read csv file
with open(csvpath, newline='') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')

    #store header row
    data_header = next(election_data)

    for r in election_data:
        #store election data columns in list
        voter_id.append(r[0])
        county.append(r[1])
        candidate.append(r[2])


    #Total number of votes cast
    tot_voterID = len(voter_id)


    #Unique list of candidates who recieved votes
    
    # traverse for all elements 
    for x in candidate: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 

   

    #Count the number of votes for each character
    for x in candidate:

        if x == 'Khan':
            khan_votes += 1

        elif x == 'Correy':
            Correy_votes +=1

        elif x == 'Li':
            Li_votes += 1 

        else:
            O_Tooley += 1

    #enter the number of votes in a list
    votes = [khan_votes, Correy_votes, Li_votes, O_Tooley]

    #Percentage of votes each candidate recieved
    percentage = []

    percentage = ["{:.3f}%".format((x/tot_voterID) * 100) for x in votes]

    #Proclaim a winner
    max_percent = max(percentage)
    max_percentID = percentage.index(max_percent)
    winner = unique_list[max_percentID]


#Voter Analysis
print("Election Results")
print("---------------------------")
print(f'Total Votes: {tot_voterID}')
print("---------------------------")
print(f'Khan: {percentage[0]}   ({votes[0]})' )
print(f'Correy: {percentage[1]}  ({votes[1]})' )
print(f'Li: {percentage[2]} ({votes[2]})' )
print(f"O'Tooley: {percentage[3]}  ({votes[3]})")
print("---------------------------")
print(f'Winner: {winner}')
print("---------------------------")  


#Export analysis to text file
output = open("output.txt", "w")

line1 = "Election Results"
line2 = "---------------------------"
line3 = str(f'Total Votes: {tot_voterID}')
line4 = "---------------------------"
line5 = str(f'Khan: {percentage[0]}   ({votes[0]})' )
line6 = str(f'Correy: {percentage[1]}  ({votes[1]})' )
line7 = str(f'Li: {percentage[2]} ({votes[2]})' )
line8 = str(f"O'Tooley: {percentage[3]}  ({votes[3]})")
line9 = "---------------------------" 
line10 = str(f'Winner: {winner}')
line11 = "---------------------------"
output.write('{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4))
output.write('{}\n{}\n{}\n{}\n'.format(line5,line6,line7,line8))
output.write('{}\n{}\n{}\n'.format(line9,line10,line11))
