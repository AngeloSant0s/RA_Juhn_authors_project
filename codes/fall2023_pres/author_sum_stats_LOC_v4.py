#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:55:53 2023

@author: jordanholbrook
"""


import pandas as pd
import matplotlib.pyplot as plt
import logging
import numpy as np
import os


# books = pd.read_stata(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/library_of_congress_data/books_dataset_filtered.dta")  
# authors_loc = pd.read_stata(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/library_of_congress_data/authors_dataset_loc_filtered.dta")

os.chdir('/Users/angelosantos/Library/CloudStorage/Dropbox-UH-ECON/authors_project_jordan_angelo/library_of_congress_data')
authors_loc = pd.read_stata('authors_dataset_loc_filtered.dta')

authors_loc['female'] = (authors_loc['gender'] == 'female').astype(int)
authors_loc['male'] = (authors_loc['gender'] == 'male').astype(int)

sum_stats = authors_loc[['female','male','birth_year','death_year','audience','audiencel','audienceu','fs_pub','married','childs','total_books']].describe()


# Filter the DataFrame to include authors with birth year >= 1900 and non-missing gender
filtered_authors = authors_loc[(authors_loc['birth_year'] >= 1900) & (authors_loc['gender'].notna())]
filtered_authors = authors_loc[(authors_loc['birth_year'] >= 1900) & (authors_loc['gender'] != 'None')]
filtered_authors = authors_loc[(authors_loc['gender'] != 'None') & (authors_loc['pub_year'] >=  1900)]
filtered_authors = authors_loc[(authors_loc['gender'] != 'None')]

# Calculate summary statistics on the filtered DataFrame
sum_stats_filtered = filtered_authors[['female', 'male', 'birth_year', 'death_year', 'audience', 'audiencel', 'audienceu', 'married', 'childs', 'total_books']].describe()
sum_stats_filtered = sum_stats_filtered.transpose()
sum_stats_filtered = sum_stats_filtered[['count','mean','std','50%','min','max']]
sum_stats_filtered = sum_stats_filtered.rename(columns={'50%' : 'Median'})
sum_stats_filtered = sum_stats_filtered.round(2)

latex_table = sum_stats_filtered.to_latex()

# Save the LaTeX table to a .tex file
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/tables/summary_stats')
with open('loc_summary_stats_table_non_gender_missing.tex', 'w') as f:
    f.write(latex_table)


# Create separate DataFrames for male and female subsamples
male_authors = filtered_authors[filtered_authors['gender'] == 'male']
female_authors = filtered_authors[filtered_authors['gender'] == 'female']

# Calculate summary statistics for the male subsample
male_sum_stats = male_authors[['female', 'male', 'birth_year', 'death_year', 'audience', 'audiencel', 'audienceu', 'married', 'childs', 'total_books']].describe()
male_sum_stats = male_sum_stats.transpose()
male_sum_stats = male_sum_stats[['count', 'mean', 'std','50%', 'min', 'max']]
male_sum_stats = male_sum_stats.rename(columns={'50%' : 'Median'})


# Calculate summary statistics for the female subsample
female_sum_stats = female_authors[['female', 'male', 'birth_year', 'death_year', 'audience', 'audiencel', 'audienceu', 'married', 'childs', 'total_books']].describe()
female_sum_stats = female_sum_stats.transpose()
female_sum_stats = female_sum_stats[['count', 'mean', 'std', '50%', 'min', 'max']]
female_sum_stats = female_sum_stats.rename(columns={'50%' : 'Median'})


import pandas as pd

# Assuming you already have 'male_sum_stats' and 'female_sum_stats' DataFrames

# Drop 'male' and 'female' rows from the DataFrames
# male_sum_stats = male_sum_stats.drop(['male', 'female'])
male_sum_stats = male_sum_stats.drop(['female'])

# female_sum_stats = female_sum_stats.drop(['male', 'female'])
female_sum_stats = female_sum_stats.drop(['male'])

# Concatenate the DataFrames vertically
combined_sum_stats = pd.concat([male_sum_stats, female_sum_stats])
combined_sum_stats = combined_sum_stats.round(2)

# Export the combined summary statistics to a LaTeX table
latex_table = combined_sum_stats.to_latex()

# Save the LaTeX table to a file (e.g., 'summary_stats.tex')
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/tables/summary_stats')
with open('loc_combined_gender_sum_stats_non_gender_missing.tex', 'w') as f:
    f.write(latex_table)
    
    
    

