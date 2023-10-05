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
#plt.plot(author_counts.index, author_counts['male_share'], label='Male Share', marker='o')
plt.plot(author_counts.index, author_counts['female_share'], label='Female Share', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('Female Author Share on NYT Best Seller List Each Year')
plt.legend()
plt.grid(True)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Your code to merge and calculate author counts here...

# Calculate 5-year averages for male and female author shares
averages_df = author_counts[['male_share', 'female_share']].rolling(window=5).mean()

# Plot the male and female author share 5-year averages
plt.figure(figsize=(12, 6))
#plt.plot(averages_df.index, averages_df['male_share'], label='Male Share (5-year average)', marker='o')
plt.plot(averages_df.index, averages_df['female_share'], label='Female Share (5-year average)', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('5-Year Average Female Author Share on NYT Best Seller List')
plt.legend()
plt.grid(True)
plt.show()





import pandas as pd
import matplotlib.pyplot as plt

# Your code to merge 'books' and 'authors' DataFrames here...

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
#plt.plot(averages_df.index, averages_df['female_share'], label='Female Share (5-year average)', marker='o')

#plt.plot(non_fiction_averages_df.index, non_fiction_averages_df['female_share'], label='Non-Fiction Female Share (5-year average)', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('5-Year Average Female Author Share on NYT Best Seller List')
plt.legend()
plt.grid(True)
plt.show()


authors['college'] = authors['alama_mater'] not nan
import pandas as pd

# Assuming you already have the 'authors' DataFrame

# Create the 'college' variable based on 'alama_mater' not being NaN
authors['college'] = authors['almamater'].notna()

# The 'college' column will contain True where 'alama_mater' is not NaN and False where it is NaN

x =authors.describe()


# Assuming you have a 'books' DataFrame with 'author_id' and 'num_weeks' columns
# You may need to adjust the column names based on your actual DataFrame

# Calculate the number of books each author has written
number_books = books.groupby('author_id')['book_id'].nunique().reset_index()
number_books.rename(columns={'book_id': 'number_books'}, inplace=True)

# Calculate the total number of weeks each author has spent on the best sellers list
num_weeks = books.groupby('author_id')['num_weeks'].sum().reset_index()

# Merge the 'number_books' and 'num_weeks' DataFrames with the 'authors' DataFrame
authors = authors.merge(number_books, on='author_id', how='left')
authors = authors.merge(num_weeks, on='author_id', how='left')

# Fill NaN values with 0 in case some authors have no books or weeks on the best sellers list
authors['number_books'].fillna(0, inplace=True)
authors['num_weeks'].fillna(0, inplace=True)


# Assuming you have a 'books' DataFrame with 'author_id' and 'number_of_weeks' columns

# Calculate the total number of weeks each author has spent on the best sellers list
author_weeks = books.groupby('author_id')['number_of_weeks'].max().reset_index()

# Rename the 'number_of_weeks' column to 'total_weeks_on_list' for clarity
author_weeks.rename(columns={'number_of_weeks': 'total_weeks_on_list'}, inplace=True)

# Merge the 'author_weeks' DataFrame with the 'authors' DataFrame
authors = authors.merge(author_weeks, on='author_id', how='left')

# Fill NaN values with 0 in case some authors have no weeks on the best sellers list
authors['total_weeks_on_list'].fillna(0, inplace=True)





import numpy as np
# Assuming df is your DataFrame
books.replace('--', np.nan, inplace=True)


import pandas as pd

expanded_df2 = pd.DataFrame(columns=df2.columns)

for index, row in df2.iterrows():
    authors = row['author1'], row['author2'], row['author3'], row['author4'], row['author5']
    for author in authors:
        if not pd.isnull(author):
            expanded_df2 = expanded_df2.append(row)

books = books.head(100)

import pandas as pd

# Initialize an empty DataFrame to store the transformed data
transformed_books = pd.DataFrame(columns=books.columns)

# Iterate through each row of the original DataFrame
for index, row in books.iterrows():
    # Extract information for the first author
    author_info = {
        'author1': row['author1'],
        'author2': None,
        'author3': None,
        'author4': None,
        'author5': None,
    }
    transformed_books = transformed_books.append(author_info, ignore_index=True)
    
    # Iterate through the remaining authors (if any)
    for col_num in range(2, 6):
        author_col = f'author{col_num}'
        author_name = row[author_col]
        if not pd.isnull(author_name):
            author_info['author1'] = author_name
            transformed_books = transformed_books.append(author_info, ignore_index=True)

# You can reset the index of the transformed DataFrame if needed
transformed_books.reset_index(drop=True, inplace=True)

import pandas as pd
import numpy as np

# Assuming df2 is your original DataFrame
# Replace '--' with NaN
df2.replace('--', np.nan, inplace=True)

# Initialize an empty DataFrame to store the transformed data
transformed_books = pd.DataFrame(columns=df2.columns)

# Iterate through each row of the original DataFrame
for index, row in df2.iterrows():
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



combine = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/new_york_time_best_sellers_data/best_sellers_authors_books_combined.xlsx")  

combine = combine[['author_name', 'author_id']]
combine = combine.rename(columns = {'author_name' : 'author1'})
combine = combine.groupby(['author1']).first().reset_index()

