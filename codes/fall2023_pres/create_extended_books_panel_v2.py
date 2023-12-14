#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:33:44 2023

@author: jordanholbrook
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

new_working_directory = '/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs'

# Change the working directory
os.chdir(new_working_directory)


books = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/book_view_new.xlsx")  
authors = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/cre_demo_bs_v1.xlsx")



# Replace '--' with NaN
books.replace('--', np.nan, inplace=True)

# Initialize an empty DataFrame to store the transformed data
transformed_books = pd.DataFrame(columns=books.columns)

# Iterate through each row of the original DataFrame
for index, row in books.iterrows():
    # Iterate through each author column
    for col_num in range(1, 6):
        author_col = f'author{col_num}'
        author_name = row[author_col]
        
        # Create a new row for each author with the author's name
        if not pd.isnull(author_name):
            new_row = row.copy()  # Create a copy of the original row
            new_row['author'] = author_name  # Add a new 'author' column
            transformed_books = transformed_books.append(new_row, ignore_index=True)

# Reset the index of the transformed DataFrame
transformed_books.reset_index(drop=True, inplace=True)


# Count total authors
total_authors = books[['author1', 'author2', 'author3', 'author4', 'author5']].count().sum()


if transformed_books.shape[0] == total_authors:
    print("All authors accounted for")


# Assuming 'authors' and 'transformed_books' are your DataFrames
transformed_books = transformed_books.merge(authors[['author_iddemo', 'author_name']], left_on='author', right_on='author_name', how='left')

# Drop the 'author_name' column if you don't need it in the final DataFrame
transformed_books.drop(columns=['author_name'], inplace=True)


transformed_books.to_csv("extended_books_panel_v2.csv")



import pandas as pd

# Assuming 'authors' and 'transformed_books' are your DataFrames
transformed_books = transformed_books.merge(authors[['author_iddemo', 'author_name']], left_on='author', right_on='author_name', how='left')

# Count the number of merged and unmerged observations
merged_count = transformed_books['author_iddemo'].notnull().sum()
unmerged_count = transformed_books['author_iddemo'].isnull().sum()

# Print the summary report
print("Summary of the merge:")
print(f"Total observations in 'transformed_books': {len(transformed_books)}")
print(f"Number of observations merged: {merged_count}")
print(f"Number of observations not merged: {unmerged_count}")

# Drop the 'author_name' column if you don't need it in the final DataFrame
transformed_books.drop(columns=['author_name'], inplace=True)


import pandas as pd

# Assuming 'books' is your DataFrame
# Create a Series containing all the author names
all_authors = pd.concat([books['author1'], books['author2'], books['author3'], books['author4'], books['author5']])

# Count the number of unique authors
unique_authors_count = all_authors.nunique()

print("Number of unique authors:", unique_authors_count)







import pandas as pd

# Assuming 'authors' and 'transformed_books' are your DataFrames
transformed_books = transformed_books.merge(authors[['author_iddemo', 'author_name']], left_on='author', right_on='author_name', how='left')

# Count the number of unmerged observations from the 'authors' dataset
unmerged_authors_count = authors['author_iddemo'].isnull().sum()

# Print the count of unmerged authors
print(f"Number of authors from 'authors' dataset that were not merged: {unmerged_authors_count}")

# Drop the 'author_name' column if you don't need it in the final DataFrame
transformed_books.drop(columns=['author_name'], inplace=True)









