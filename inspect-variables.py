import wrds
import pandas as pd

# =============================================================================
# Inspect variables/tables/libraries
# =============================================================================

# Establish connection to WRDS
db = wrds.Connection(wrds_username='brumor')

# List available libraries
libraries = sorted(db.list_libraries())
libraries = pd.DataFrame(libraries, columns=["Library"])

# Select library to work with
lib = "crsp"

# List tables in library lib
tables = db.list_tables(library=lib)
tables = pd.DataFrame(tables, columns=["Table"])

# Select table to work with
tab = "metasiztociz"

# List variables in table tab
variables = db.describe_table(library=lib, table=tab)

# Get row count
row_count = db.get_row_count(lib, tab)

# Get the first 100 observations
table = db.get_table(lib, tab, obs=100)

# Close the connection
db.close()

# =============================================================================
# Locate a specific term within variable descriptions
# =============================================================================

# # Locate the term "country" or "Country" in the comment column
# mask = variables['comment'].str.contains('country', case=False, na=False)

# # Filter rows containing the term
# filtered_df = variables[mask]