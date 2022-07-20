# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total numbers of votes each candidate won
# 5. The winner of the election based on popular vote.


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# To do: perform analysis.


# Close the file.
election_data.close()



