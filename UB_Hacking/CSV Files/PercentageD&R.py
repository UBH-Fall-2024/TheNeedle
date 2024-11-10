import csv
import re

# Load the CSV data into a dictionary with lowercase keys
file = "D&Rtestingcase.csv"
aDict = {}

with open(file, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) == 2:
            key = row[0].strip().lower()
            try:
                value = int(row[1])
                aDict[key] = value
            except ValueError:
                print(f"Warning: Skipping non-integer value in row: {row}")


#WHEN COMPILING CHANGE THE INPUT TO GUI
# Input: block of text
user_input = input("Enter a block of text: ").lower()

# Initialize list to store scores of matching phrases
values = []

# Find all phrases in the dictionary that appear in the text and count occurrences
for phrase, score in aDict.items():
    matches = re.findall(rf'\b{re.escape(phrase)}\b', user_input)
    count = len(matches)  # Count the occurrences of the phrase

    # Append the score to values list for each occurrence
    values.extend([score] * count)

# Check if there are at least 3 matching phrases
if len(values) < 3: # Less than 3 'Catches' of political phrasing
    print("Not enough data to determine political leaning.")
else:
    # Calculate the average based on the values in the list
    average = sum(values) / len(values)
    
    if average < 0:
        leaning = "Democratic"
        percentage = abs(average) * 5  # Convert to percentage
    elif average > 0:
        leaning = "Republican"
        percentage = average * 5  # Convert to percentage
    else:
        leaning = "Neutral / Centrist"
        percentage = 0
    
    print(f"{percentage:.1f}% {leaning} leaning based on {len(values)} matching phrases")

print(values)

    print(f"{percentage:.1f}% {leaning} leaning based on {len(values)} matching phrases")
else:
    print("No partisan lean.")
