import pandas as pd
import json

# Paths for the JSON input and CSV output files
json_file_path = 'output_data.json'  # Replace with the path to your JSON file
csv_file_path = 'vsin_ncaab.csv'    # Output CSV file name

# Load the JSON data
with open(json_file_path, 'r') as file:
    data = json.load(file)

# New column names
column_names = ["Saturday, January 27", "DK Open", "DK", "Circa", "South Point", "Golden Nugget",
                "Westgate", "Wynn", "Stations", "Caesars", "Mirage"]

# Create a DataFrame and process the data
df = pd.DataFrame(data)
# Split the data in each column by newline and stack them
stacked_df = (df.apply(lambda x: x.str.split('\n').explode())
                .reset_index(drop=True))

# Rename columns
stacked_df.columns = column_names

# Create a 'game_id' column
# Each game is represented by two rows, so we use integer division by 2 on the index, then add 1
stacked_df['game_id'] = (stacked_df.index // 2) + 1

# Save to CSV
stacked_df.to_csv(csv_file_path, index=False)
