#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 08:28:10 2023

@author: jordanholbrook
"""


import pandas as pd
import matplotlib.pyplot as plt
import logging
import numpy as np


books = pd.read_stata(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/library_of_congress_data/books_dataset_filtered.dta")  

authors_loc = pd.read_stata(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/library_of_congress_data/authors_dataset_loc_filtered.dta")

authors_loc['female'] = (authors_loc['gender'] == 'female').astype(int)
authors_loc['male'] = (authors_loc['gender'] == 'male').astype(int)

sum_stats = authors_loc[['female','male','birth_year','death_year','audience','audiencel','audienceu','fs_pub','married','childs','total_books']].describe()


# Filter the DataFrame to include authors with birth year >= 1900 and non-missing gender
filtered_authors = authors_loc[(authors_loc['birth_year'] >= 1900) & (authors_loc['gender'].notna())]
filtered_authors = authors_loc[(authors_loc['gender'].notna())]

# Calculate summary statistics on the filtered DataFrame
sum_stats_filtered = filtered_authors[['female', 'male', 'birth_year', 'death_year', 'audience', 'audiencel', 'audienceu', 'married', 'childs', 'total_books']].describe()
sum_stats_filtered = sum_stats_filtered.transpose()
sum_stats_filtered = sum_stats_filtered[['count','mean','std','min','max']]
sum_stats_filtered = sum_stats_filtered.round(2)

latex_table = sum_stats_filtered.to_latex()

# Save the LaTeX table to a .tex file
with open('loc_summary_stats_table.tex', 'w') as f:
    f.write(latex_table)


# Create separate DataFrames for male and female subsamples
male_authors = filtered_authors[filtered_authors['gender'] == 'male']
female_authors = filtered_authors[filtered_authors['gender'] == 'female']

# Calculate summary statistics for the male subsample
male_sum_stats = male_authors[['female', 'male', 'birth_year', 'death_year', 'audience', 'audiencel', 'audienceu', 'married', 'childs', 'total_books']].describe()
male_sum_stats = male_sum_stats.transpose()
male_sum_stats = male_sum_stats[['count', 'mean', 'std', 'min', 'max']]

# Calculate summary statistics for the female subsample
female_sum_stats = female_authors[['female', 'male', 'birth_year', 'death_year', 'audience', 'audiencel', 'audienceu', 'married', 'childs', 'total_books']].describe()
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
with open('loc_combined_gender_sum_stats.tex', 'w') as f:
    f.write(latex_table)
    
    
    
    


# Assuming your dataset is stored in a variable called 'authors'
# Replace 'authors' with the actual variable name if it's different

# Calculate the total number of rows in the dataset
total_rows = len(authors)

# Create a DataFrame to store the missing data report
missing_data_report = pd.DataFrame(columns=['Column', 'Total Missing', 'Percentage Missing'])

# Iterate through each column in the dataset
for column in authors.columns:
    # Calculate the number of missing values in the column
    missing_count = authors[column].isnull().sum()
    
    # Calculate the percentage of missing values
    percentage_missing = (missing_count / total_rows) * 100
    
    # Append the results to the missing data report DataFrame
    missing_data_report = missing_data_report.append({'Column': column,
                                                      'Total Missing': missing_count,
                                                      'Percentage Missing': percentage_missing},
                                                     ignore_index=True)

# Sort the missing data report by the percentage missing in descending order
missing_data_report = missing_data_report.sort_values(by='Percentage Missing', ascending=False)

# Display the missing data report
print(missing_data_report)


import pandas as pd
import numpy as np

# Assuming your dataset is stored in a variable called 'authors'
# Replace 'authors' with the actual variable name if it's different

# Replace 'None' values with actual NaN values
authors.replace('None', np.nan, inplace=True)

# Calculate the total number of rows in the dataset
total_rows = len(authors)

# Create a DataFrame to store the missing data report
missing_data_report = pd.DataFrame(columns=['Column', 'Total Missing', 'Percentage Missing'])

# Iterate through each column in the dataset
for column in authors.columns:
    # Calculate the number of missing values in the column
    missing_count = authors[column].isnull().sum()
    
    # Calculate the percentage of missing values
    percentage_missing = (missing_count / total_rows) * 100
    
    # Append the results to the missing data report DataFrame
    missing_data_report = missing_data_report.append({'Column': column,
                                                      'Total Missing': missing_count,
                                                      'Percentage Missing': percentage_missing},
                                                     ignore_index=True)

# Sort the missing data report by the percentage missing in descending order
missing_data_report = missing_data_report.sort_values(by='Percentage Missing', ascending=False)


# Configure the logging module to write to a log file

logging.basicConfig(filename='missing_data_report.log', level=logging.INFO)
# Write the missing data report to the log file
with open('missing_data_report.log', 'a') as log_file:
    log_file.write('\nMissing Data Report for Specific Columns:\n')
    log_file.write(missing_data_report.to_string(index=False))
    log_file.write('\n\n')
    
# Display the missing data report
print(missing_data_report)

authors['female'] = (authors['gender'] == 'female').astype(int)
authors['male'] = (authors['gender'] == 'male').astype(int)

sum_stats = authors[['female','male','bt_year','dt_year','audience','audiencel','audienceu','fs_pub','married','childs','total_books']].describe()
sum_stats = sum_stats.transpose()


latex_table = sum_stats.to_latex()

# Save the LaTeX table to a .tex file
with open('summary_stats_table.tex', 'w') as f:
    f.write(latex_table)



# List of categorical columns
categorical_columns = ['nets', 'ROLES', 'occup', 'ams_label', 'nationaly', 'coats']


    


# List of categorical columns
categorical_columns = ['nets', 'ROLES', 'occup', 'ams_label', 'nationaly', 'coats']

# Loop through the categorical columns
for column in categorical_columns:
    # Create a new binary column with "has_" prefix
    new_column_name = 'has_' + column
    authors[new_column_name] = authors[column].notna().astype(int)

# Fill NaN values in the new binary columns with 0s
authors[['has_' + column for column in categorical_columns]] = authors[['has_' + column for column in categorical_columns]].fillna(0)

# Display the first few rows of the updated DataFrame
print(authors.head())

authors1 = authors[['has_nets', 'has_ROLES','has_occup', 'has_ams_label', 'has_nationaly', 'has_coats']].fillna(0)
# Display the first few rows of the updated DataFrame
print(authors.head())
sum_stats1 = authors1[['has_nets', 'has_ROLES','has_occup', 'has_ams_label', 'has_nationaly', 'has_coats']].describe()
sum_stats1 = sum_stats1.transpose()


