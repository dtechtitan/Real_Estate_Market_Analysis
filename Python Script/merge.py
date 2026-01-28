import pandas as pd
import glob
import os

# 1. Find all CSV files in the folder
csv_files = ['data/ajah_properties.csv', 'data/Island_Luxury_Data.csv', 'data/Lekki_Central_Data.csv']

# 2. Read and label them
dataframes = []
for filename in csv_files:
    print(f"Reading {filename}...")
    df = pd.read_csv(filename)
    df['Scraped_By'] = filename # Tracks who scraped what
    dataframes.append(df)

# 3. Combine
master_df = pd.concat(dataframes, ignore_index=True)

# 4. Remove Duplicates (Clean based on URL)
master_df = master_df.drop_duplicates(subset=['url'], keep='first')

# 5. Save Master File
master_df.to_csv("Lagos_Master_Data.csv", index=False)
print(f"Done. Merged {len(master_df)} listings into Lagos_Master_Data.csv")