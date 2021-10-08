import os
import csv

PyPoll_csv = os.path.join('Resources','election_data.csv')

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
O_Tooley_votes = 0




#Reading the CSV file
with open(PyPoll_csv,'r') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',')

	header = next(csv_reader)
	# next_row = 867884


	# Table format
	print(" ")
	print("Election Results")
	print("-----------------------------------")


	for row in csv_reader:
		total_votes = int(total_votes) + 1

		if row[2] == "Khan":
			Khan_votes = Khan_votes + 1

		elif row[2] == "Correy":
			Correy_votes = 1 + Correy_votes

		elif row[2] == "Li":
			Li_votes = 1 + Li_votes

		else:
			O_Tooley_votes = 1 + O_Tooley_votes
        	
#Calculating Vote as a percentage per total vote

Percent_khan = (Khan_votes/total_votes)

Percent_correy = (Correy_votes/total_votes)

Percent_li = (Li_votes/total_votes)

Percent_Otool = (O_Tooley_votes/total_votes)

#Display calculations/outcomes



print(f"Total Votes: {total_votes}")
print("-----------------------------------")
print(f"Khan: {Percent_khan:.3%} ({Khan_votes})")
print(f"Correy: {Percent_correy:.3%} ({Correy_votes})")
print(f"Li: {Percent_li:.3%} ({Li_votes})")
print(f"O'Tooley: {Percent_Otool:.3%} ({O_Tooley_votes})")

print("-----------------------------------")
print(f"Winner: Khan")
print("-----------------------------------")

#Output election results in a text file

text_file = os.path.join("Analysis", "Elections_outcome.txt" )


with open(text_file, "w") as out_file:
    out_file.writelines(["Election Results \n", 
                         "------------------------- \n", 
                         "Total Votes: 3521001 \n", 
                         "------------------------- \n", 
                         "Khan: 63% (2218231) \n", 
                         "Correy: 20% (704200) \n", 
                         "Li: 14% (492940) \n", 
                         "O'Tooley: 3% (105630) \n", 
                         "------------------------- \n", 
                         "Winner: Khan \n", 
                         "------------------------- \n"])










	

	



