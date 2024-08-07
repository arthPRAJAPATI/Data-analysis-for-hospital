import pandas as pd
import matplotlib.pyplot as plt

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
# Drop rows where all elements are missing
general_df.dropna(axis='rows', inplace=True, how='all')

# Replace 'male' and 'man' with 'm' in the gender column
general_df.replace(['male', 'man'], 'm', inplace=True)

# Replace 'female' and 'woman' with 'f' in the gender column
general_df.replace(['female', 'woman'], 'f', inplace=True)

# Fill NaN values in the 'gender' column with 'f'
general_df.fillna({'gender': 'f'}, inplace=True)

# Fill NaN values in specified columns with 0
general_df.fillna({'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0, 'mri': 0, 'xray': 0, 'children': 0, 'months': 0}, inplace=True)

#Which hospital has the highest number of patients?
#print(f"The answer to the 1st question is {general_df.hospital.value_counts().idxmax()}")

#What share of the patients in the general hospital suffers from stomach-related issues?
# Round the result to the third decimal place.
#print(f"The answer to the 2nd question is {round((general_df.loc[(general_df['hospital'] == 'general') & (general_df['diagnosis'] == 'stomach')].shape[0] / general_df.loc[general_df['hospital'] == 'general'].shape[0]), 3)}")

#What share of the patients in the sports hospital suffers from dislocation-related issues?
# Round the result to the third decimal place.
#print(f"The answer to the 3rd question is {round((general_df.loc[(general_df['hospital'] == 'sports') & (general_df['diagnosis'] == 'dislocation')].shape[0] / general_df.loc[general_df['hospital'] == 'sports'].shape[0]), 3)}")

#What is the difference in the median ages of the patients in the general and sports hospitals?
#print(f"The answer to the 4th question is {general_df[general_df['hospital'] == 'general'].age.median() - general_df[general_df['hospital'] == 'sports'].age.median()} ")

#After data processing at the previous stages, the blood_test column has three values: t = a blood test was taken,
# f = a blood test wasn't taken, and 0 = there is no information.
# In which hospital the blood test was taken the most often (there is the biggest number of t in the
# blood_test column among all the hospitals)? How many blood tests were taken?
#print(f"The answer to the 5th question is {general_df[general_df['blood_test'] == 't'].groupby('hospital')['blood_test'].count().idxmax()}, {general_df[general_df['blood_test'] == 't'].groupby('hospital')['blood_test'].value_counts().max()} blood tests")

# What is the most common age of a patient among all hospitals?
age = general_df['age']
bin = [0, 15,35, 55, 70, 80]
values, bins, bars = plt.hist(age, edgecolor='black', bins=bin)
plt.show()
common_age = values.argmax()
print(f"The answer to the 1st question: {bins[common_age]}-{bins[common_age + 1]}")

#What is the most common diagnosis among patients in all hospitals?
diagnosis = general_df['diagnosis'].value_counts()
plt.pie(diagnosis, labels=diagnosis.index.tolist(), autopct='%1.1f%%')
plt.show()
common_diagnosis = diagnosis.index.tolist()[0]
print(f"The answer to the 2nd question: {common_diagnosis}")

# Build a violin plot of height distribution by hospitals.
# What is the main reason for the gap in values? Why there are two peaks,
# which correspond to the relatively small and big values?
height_general = general_df.loc[general_df['hospital'] == 'general', 'height']
height_sports = general_df.loc[general_df['hospital'] == 'sports', 'height']
height_prenatal = general_df.loc[general_df['hospital'] == 'prenatal', 'height']
height = [height_general, height_sports, height_prenatal]
fig, axes = plt.subplots()
axes.set_xticks((1, 2, 3))
axes.set_xticklabels(("General","Sports", "Prenatal"))
axes.set_ylabel("Height")
plt.violinplot(height)
plt.show()
print(f"The answer to the 3rd question: difference in because the sports hospital will mostly have adult patients")

# Sample 20 rows from the DataFrame with a fixed random state for reproducibility
general_df = general_df.sample(n=20, random_state=30)

# Print the first 20 rows of the sampled DataFrame
# pd.set_option('display.max_columns', None)
# print(general_df.head(20))