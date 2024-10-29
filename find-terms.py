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
libraries = ['crsp']  # List of libraries to check

# Define the search and exclusion terms
term_to_search = 'cap'
term_to_exclude = 'previous cap'

# Initialize a list to store results for each matching variable
results = []

# Iterate through each library
for library in libraries:
    # List tables in the current library (with manual override for tables)
    tables = ["crsp_daily_data",
              "dsf62_v2",
              "dsf_v2",
              "stkdlysecuritydata",
              "stkdlysecuritydata62",
              "stkdlysecurityprimarydata",
              "stkdlysecurityprimarydata62",
              "wrds_dsf62v2_query",
              "wrds_dsfv2_query"]
    
    for table in tables:
        # Describe the current table to get variables and comments
        variables = db.describe_table(library=library, table=table)
        
        # Filter for rows where the comment contains 'cap' but not 'previous cap'
        matching_variables = variables[
            variables['comment'].str.contains(term_to_search, case=False, na=False) &
            ~variables['comment'].str.contains(term_to_exclude, case=False, na=False)
        ]
        
        # Append results if there are matches
        for _, row in matching_variables.iterrows():
            results.append({'Library': library, 'Table': table, 'Variable': row['name'], 'Comment': row['comment']})


# Convert the results list to a DataFrame
results_df = pd.DataFrame(results)
