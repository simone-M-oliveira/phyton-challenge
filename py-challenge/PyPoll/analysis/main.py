#modules
import csv

#get data file path
data_file_path = "PyPoll/Resources/election_data.csv"

#set variables

total_votes = 0
candidates = []
candidate_vote_totals = []
candidate_percents = []
winner = ""
header_line = []

#open results
with open (data_file_path,"r") as results:
    #read results
    results_reader=csv.reader(results)
    for vote in results_reader:
        #find header_line categories
        if (results_reader.line_num ==1):
            header_line = vote
        else:
            #set categores for vote based on header_line
            ballot_id = vote [0]
            county = vote [1]
            candidate = vote [2]
            #fill candidates list
            if candidate not in candidates:
                candidates.append (candidate)
                candidate_vote_totals.append (1)
            #calculate total votes per candidate
            else:
                candidate_number = candidates.index(candidate)
                candidate_vote_totals[candidate_number] +=1
            #add the vote to the votes total
            total_votes +=1
    #calculate percents for candidates
    winning_total = 0
    for total in candidate_vote_totals:
        current_percent = ((total/total_votes)*100)
        candidate_percents.append (current_percent)
        #determine winner
        if total>winning_total:
            candidate_number = candidate_vote_totals.index(total)
            winning_total = total
            winner = (candidates[candidate_number])            

#print results in terminal
    print ("")
    print ("Election Results")
    print ("")
    print ("-------------------------")
    print ("")
    print (f'Total Votes: {total_votes}')
    print ("")
    print ("-------------------------")
    print ("")
    for candidate in candidates:
        candidate_number = candidates.index(candidate)
        print (f'{candidate}: {candidate_percents[candidate_number]}% ({candidate_vote_totals[candidate_number]})')
        print ("")
    print ("-------------------------")
    print ("")
    print (f'Winner: {winner}')
    print ("")
    print ("------------------------")

#export results to text file

#get results file path
results_file_path="PyPoll/Analysis/PyPoll_Analysis.txt"

#open results file
with open(results_file_path,"w") as results_file:
    
    #write to results file
    results_file.write ("\n")
    results_file.write ("Election Results\n")
    results_file.write ("\n")
    results_file.write ("-------------------------\n")
    results_file.write ("\n")
    results_file.write (f'Total Votes: {total_votes}\n')
    results_file.write ("\n")
    results_file.write ("-------------------------\n")
    results_file.write ("\n")
    for candidate in candidates:
        candidate_number = candidates.index(candidate)
        results_file.write (f'{candidate}: {candidate_percents[candidate_number]}% ({candidate_vote_totals[candidate_number]})\n')
        results_file.write ("\n")
    results_file.write ("-------------------------\n")
    results_file.write ("\n")
    results_file.write (f'Winner: {winner}\n')
    results_file.write ("\n")
    results_file.write ("------------------------\n")