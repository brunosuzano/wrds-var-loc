import wrds
import pandas as pd
import os

# Establish connection to WRDS
db = wrds.Connection(wrds_username='brumor')

# List available libraries
libraries = sorted(db.list_libraries())
libraries_df = pd.DataFrame(libraries, columns=["Library"])

# CRSP Libraries
crsp_libraries = [
    "crsp",
    "crsp_a_ccm",
    "crsp_a_indexes",
    "crsp_a_stock",
    "crsp_q_indexhist",
    "crsp_q_mutualfunds",
    "crspsamp",
    "crspsamp_all",
    "crspsamp_mf"
]

# Compustat libraries
comp_libraries = [
    "comp",
    "comp_bank",
    "comp_bank_daily",
    "comp_execucomp",
    "comp_global",
    "comp_global_daily",
    "comp_na_annual_all",
    "comp_na_daily_all",
    "comp_na_monthly_all",
    "comp_segments_hist",
    "comp_segments_hist_daily",
    "comp_snapshot",
    "compa",
    "compb",
    "compg",
    "compm",
    "compsamp",
    "compsamp_all",
    "compsamp_snapshot",
    "compseg",
    "compsnap"
]

# Manual override for the library
libraries = crsp_libraries

# Define the variables to search for
variables_to_check = ['tcap']  # You can modify this list to include any variables you want

# Initialize a dictionary to store results for each variable
results = {var: [] for var in variables_to_check}

# Iterate through each library
for library in libraries:
    # List tables in the current library
    tables = db.list_tables(library=library)
    for table in tables:
        # Describe the current table to get variables
        variables = db.describe_table(library=library, table=table)
        variable_names = variables['name'].tolist()

        # Check if each variable in variables_to_check is in the variables list
        for var in variables_to_check:
            if var in variable_names:
                results[var].append({'Library': library, 'Table': table})

# ======================================================================================================================

# Get the current working directory
current_working_directory = os.getcwd()

# Define the directory path
directory_path = os.path.join(current_working_directory, 'var-loc')

# Ensure the directory exists
os.makedirs(directory_path, exist_ok=True)

# Convert results to DataFrames and save to CSV files
for var, data in results.items():
    df = pd.DataFrame(data)

    # Define file path
    file_path = os.path.join(directory_path, f'{var}_loc.csv')

    # Save the DataFrame to a CSV file in the specified directory
    df.to_csv(file_path, index=False)

    # Load the CSV file back into a DataFrame
    globals()[f'{var}_df'] = pd.read_csv(file_path)

# Close the connection
db.close()
