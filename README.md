# Election_Analysis
 
## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.69.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
   - Charles Casper Stockham
   - Diana DeGette
   - Raymon Anthony Doane
- The candidate results were:
   - Charles Casper Stockham: 23.0% (85,213)
   - Diana DeGette: 73.8% (272,892)
   - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
   - Diana DeGette: who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
The challenge required me to calculate the number of votes for each county, find the percentage of votes for each county, and print that data along with the county that had the most votes. A lot of the code was similar to what I had previously done with the candidates.
## Challenge Summary
The analysis of the election show that:
- There were 3 counties that participated.
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- The county vote majority was:
  - Denver with 306,055 votes resulting in 82.8% of the total votes.
  
  This script was able to determine results from candidates and county effectively. It proved everything needed for a proper election. I believe this script has the capability to be used for any other election; with some slight modifications. As for a presidential election, instead of going by county, the script could be replaced by state votes. As long as the csv file has that information it would be a viable modification to show what states have the highest voting percentage. It could also be used on a smaller scale, for example: An election for county sheriff. If used that way then instead of voters by county it could be modified to voters by city. The script is easily manipulated to tend to whatever the election calls for. 
  
  # Script
  Below is an outline of the full script
  
  coding: UTF-8
PyPoll Homework Challenge Solution.
```
 Add our dependencies.
import csv
import os

 Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
 Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

 Initialize a total vote counter.
total_votes = 0

 Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

 1: Create a county list and county votes dictionary.

county_list = []
county_votes = {}

 Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

 2: Track the largest county and county voter turnout.

largest_county = ""
largest_county_voter_turnout = 0

 Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

     Read the header
    header = next(reader)

     For each row in the CSV file.
    for row in reader:

         Add to the total vote count
        total_votes = total_votes + 1

         Get the candidate name from each row.
        candidate_name = row[2]

         3: Extract the county name from each row.
        county_name = row[1]

         If the candidate does not match any existing candidate add it to
         the candidate list
        if candidate_name not in candidate_options:

             Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

             And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

         Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

         4a: Write an if statement that checks that the
         county does not match any existing county in the county list.
        if county_name not in county_list:

             4b: Add the existing county to the list of counties.
            county_list.append(county_name)

             4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

         5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


 Save the results to our text file.
with open(file_to_save, "w") as txt_file:

     Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

     6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

         6b: Retrieve the county vote count.
        county_v = county_votes.get(county_name)

         6c: Calculate the percentage of votes for the county.
        county_vp = float(county_v) / float(total_votes) * 100

          6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {county_vp:.1f}% ({county_v:,})\n")
        print(county_results)

          6e: Save the county votes to a text file.
        txt_file.write(county_results)

          6f: Write an if statement to determine the winning county and get its vote count.
        if (county_v > largest_county_voter_turnout):
            largest_county_voter_turnout = county_v
            largest_county = county_name
            
     7: Print the county with the largest turnout to the terminal.
    largest_county_turnout = (f"-------------------------------\n"
    f"Largest County Turnout: {largest_county}\n"
    f"-------------------------------\n")
    print(largest_county_turnout)
         

     8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_turnout)

     Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

         Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

         Print each candidate's voter count and percentage to the
         terminal.
        print(candidate_results)
          Save the candidate results to our text file.
        txt_file.write(candidate_results)

         Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

     Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

     Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    ```
