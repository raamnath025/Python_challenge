import os
import csv


Poll_Data = os.path.join("Resources","election_data.csv")
vote_total = []
vote_percentage = []
candidates = []
main_candidate = []
total_votes = 0


with open(Poll_Data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1
        candidates.append(row[2])
    for Final in set(candidates):
        main_candidate.append(Final)
        number_candidate = candidates.count(Final)
        vote_total.append(number_candidate)
        percent = (number_candidate/total_votes)*100
        vote_percentage.append(percent)
        
    
    winner = main_candidate[vote_total.index(max(vote_total))]
    

 
print("-----------------------")
print("Election Results")   
print("-----------------------")
print("Total Votes: " + str(total_votes))    
print("-----------------------")
for Final in range(len(main_candidate)):
            print(main_candidate[Final] + ": " + str(round(vote_percentage[Final],3)) +"% (" + str(vote_total[Final])+ ")")
print("-----------------------")
print("The winner is: " + winner)
print("-----------------------")

Poll_Data = os.path.join("analysis","election_data.txt")
with open(Poll_Data, 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("-------------------------------------\n")
    for Final in range(len(set(main_candidate))):
        text.write(main_candidate[Final] + ": " + str(vote_percentage[Final]) +"% (" + str(vote_total[Final]) + ")\n")
    text.write("-------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("-------------------------------------\n")
