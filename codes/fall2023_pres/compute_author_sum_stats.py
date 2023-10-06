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
num_weeks = books.groupby('author_iddemo')['number_of_weeks'].max().reset_index()

# Merge the 'number_books' and 'num_weeks' DataFrames with the 'authors' DataFrame
authors = authors.merge(number_books, on='author_iddemo', how='left')
authors = authors.merge(num_weeks, on='author_iddemo', how='left')

# Fill NaN values with 0 in case some authors have no books or weeks on the best sellers list
authors['number_books'].fillna(0, inplace=True)
authors['number_of_weeks'].fillna(0, inplace=True)


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


latex_table = sum_stats.to_latex()

# Save the LaTeX table to a .tex file
with open('summary_stats_table.tex', 'w') as f:
    f.write(latex_table)


