import wrds
import pandas as pd
import os

# Establish connection to WRDS
db = wrds.Connection(wrds_username='brumor')

# List available libraries
libraries = sorted(db.list_libraries())
libraries_df = pd.DataFrame(libraries, columns=["Library"])

# Initialize lists to store results
namedt_present = []
nameendt_present = []

# Manual override for the library
# libraries = ["crsp"]

# Iterate through each library
for library in libraries:
    # List tables in the current library
    tables = db.list_tables(library=library)
    for table in tables:
        # Describe the current table to get variables
        variables = db.describe_table(library=library, table=table)
        variable_names = variables['name'].tolist()

        # Check if 'var-loc' and 'nameendt' are in the variables list
        if 'namedt' in variable_names:
            namedt_present.append({'Library': library, 'Table': table)
        if 'nameendt' in variable_names:
            nameendt_present.append({'Library': library, 'Table': table)

# Convert results to DataFrame
namedt_df = pd.DataFrame(namedt_present)
nameendt_df = pd.DataFrame(nameendt_present)

# Display the results
print("Tables with 'namedt' variable:")
print(namedt_df)

print("\nTables with 'nameendt' variable:")
print(nameendt_df)

# Close the connection
db.close()

# ======================================================================================================================

# Get the current working directory
current_working_directory = os.getcwd()

# Define the directory path
directory_path = os.path.join(current_working_directory, 'var-loc')

# Ensure the directory exists
os.makedirs(directory_path, exist_ok=True)

# Define file paths
namedt_file_path = os.path.join(directory_path, 'namedt_present.csv')
nameendt_file_path = os.path.join(directory_path, 'nameendt_present.csv')

# Save the DataFrames to CSV files in the specified directory
namedt_df.to_csv(namedt_file_path, index=False)
nameendt_df.to_csv(nameendt_file_path, index=False)
