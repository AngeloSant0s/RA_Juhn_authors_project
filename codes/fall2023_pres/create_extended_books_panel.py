#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 23:02:51 2023

@author: jordanholbrook
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

new_working_directory = '/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs'

# Change the working directory
os.chdir(new_working_directory)


books = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/new_york_time_best_sellers_data/best_sellers_books_panel.xlsx")  
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



# Count the number of matched authors with 'author_id'
matched_authors_count = transformed_books['author_id'].notna().sum()

# Print the count of matched authors
print(f"Number of authors matched with an author_id: {matched_authors_count}")

# Calculate the total number of authors in the 'transformed_books' DataFrame
total_authors_count = len(transformed_books)

# Calculate the number of missing authors
missing_authors_count = total_authors_count - matched_authors_count

# Print the count of missing authors
print(f"Number of authors missing an author_id: {missing_authors_count}")


# Drop the 'author_id' column from the 'transformed_books' DataFrame
transformed_books.drop(columns=['author_id'], inplace=True)


# Save the 'transformed_books' DataFrame as a CSV file
transformed_books.to_csv('extended_books_panel.csv', index=False)
