import os
import csv


# Path to collect data from the Resources folder
election_csv = os.path.join('election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

	# Split the data on commas
	csvreader = csv.reader(csvfile, delimiter=',')

	# Read the header row first (skip this step if there is now header)
	header=next(csvreader,None)
	#print(header)

	#Total nb of rows
	row_count = sum(1 for row in csvreader)
	print("Total Votes: " + str(row_count))

# Opening again the file, otherwise for loop returns empty
with open(election_csv, 'r') as csvfile:

	# Split the data on commas
	csvreader = csv.reader(csvfile, delimiter=',')

	# Read the header row first (skip this step if there is now header)
	header=next(csvreader,None)

	list_candidates=[]
	for row in csvreader:
		list_candidates.append(row[2])
	
	# Get unique list of candidates
	list_candidates_unique=set(list_candidates)
	# Covnert to List because Set object is not indexed
	list_candidates_unique=list(list_candidates_unique)
	print("List of candidates: " + str(list_candidates_unique))

	dictionary=dict((x,list_candidates.count(x)) for x in list_candidates_unique)
	#print(dictionary)
	#print(len(dictionary))

	# Pass only values (not keys) from the dictionary to a list
	list_dict_votes=dictionary.values()
	max_votes=max(list_dict_votes)
	out_results=''

	# Loop to get votes, percentage for each candidate and the winner
	for cand in range(len(list_candidates_unique)):
		candidate=list_candidates_unique[cand]
		vote_cand=int(dictionary[candidate])
		per_votes="{:.3%}".format(vote_cand/row_count)
		if vote_cand==max_votes:
			max_cand=candidate
		print(f"{candidate}: {per_votes} ({vote_cand})")
		out_results=out_results + candidate + ': ' + str(per_votes) + ' (' + str(vote_cand) + ')' + '\n'

	print(f"Winner: {max_cand} with {max_votes} votes")

file = './output_candidates.txt'

# Open the file in "write" mode ('w') and store the contents in the variable "text"
with open(file, 'w') as text:
	text.write("Election Results")
	text.write('\n' + "----------------------------")
	text.write('\n' + "Total Votes: " + str(row_count))
	text.write('\n' + "----------------------------")
	text.write('\n' + out_results)
	text.write("----------------------------")
	text.write('\n' + "Winner: " + max_cand + " with " + str(max_votes) + " votes")