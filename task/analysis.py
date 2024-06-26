import pandas as pd

# Set the maximum number of columns displayed to 8
pd.set_option('display.max_columns', 8)

# Read CSV files into DataFrames
general_df = pd.read_csv("test/general.csv")
prenatal_df = pd.read_csv("test/prenatal.csv")
sports_df = pd.read_csv("test/sports.csv")

# Rename columns in prenatal_df to have consistent column names
prenatal_df.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)

# Rename columns in sports_df to have consistent column names
sports_df.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

# Concatenate the DataFrames into one, ignoring the original index
general_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

# Drop the 'Unnamed: 0' column from the concatenated DataFrame
general_df.drop(columns=['Unnamed: 0'], inplace=True)

# Sample 20 rows from the DataFrame with a fixed random state for reproducibility
general_df = general_df.sample(n=20, random_state=30)

# Print the first 20 rows of the sampled DataFrame
print(general_df.head(20))
