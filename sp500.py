import csv
from itertools import islice


# Open the CSV file
with open('./IVV_holdings.csv', 'r') as f:
    # Create a CSV reader object
    reader = csv.reader(f)

    # Create an empty list to store the ticker
    SP_500_TICKER = []

    # Loop through each row in the CSV file
    for row in islice(reader, 10, 519):
        # Extract the ticker from the row
        first_word = row[0].split()[0]

        # Add the ticker to the list
        SP_500_TICKER.append(first_word)

# Print the list of stocks
print(SP_500_TICKER)