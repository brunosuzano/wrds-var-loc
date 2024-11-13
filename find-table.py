import wrds
import pandas as pd
import os

# Establish connection to WRDS
db = wrds.Connection(wrds_username='brumor')

# List available libraries
libraries = sorted(db.list_libraries())
libraries_df = pd.DataFrame(libraries, columns=["Library"])

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

# =============================================================================
# Search for a particular table name
# =============================================================================

# Manual override for the library
libraries = crsp_libraries

# Define the table name you're looking for
table_to_find = "metasiztociz"  # Replace with the table you want to find

# Initialize a list to store results
found_tables = []

# Search for the table in each library
for library in libraries:
    # List tables in the current library
    tables = db.list_tables(library=library)
    
    # Check if the specific table is in the list of tables
    if table_to_find in tables:
        found_tables.append({'Library': library, 'Table': table_to_find})

# Convert the results to a DataFrame for easy viewing
found_tables_df = pd.DataFrame(found_tables)
print(found_tables_df)

# =============================================================================
# Search for a particular term in a table's name
# =============================================================================

# Manual override for the library
libraries = ['crsp']

# Define the term you're looking for within table names
term_to_find = "linktable"  # Replace with the term you want to search for

# Initialize a list to store results
found_tables = []

# Search for tables containing the specified term in each library
for library in libraries:
    # List tables in the current library
    tables = db.list_tables(library=library)
    
    # Check each table to see if it contains the term
    for table in tables:
        if term_to_find in table:  # Check if term_to_find is a substring of table name
            found_tables.append({'Library': library, 'Table': table})

# Convert the results to a DataFrame for easy viewing
found_tables_df = pd.DataFrame(found_tables)
print(found_tables_df)
