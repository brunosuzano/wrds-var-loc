import wrds
import pandas as pd

# Establish connection to WRDS
db = wrds.Connection(wrds_username='brumor')

# Query to select all rows and columns from specified table
query = "SELECT * FROM crsp.ccmxpf_linktable"

# Execute the query and load the data into a DataFrame
data = db.raw_sql(query)

# Display the first few rows of the data
print(data.head())

# # Optionally, save the data to a CSV file
# data.to_csv("data.csv", index=False)
