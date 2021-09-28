"""
Takes in a csv file generated from the new officers Google Sheets
and writes to a new file named results.csv for importing to LastPass.

Example usage: python lastpass.py officers.csv
"""

import csv, sys

# Modify this if needed
committees = {'studrel': 3, 'bridge': 6, 'treas': 1}

count = committees.copy()
with open(sys.argv[1], 'r') as read_file, open('results.csv', 'w', newline='') as write_file:
    csv_reader = csv.reader(read_file, delimiter=',')
    csv_writer = csv.writer(write_file, delimiter=',')
    csv_writer.writerow(['Email', 'Firstname', 'Lastname'])
    for row in csv_reader:
        if row[5][:-1] in committees.keys():
            csv_writer.writerow([row[4], row[1], row[2]])
            count[row[5][:-1]] -= 1

# FYI statement if incorrect number of officers per license
for c in count.keys():
    if count[c] != 0:
        print(c, "has", committees[c]-count[c], "officers when they're supposed to have", committees[c])
        print("Here are the officers in", c)
        with open(sys.argv[1], 'r') as read_file:
            csv_reader = csv.reader(read_file, delimiter=',')
            for row in csv_reader:
                if row[5][:-1] == c:
                    print(" ", row[4], row[1], row[2])