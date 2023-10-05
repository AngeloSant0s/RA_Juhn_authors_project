#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:15:16 2023

@author: jordanholbrook
"""

import pandas as pd
import matplotlib.pyplot as plt


books = pd.read_csv(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/extended_books_panel.csv")  

authors = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/cre_demo_bs_v1.xlsx")

###############################################################################
###############################################################################


'''
Create Authors Share Figure Raw Data - No Averages
'''

# Merge 'books' and 'authors' DataFrames on 'author_id'
merged_df = books.merge(authors[['author_iddemo', 'gender']], on='author_iddemo', how='left')

# Group by 'year' and 'gender' to count the number of male and female authors each year
author_counts = merged_df.groupby(['year', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) each year
author_counts['total'] = author_counts['female'] + author_counts['male']

# Calculate the male and female share as a percentage of the total authors
author_counts['male_share'] = (author_counts['male'] / author_counts['total']) * 100
author_counts['female_share'] = (author_counts['female'] / author_counts['total']) * 100

# Plot the male and female author share for each year
plt.figure(figsize=(12, 6))
#plt.plot(author_counts.index, author_counts['male_share'], label='Male Share', marker='o')
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
#plt.plot(author_counts.index, author_counts['male_share'], label='Male Share', marker='o')
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
#plt.plot(author_counts.index, author_counts['male_share'], label='Male Share', marker='o')
plt.plot(author_counts.index, author_counts['female_share'], label='Female Share', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('Male and Female Author Share on NYT Best Seller List for Non-Fiction Books Each Year')
plt.legend()
plt.grid(True)
plt.show()


###############################################################################
###############################################################################

'''
Rolling Average Female Shares
'''


# Create a function to calculate 5-year rolling averages for author shares
def calculate_5_year_averages(df):
    rolling_averages = df.rolling(window=5).mean()
    return rolling_averages

# Filter for fiction books
fiction_df = merged_df[merged_df['fiction'] == 1]

# Group by 'year' and 'gender' to count the number of male and female authors each year for fiction books
fiction_author_counts = fiction_df.groupby(['year', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) each year for fiction books
fiction_author_counts['total'] = fiction_author_counts['female'] + fiction_author_counts['male']

# Calculate the male and female share as a percentage of the total authors for fiction books
fiction_author_counts['male_share'] = (fiction_author_counts['male'] / fiction_author_counts['total']) * 100
fiction_author_counts['female_share'] = (fiction_author_counts['female'] / fiction_author_counts['total']) * 100

# Calculate 5-year rolling averages for fiction books
fiction_averages_df = calculate_5_year_averages(fiction_author_counts[['male_share', 'female_share']])

# Filter for non-fiction books
non_fiction_df = merged_df[merged_df['fiction'] == 0]

# Group by 'year' and 'gender' to count the number of male and female authors each year for non-fiction books
non_fiction_author_counts = non_fiction_df.groupby(['year', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) each year for non-fiction books
non_fiction_author_counts['total'] = non_fiction_author_counts['female'] + non_fiction_author_counts['male']

# Calculate the male and female share as a percentage of the total authors for non-fiction books
non_fiction_author_counts['male_share'] = (non_fiction_author_counts['male'] / non_fiction_author_counts['total']) * 100
non_fiction_author_counts['female_share'] = (non_fiction_author_counts['female'] / non_fiction_author_counts['total']) * 100

# Calculate 5-year rolling averages for non-fiction books
non_fiction_averages_df = calculate_5_year_averages(non_fiction_author_counts[['male_share', 'female_share']])

# Plot 5-year rolling averages for both fiction and non-fiction books
plt.figure(figsize=(12, 6))
#plt.plot(fiction_averages_df.index, fiction_averages_df['male_share'], label='Fiction Male Share (5-year average)', marker='o')
plt.plot(fiction_averages_df.index, fiction_averages_df['female_share'], label='Fiction Female Share (5-year average)', marker='o')
#plt.plot(non_fiction_averages_df.index, non_fiction_averages_df['male_share'], label='Non-Fiction Male Share (5-year average)', marker='o')

plt.plot(non_fiction_averages_df.index, non_fiction_averages_df['female_share'], label='Non-Fiction Female Share (5-year average)', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('5-Year Average Female Author Share on NYT Best Seller List')
plt.legend()
plt.grid(True)
plt.show()


# Assuming 'merged_df' is your DataFrame
year_1931_df = merged_df[merged_df['year'] == 1931]
