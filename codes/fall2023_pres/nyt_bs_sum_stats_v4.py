#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:45:47 2023

@author: jordanholbrook
"""


books = pd.read_csv('/Users/jordanholbrook/extended_books_panel_v2.csv')



authors['college'] = authors['almamater'].notna()

authors['female'] = (authors['gender'] == 'female').astype(int)

authors['male'] = (authors['gender'] == 'male').astype(int)





import pandas as pd

# Assuming 'books' is your DataFrame
books.rename(columns={'author_iddemo_x': 'author_iddemo'}, inplace=True)

# Now, 'author_iddemo_x' has been renamed to 'author_iddemo' in the 'books' DataFrame

# Calculate the number of books each author has written
number_books = books.groupby('author_iddemo')['book_id'].nunique().reset_index()
number_books.rename(columns={'book_id': 'number_books'}, inplace=True)

# Calculate the total number of weeks each author has spent on the best sellers list
#num_weeks = books.groupby('author_iddemo')['number_of_weeks'].max().reset_index()
num_weeks = books.groupby('author_iddemo')['number_of_weeks'].count().reset_index()

# Merge the 'number_books' and 'num_weeks' DataFrames with the 'authors' DataFrame
authors = authors.merge(number_books, on='author_iddemo', how='left')
authors = authors.merge(num_weeks, on='author_iddemo', how='left')

sum_stats = authors[['female','male','birth_year','death_year','num_children','has_spouse','has_children','college','number_books','number_of_weeks']].describe()
sum_stats = sum_stats.transpose()
import pandas as pd

# Check if 'alma mater' is not empty and assign 1, otherwise assign a missing value
authors['college'] = authors['almamater'].apply(lambda x: 1 if pd.notna(x) else np.nan)

sum_stats = sum_stats.transpose()
sum_stats = sum_stats [['count','mean','std','min','50%','max']]
sum_stats = sum_stats.round(2)


latex_table = sum_stats.to_latex()

# Save the LaTeX table to a .tex file
with open('nytbs_summary_stats_table_v5.tex', 'w') as f:
    f.write(latex_table)


# Create separate DataFrames for male and female subsamples
male_authors = authors[authors['gender'] == 'male']
female_authors = authors[authors['gender'] == 'female']

# Calculate summary statistics for the male subsample
male_sum_stats = male_authors[['female', 'male', 'birth_year', 'death_year', 'num_children', 'has_spouse', 'has_children', 'college','number_books','number_of_weeks']].describe()
male_sum_stats = male_sum_stats.transpose()
male_sum_stats = male_sum_stats[['count', 'mean', 'std','50%', 'min', 'max']]

# Calculate summary statistics for the female subsample
female_sum_stats = female_authors[['female', 'male', 'birth_year', 'death_year', 'num_children', 'has_spouse', 'has_children', 'college','number_books','number_of_weeks']].describe()
female_sum_stats = female_sum_stats.transpose()
female_sum_stats = female_sum_stats[['count', 'mean', 'std','50%', 'min', 'max']]

# Assuming you already have 'male_sum_stats' and 'female_sum_stats' DataFrames

# Drop 'male' and 'female' rows from the DataFrames
male_sum_stats = male_sum_stats.drop(['male', 'female'])
female_sum_stats = female_sum_stats.drop(['male', 'female'])

# Concatenate the DataFrames vertically
combined_sum_stats = pd.concat([male_sum_stats, female_sum_stats])
combined_sum_stats[['mean', 'std', '50%', 'min', 'max']] = combined_sum_stats[['mean', 'std', '50%', 'min', 'max']].round(2)

combined_sum_stats = combined_sum_stats[['mean', 'std','50%', 'min', 'max']].round(2)

# Export the combined summary statistics to a LaTeX table
latex_table = combined_sum_stats.to_latex()

# Save the LaTeX table to a file (e.g., 'summary_stats.tex')
with open('bs_combined_gender_sum_stats_v5.tex', 'w') as f:
    f.write(latex_table)

