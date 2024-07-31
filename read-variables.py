import pandas as pd

# Load the CSV files into DataFrames
exchcd_df = pd.read_csv('exchcd_loc.csv')
prc_df = pd.read_csv('prc_loc.csv')

# Merge the DataFrames on the 'Table' column and keep all columns
common_tables_df = pd.merge(prc_df, exchcd_df, on=['Library', 'Table'], how='inner')

# Display the merged DataFrame
print("Merged DataFrame with common 'Table' values:")
print(common_tables_df)