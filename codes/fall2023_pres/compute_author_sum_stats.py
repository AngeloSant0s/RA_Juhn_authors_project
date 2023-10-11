#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:05:07 2023

@author: jordanholbrook
"""

import pandas as pd
import matplotlib.pyplot as plt



books = pd.read_csv(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/extended_books_panel.csv")  

authors = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/cre_demo_bs_v1.xlsx")

###############################################################################
###############################################################################


# Merge 'books' and 'authors' DataFrames on 'author_id'
#merged_df = books.merge(authors[['author_iddemo', 'gender']], on='author_iddemo', how='left')


# Calculate the number of books each author has written
number_books = books.groupby('author_iddemo')['book_id'].nunique().reset_index()
number_books.rename(columns={'book_id': 'number_books'}, inplace=True)

# Calculate the total number of weeks each author has spent on the best sellers list
#num_weeks = books.groupby('author_iddemo')['number_of_weeks'].max().reset_index()
num_weeks = books.groupby('author_iddemo')['number_of_weeks'].count().reset_index()

# Merge the 'number_books' and 'num_weeks' DataFrames with the 'authors' DataFrame
authors = authors.merge(number_books, on='author_iddemo', how='left')
authors = authors.merge(num_weeks, on='author_iddemo', how='left')

# Fill NaN values with 0 in case some authors have no books or weeks on the best sellers list
#authors['number_books'].fillna(0, inplace=True)
#authors['number_of_weeks'].fillna(0, inplace=True)
#

# Perform the merge with indicator=True
#merged_df = pd.merge(books, authors[['author_iddemo', 'gender']], left_on='author_iddemo', right_on='author_iddemo', how='left', indicator=True)
# Filter rows where the author is only in the left DataFrame (books) or only in the right DataFrame (authors)
#unmatched_authors = merged_df[merged_df['_merge'] != 'both']

# Step 1: Group books data by author and find the minimum year
author_first_year = books.groupby('author_iddemo')['year'].min().reset_index()
author_first_year.columns = ['author_iddemo', 'first_year']

# Step 2: Merge the first year data into the author file
authors = authors.merge(author_first_year, on='author_iddemo', how='left')

authors['age_at_bs_pub'] = authors['year']-authors['first_year']

# Create the 'college' variable based on 'alama_mater' not being NaN
authors['college'] = authors['almamater'].notna().astype(int)

authors['Female'] = (authors['gender'] == 'female').astype(int)



sum_stats = authors[['Female','birth_year','death_year','num_children','has_spouse','has_children','college','number_books','number_of_weeks']].describe()


sum_stats = sum_stats.transpose()
sum_stats = sum_stats [['count','mean','std','min','max']]

latex_table = sum_stats.to_latex()

# Save the LaTeX table to a .tex file
with open('summary_stats_table_v2.tex', 'w') as f:
    f.write(latex_table)



# Calculate summary statistics for females
female_summary_stats = authors[authors['Female'] == 1][['birth_year','death_year','num_children','has_spouse','has_children','college','number_books','number_of_weeks']].describe()

# Transpose the female summary stats
female_summary_stats = female_summary_stats.transpose()

# Select only the desired summary statistics columns
female_summary_stats = female_summary_stats[['count','mean','std','min','max']]

# Rename the columns to indicate they are for females
female_summary_stats = female_summary_stats.rename(columns={
    'count': 'Female Count',
    'mean': 'Female Mean',
    'std': 'Female Std',
    'min': 'Female Min',
    'max': 'Female Max'
})

# Calculate summary statistics for males
male_summary_stats = authors[authors['Female'] == 0][['birth_year','death_year','num_children','has_spouse','has_children','college','number_books','number_of_weeks']].describe()

# Transpose the male summary stats
male_summary_stats = male_summary_stats.transpose()

# Select only the desired summary statistics columns
male_summary_stats = male_summary_stats[['count','mean','std','min','max']]

# Rename the columns to indicate they are for males
male_summary_stats = male_summary_stats.rename(columns={
    'count': 'Male Count',
    'mean': 'Male Mean',
    'std': 'Male Std',
    'min': 'Male Min',
    'max': 'Male Max'
})

# Merge the female and male summary stats into a single table
combined_summary_stats = pd.concat([female_summary_stats, male_summary_stats], axis=1)


column_order = ['Female Count', 'Male Count', 'Female Mean', 'Male Mean',
                'Female Std', 'Male Std', 'Female Min', 'Male Min',
                'Female Max', 'Male Max']

# Reorganize the columns in the combined_summary_stats DataFrame
combined_summary_stats = combined_summary_stats[column_order]

# Round the values in the DataFrame to two decimal places
combined_summary_stats = combined_summary_stats.round(2)
# Convert the combined summary stats table to LaTeX format
latex_table = combined_summary_stats.to_latex()

# Save the LaTeX table to a .tex file
with open('combined_summary_stats_table.tex', 'w') as f:
    f.write(latex_table)
    
    
    
# Calculate summary statistics for males
male_summary_stats = authors[authors['Female'] == 0][['birth_year','death_year','num_children','has_spouse','has_children','college','number_books','number_of_weeks']].describe()

# Transpose the male summary stats
male_summary_stats = male_summary_stats.transpose()

# Select only the desired summary statistics columns
male_summary_stats = male_summary_stats[['count','mean','std','min','max']]

# Calculate summary statistics for females
female_summary_stats = authors[authors['Female'] == 1][['birth_year','death_year','num_children','has_spouse','has_children','college','number_books','number_of_weeks']].describe()

# Transpose the female summary stats
female_summary_stats = female_summary_stats.transpose()

# Select only the desired summary statistics columns
female_summary_stats = female_summary_stats[['count','mean','std','min','max']]

# Convert the summary stats tables to LaTeX format
male_latex_table = male_summary_stats.to_latex()
female_latex_table = female_summary_stats.to_latex()

# Save the LaTeX tables to separate .tex files
with open('male_summary_stats_table.tex', 'w') as f:
    f.write(male_latex_table)

with open('female_summary_stats_table.tex', 'w') as f:
    f.write(female_latex_table)







authors_with_112_books = authors[authors['number_books'] == 112]
authors_with_923_weeks = authors[authors['number_of_weeks'] == 923]

# Combine the two DataFrames to get authors with both conditions satisfied
authors_with_both_conditions = authors_with_112_books.merge(authors_with_923_weeks, on='author_name', how='inner')

# Get the names of authors
author_names_with_both_conditions = authors_with_both_conditions['author_name'].tolist()


author_born_in_1684 = authors[authors['birth_year'] == 1684]
author_name_born_in_1684 = author_born_in_1684['author_name'].tolist()


author_died_in_1703 = authors[authors['death_year'] == 1703]
author_name_died_in_1703 = author_died_in_1703['author_name'].tolist()

author_with_24_children = authors[authors['num_children'] == 24]
author_name_with_24_children = author_with_24_children['author_name'].tolist()




# Assuming the author name is stored in one of the 'authorX' columns (author1, author2, author3, etc.)
author_name = "beethoven-"

# Create a boolean mask to filter rows where any of the author columns contains the desired name
mask = books[['author1', 'author2', 'author3', 'author4', 'author5']].apply(lambda x: x.str.lower() == author_name.lower()).any(axis=1)

# Use the mask to filter the rows that match the author name
books_with_author = books[mask]

# Display the books with the specified author name
print(books_with_author)

