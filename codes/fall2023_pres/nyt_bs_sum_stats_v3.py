#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:54:27 2023

@author: jordanholbrook
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



authors = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/cre_demo_bs_v1.xlsx")


authors['college'] = authors['almamater'].notna()

authors['female'] = (authors['gender'] == 'female').astype(int)

authors['male'] = (authors['gender'] == 'male').astype(int)


sum_stats = authors[['female','male','birth_year','death_year','num_children','has_spouse','has_children','college']].describe()
sum_stats = sum_stats.transpose()
import pandas as pd

# Check if 'alma mater' is not empty and assign 1, otherwise assign a missing value
authors['college'] = authors['almamater'].apply(lambda x: 1 if pd.notna(x) else np.nan)

sum_stats = sum_stats.transpose()
sum_stats = sum_stats [['count','mean','std','min','max']]
sum_stats = sum_stats.round(2)

latex_table = sum_stats.to_latex()
# Save the LaTeX table to a file (e.g., 'summary_stats.tex')
with open('bs_sum_stats_v3.tex', 'w') as f:
    f.write(latex_table)

# Create separate DataFrames for male and female subsamples
male_authors = authors[authors['gender'] == 'male']
female_authors = authors[authors['gender'] == 'female']

# Calculate summary statistics for the male subsample
male_sum_stats = male_authors[['female', 'male', 'birth_year', 'death_year', 'num_children', 'has_spouse', 'has_children', 'college','US_citizen']].describe()
male_sum_stats = male_sum_stats.transpose()
male_sum_stats = male_sum_stats[['count', 'mean', 'std', 'min', 'max']]

# Calculate summary statistics for the female subsample
female_sum_stats = female_authors[['female', 'male', 'birth_year', 'death_year', 'num_children', 'has_spouse', 'has_children', 'college','US_citizen']].describe()
female_sum_stats = female_sum_stats.transpose()
female_sum_stats = female_sum_stats[['count', 'mean', 'std', 'min', 'max']]


import pandas as pd

# Assuming you already have 'male_sum_stats' and 'female_sum_stats' DataFrames

# Drop 'male' and 'female' rows from the DataFrames
male_sum_stats = male_sum_stats.drop(['male', 'female'])
female_sum_stats = female_sum_stats.drop(['male', 'female'])

# Concatenate the DataFrames vertically
combined_sum_stats = pd.concat([male_sum_stats, female_sum_stats])
combined_sum_stats = combined_sum_stats.round(2)

# Export the combined summary statistics to a LaTeX table
latex_table = combined_sum_stats.to_latex()

# Save the LaTeX table to a file (e.g., 'summary_stats.tex')
with open('bs_combined_gender_sum_stats.tex', 'w') as f:
    f.write(latex_table)



import pandas as pd

# Create the 'US_citizen' variable (case-insensitive and robust to spelling)
authors['US_citizen'] = authors['nationality'].str.lower().str.contains('united states', case=False).astype(int)

import pandas as pd

# Create the 'US_citizen' variable (case-insensitive and robust to spelling)
authors['US_citizen'] = authors['nationality'].str.lower().fillna('').str.contains('united states', case=False).astype(int)



import pandas as pd

# Create the 'US_citizen' variable (case-insensitive and robust to spelling)
authors['US_citizen'] = authors['nationality'].str.lower().apply(lambda x: x == 'united states' if pd.notna(x) else np.nan)

import pandas as pd

# Create the 'US_citizen' variable (case-insensitive and robust to spelling)
authors['US_citizen'] = authors.apply(lambda row: 1 if pd.notna(row['nationality']) and 'united states' in row['nationality'].lower() else np.nan, axis=1)

import pandas as pd

# Create the 'US_citizen' variable (case-insensitive and robust to spelling)
authors['US_citizen'] = authors.apply(lambda row: 1 if pd.notna(row['nationality']) and 'united states' in row['nationality'].lower() else (0 if pd.notna(row['nationality']) else np.nan), axis=1)


# Calculate the percentage of male authors who are U.S. citizens with nationality information
total_male_authors = len(authors[(authors['gender'] == 'male') & (authors['nationality'].notna())])
us_citizen_male = len(authors[(authors['gender'] == 'male') & (authors['US_citizen'] == 1) & (authors['nationality'].notna())])
percent_us_citizen_male = (us_citizen_male / total_male_authors) * 100

# Calculate the percentage of female authors who are U.S. citizens with nationality information
total_female_authors = len(authors[(authors['gender'] == 'female') & (authors['nationality'].notna())])
us_citizen_female = len(authors[(authors['gender'] == 'female') & (authors['US_citizen'] == 1) & (authors['nationality'].notna())])
percent_us_citizen_female = (us_citizen_female / total_female_authors) * 100

print(f"Percentage of male authors who are U.S. citizens: {percent_us_citizen_male:.2f}%")
print(f"Percentage of female authors who are U.S. citizens: {percent_us_citizen_female:.2f}%")
