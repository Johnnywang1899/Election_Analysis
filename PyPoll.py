'''
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
'''

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')
#with open(file_to_load) as election_data:

# To do: perform analysis
    #print(election_data)

# Close the file.
# election_data.close()

import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row and print.
    headers = next(file_reader)
    print(headers)

    '''
    # Print each row in the CSV file
    for row in file_reader:
        print(row)
        '''


'''
# Using the with statement to open the file as a text file
with open(file_to_save, "w") as outfile:
    
    # Write something
    outfile.write("Counties in Election \n--------------------\n")
    outfile.write("Arapahoe \n")
    outfile.write("Denver \n")
    outfile.write("Jefferson")
'''