#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:12:07 2023

@author: jordanholbrook
"""


import pandas as pd
import matplotlib.pyplot as plt


books = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/new_york_time_best_sellers_data/best_sellers_books_panel.xlsx")  

authors = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/new_york_time_best_sellers_data/best_sellers_authors_data.xlsx")  


'''
Create Authors Share Figure
'''

# Merge 'books' and 'authors' DataFrames on 'author_id'
merged_df = books.merge(authors[['author_id', 'gender']], on='author_id', how='left')

# Group by 'year' and 'gender' to count the number of male and female authors each year
author_counts = merged_df.groupby(['year', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) each year
author_counts['total'] = author_counts['female'] + author_counts['male']

# Calculate the male and female share as a percentage of the total authors
author_counts['male_share'] = (author_counts['male'] / author_counts['total']) * 100
author_counts['female_share'] = (author_counts['female'] / author_counts['total']) * 100

# Plot the male and female author share for each year
plt.figure(figsize=(12, 6))
plt.plot(author_counts.index, author_counts['male_share'], label='Male Share', marker='o')
plt.plot(author_counts.index, author_counts['female_share'], label='Female Share', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('Male and Female Author Share on NYT Best Seller List Each Year')
plt.legend()
plt.grid(True)
plt.show()

'''
Create Authors Share Figrue by Fiction Books
'''

# Merge 'books' and 'authors' DataFrames on 'author_id'
merged_df = books.merge(authors[['author_id', 'gender']], on='author_id', how='left')

# Filter for fiction books
fiction_df = merged_df[merged_df['fiction'] == 1]

# Group by 'year' and 'gender' to count the number of male and female authors each year for fiction books
author_counts = fiction_df.groupby(['year', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) each year for fiction books
author_counts['total'] = author_counts['female'] + author_counts['male']

# Calculate the male and female share as a percentage of the total authors for fiction books
author_counts['male_share'] = (author_counts['male'] / author_counts['total']) * 100
author_counts['female_share'] = (author_counts['female'] / author_counts['total']) * 100

# Plot the male and female author share for each year for fiction books
plt.figure(figsize=(12, 6))
plt.plot(author_counts.index, author_counts['male_share'], label='Male Share', marker='o')
plt.plot(author_counts.index, author_counts['female_share'], label='Female Share', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('Male and Female Author Share on NYT Best Seller List for Fiction Books Each Year')
plt.legend()
plt.grid(True)
plt.show()


'''
Create Authors Share Figure by Non-fiction Books
'''

# Merge 'books' and 'authors' DataFrames on 'author_id'
merged_df = books.merge(authors[['author_id', 'gender']], on='author_id', how='left')

# Filter for non-fiction books
non_fiction_df = merged_df[merged_df['fiction'] == 0]

# Group by 'year' and 'gender' to count the number of male and female authors each year for non-fiction books
author_counts = non_fiction_df.groupby(['year', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) each year for non-fiction books
author_counts['total'] = author_counts['female'] + author_counts['male']

# Calculate the male and female share as a percentage of the total authors for non-fiction books
author_counts['male_share'] = (author_counts['male'] / author_counts['total']) * 100
author_counts['female_share'] = (author_counts['female'] / author_counts['total']) * 100

# Plot the male and female author share for each year for non-fiction books
plt.figure(figsize=(12, 6))
plt.plot(author_counts.index, author_counts['male_share'], label='Male Share', marker='o')
plt.plot(author_counts.index, author_counts['female_share'], label='Female Share', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('Male and Female Author Share on NYT Best Seller List for Non-Fiction Books Each Year')
plt.legend()
plt.grid(True)
plt.show()



