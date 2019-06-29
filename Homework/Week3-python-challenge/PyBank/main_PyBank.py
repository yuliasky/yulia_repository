import os
import csv
import statistics

# Path to collect data from the Resources folder
budget_csv = os.path.join('budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

	# Split the data on commas
	csvreader = csv.reader(csvfile, delimiter=',')

	# Read the header row first (skip this step if there is now header)
	header=next(csvreader,None)
	#print(header)

	cont_months=0
	tot_profit=0
	changes_array=[]
	prev_val=0
	dates_array=[]

	# Loop to get the total months, total amount, changes in profit/losses and all the dates (stored in lists)
	for row in csvreader:
		cont_months=cont_months+1
		tot_profit=tot_profit+int(row[1])
		changes_array.append(int(row[1])-prev_val)
		prev_val=int(row[1])
		dates_array.append(row[0])

	# Total months and total amount
	print("Total months: " + str(cont_months))
	print("Total: $" + str(tot_profit))

	#print(len(changes_array))
	#print(changes_array)
	# Remove the first value of the list of changes, because that one has not changed
	del changes_array[0]
	#print(changes_array)

	# Alternative to get the average -- not used
	#tot_changes=0
	#for val in range(len(changes_array)):
	#	tot_changes=tot_changes+changes_array[val]
	#av_changes=(tot_changes-changes_array[0])/(len(changes_array)-1)

	# Average of changes - using mean method from statistics
	av_changes=statistics.mean(changes_array)
	print("Average  Change: $" + str(round(av_changes,2)))
	# Maximum change - using max method
	max_changes=max(changes_array)
	# Get the index where that max change occurred
	max_index=changes_array.index(max(changes_array))
	#print(max_changes)
	#print(max_index)

	#print(dates_array)
	# Remove te first value of the list of dates, because is not used, no change in there
	del dates_array[0]

	# Get the date when the max change occurred
	max_date=dates_array[max_index]
	print("Greatest Increase in Profits: " + max_date +" ($" + str(max_changes) + ")")

	# Minimum change - using min method
	min_changes=min(changes_array)
	# Get the index where that min change occurred
	min_index=changes_array.index(min(changes_array))
	#print(min_changes)
	#print(min_index)

	# Get the date when the min change occurred
	min_date=dates_array[min_index]
	print("Greatest Decrease in Profits: " + min_date + " ($" + str(min_changes) + ")")

file = './output_budget.txt'

# Open the file in "write" mode ('w') and store the contents in the variable "text"
with open(file, 'w') as text:
	text.write("Financial Analysis")
	text.write('\n' + "----------------------------")
	text.write('\n' + "Total Months: " + str(cont_months))
	text.write('\n' + "Total: $" + str(tot_profit))
	text.write('\n' + "Average  Change: $" + str(round(av_changes,2)))
	text.write('\n' + "Greatest Increase in Profits: " + max_date + ' ($' + str(max_changes) + ')')
	text.write('\n' + "Greatest Decrease in Profits: " + min_date + ' ($' + str(min_changes) + ')')




	