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
# Merge 'books' and 'authors' DataFrames on 'author_id'
merged_df = books.merge(authors[['author_iddemo', 'gender']], on='author_iddemo', how='left')


# Create a function to calculate 5-year rolling averages for author shares
def calculate_5_year_averages(df):
    rolling_averages = df.rolling(window=5).mean()
    return rolling_averages

# Group by 'year' and 'gender' to count the number of male and female authors each year
author_counts = merged_df.groupby(['year', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) each year
author_counts['total'] = author_counts['female'] + author_counts['male']

# Calculate the male and female share as a percentage of the total authors
author_counts['male_share'] = (author_counts['male'] / author_counts['total']) * 100
author_counts['female_share'] = (author_counts['female'] / author_counts['total']) * 100

author_count_averages_df = calculate_5_year_averages(author_counts[['male_share', 'female_share']])


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
plt.plot(fiction_averages_df.index, fiction_averages_df['female_share'], label='Fiction Female Share (5-year average)', marker='o')
plt.plot(non_fiction_averages_df.index, non_fiction_averages_df['female_share'], label='Non-Fiction Female Share (5-year average)', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('5-Year Average Female Author Share on NYT Best Seller List')
plt.legend()
#plt.grid(True)

# Set the y-axis limits to 0 - 50
plt.ylim(0, 50)

plt.show()


# Assuming 'merged_df' is your DataFrame
year_1931_df = merged_df[merged_df['year'] == 1931]




# Filter for years starting from 1950
author_count_averages_df = author_count_averages_df[author_count_averages_df .index >= 1950]
fiction_averages_df = fiction_averages_df[fiction_averages_df.index >= 1950]
non_fiction_averages_df = non_fiction_averages_df[non_fiction_averages_df.index >= 1950]

# Plot 5-year rolling averages for both fiction and non-fiction books
plt.figure(figsize=(12, 6))
plt.plot(author_count_averages_df.index, author_count_averages_df['female_share'], label='Female Share', marker='o')
#plt.plot(fiction_averages_df.index, fiction_averages_df['female_share'], label='Fiction Female Share (5-year average)', marker='o')
#plt.plot(non_fiction_averages_df.index, non_fiction_averages_df['female_share'], label='Non-Fiction Female Share (5-year average)', marker='o')
plt.xlabel('Year')
plt.ylabel('Author Share (%)')
plt.title('5-Year Average Female Author Share on NYT Best Seller List')
plt.legend()
plt.grid(True)

# Set the y-axis limits to 0 - 50
plt.ylim(0, 50)

plt.show()


import matplotlib.pyplot as plt

# Plot 5-year rolling averages for both fiction and non-fiction books
plt.figure(figsize=(12, 6))
plt.plot(author_count_averages_df.index, author_count_averages_df['female_share'], label='Female Share', marker='o')
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Author Share (%)', fontsize=14, fontweight='bold')
plt.title('5-Year Average Female Author Share on NYT Best Seller List', fontsize=16, fontweight='bold')
plt.legend()
plt.grid(True)

# Set the y-axis limits to 0 - 50
plt.ylim(0, 50)

# Increase the font size of x and y ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()


import matplotlib.pyplot as plt

# Plot 5-year rolling averages for both fiction and non-fiction books with a thicker blue line
plt.figure(figsize=(12, 6))
#plt.plot(author_count_averages_df.index, author_count_averages_df['female_share'], label='Female Share', marker='o', color='blue', linestyle='-', linewidth=2.5)
#plt.plot(fiction_averages_df.index, fiction_averages_df['female_share'], label='Fiction Female Share (5-year average)', marker='o', color='blue', linestyle='-', linewidth=2.5)
plt.plot(non_fiction_averages_df.index, non_fiction_averages_df['female_share'], label='Non-Fiction Female Share (5-year average)', marker='o',color='blue', linestyle='-', linewidth=2.5)
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Author Share (%)', fontsize=14, fontweight='bold')
plt.title('5-Year Average Female Author Non-Fiction Share on NYT Best Seller List', fontsize=16, fontweight='bold')
plt.legend()
plt.grid(True)

# Set the y-axis limits to 0 - 50
plt.ylim(0, 50)

# Increase the font size of x and y ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()



import matplotlib.pyplot as plt

# Plot 5-year rolling averages for non-fiction books with a thicker blue line
plt.figure(figsize=(12, 6))
plt.plot(non_fiction_averages_df.index, non_fiction_averages_df['female_share'], label='Non-Fiction Female Share (5-year average)', marker='o', color='blue', linestyle='-', linewidth=2.5)
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Author Share (%)', fontsize=14, fontweight='bold')
plt.title('5-Year Average Female Author Non-Fiction Share on NYT Best Seller List', fontsize=16, fontweight='bold')
plt.legend()
plt.grid(True)

# Set the y-axis limits to 0 - 50
plt.ylim(0, 50)

# Increase the font size of x and y ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save the plot as a high-resolution PNG image
plt.savefig('nyt_author_share_non_fiction.png', dpi=300, bbox_inches='tight')

# Save the plot as a PDF
plt.savefig('nyt_author_share_non_fiction.pdf', format='pdf', bbox_inches='tight')

plt.show()



import matplotlib.pyplot as plt

# Plot 5-year rolling averages for non-fiction books with a thicker blue line
plt.figure(figsize=(12, 6))
plt.plot(author_count_averages_df.index, author_count_averages_df['female_share'], label='Female Share', marker='o', color='blue', linestyle='-', linewidth=2.5)

#plt.plot(fiction_averages_df.index, fiction_averages_df['female_share'], label='Fiction Female Share (5-year average)', marker='o', color='blue', linestyle='-', linewidth=2.5)
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Author Share (%)', fontsize=14, fontweight='bold')
plt.title('5-Year Average Female Author Share on NYT Best Seller List', fontsize=16, fontweight='bold')
plt.legend()
plt.grid(True)

# Set the y-axis limits to 0 - 50
plt.ylim(0, 50)

# Increase the font size of x and y ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save the plot as a high-resolution PNG image
#plt.savefig('nyt_author_share.png', dpi=300, bbox_inches='tight')

# Save the plot as a PDF
#plt.savefig('nyt_author_share.pdf', format='pdf', bbox_inches='tight')

plt.show()




import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already loaded and processed your data as shown in your code.

# Create 5-year intervals
merged_df['year_interval'] = pd.cut(merged_df['year'], bins=range(1930, 2020, 5), right=False)

# Group by 'year_interval' and 'gender' to count the number of male and female authors for each 5-year interval
author_counts_interval = merged_df.groupby(['year_interval', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) for each 5-year interval
author_counts_interval['total'] = author_counts_interval['female'] + author_counts_interval['male']

# Calculate the male and female share as a percentage of the total authors for each 5-year interval
author_counts_interval['male_share'] = (author_counts_interval['male'] / author_counts_interval['total']) * 100
author_counts_interval['female_share'] = (author_counts_interval['female'] / author_counts_interval['total']) * 100

# Reset the index to make 'year_interval' a regular column and convert it to string
#author_counts_interval['year_interval'] = author_counts_interval['year_interval'].astype(str)
author_counts_interval['year_interval'] = author_counts_interval.index.astype(str)

# Plot the average female author share for each 5-year interval
plt.figure(figsize=(12, 6))
plt.plot(author_counts_interval['year_interval'], author_counts_interval['female_share'], label='Female Share (5-year interval average)', marker='o')
plt.xlabel('5-Year Interval')
plt.ylabel('Author Share (%)')
plt.title('5-Year Interval Average Female Author Share on NYT Best Seller List')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()

# Set the y-axis limits to 0 - 50
plt.ylim(0, 50)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming you have already loaded and processed your data as shown in your code.

# Create equally spaced 5-year intervals from 1950 to 2015
year_intervals = np.linspace(1950, 2015, num=14, dtype=int)
#year_intervals = year_intervals[:-1]

# Create 5-year intervals
merged_df['year_interval'] = pd.cut(merged_df['year'], bins=year_intervals, right=False)

# Group by 'year_interval' and 'gender' to count the number of male and female authors for each 5-year interval
author_counts_interval = merged_df.groupby(['year_interval', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) for each 5-year interval
author_counts_interval['total'] = author_counts_interval['female'] + author_counts_interval['male']

# Calculate the male and female share as a percentage of the total authors for each 5-year interval
author_counts_interval['male_share'] = (author_counts_interval['male'] / author_counts_interval['total']) * 100
author_counts_interval['female_share'] = (author_counts_interval['female'] / author_counts_interval['total']) * 100

# Reset the index to make 'year_interval' a regular column and convert it to string
#author_counts_interval['year_interval'] = author_counts_interval.index.astype(str)
year_intervals = year_intervals[:-1]

# Plot the average female author share for each 5-year interval
plt.figure(figsize=(12, 6))
plt.plot(year_intervals, author_counts_interval['female_share'], label='Female Share (5-year interval average)', marker='o')
plt.xlabel('5-Year Interval')
plt.ylabel('Author Share (%)')
plt.title('5-Year Interval Average Female Author Share on NYT Best Seller List')
#plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.xticks(year_intervals)  # Set the x-axis ticks to the defined year intervals
plt.legend()

# Set the y-axis limits to 0 - 50
plt.ylim(12.5 , 47.5)

plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming you have already loaded and processed your data as shown in your code.

# Create equally spaced 5-year intervals from 1950 to 2015
year_intervals = np.linspace(1950, 2015, num=14, dtype=int)

# Create 5-year intervals
merged_df['year_interval'] = pd.cut(merged_df['year'], bins=year_intervals, right=False)

# Group by 'year_interval' and 'gender' to count the number of male and female authors for each 5-year interval
author_counts_interval = merged_df.groupby(['year_interval', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) for each 5-year interval
author_counts_interval['total'] = author_counts_interval['female'] + author_counts_interval['male']

# Calculate the male and female share as a percentage of the total authors for each 5-year interval
author_counts_interval['male_share'] = (author_counts_interval['male'] / author_counts_interval['total']) * 100
author_counts_interval['female_share'] = (author_counts_interval['female'] / author_counts_interval['total']) * 100

# Reset the index to make 'year_interval' a regular column and convert it to string
year_intervals = year_intervals[:-1]

# Filter for fiction books
fiction_df = merged_df[merged_df['fiction'] == 1]

# Group by 'year' and 'gender' to count the number of male and female authors each year for fiction books
fiction_author_counts = fiction_df.groupby(['year_interval', 'gender']).size().unstack(fill_value=0)

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
non_fiction_author_counts = non_fiction_df.groupby(['year_interval', 'gender']).size().unstack(fill_value=0)

# Calculate the total number of authors (male + female) each year for non-fiction books
non_fiction_author_counts['total'] = non_fiction_author_counts['female'] + non_fiction_author_counts['male']

# Calculate the male and female share as a percentage of the total authors for non-fiction books
non_fiction_author_counts['male_share'] = (non_fiction_author_counts['male'] / non_fiction_author_counts['total']) * 100
non_fiction_author_counts['female_share'] = (non_fiction_author_counts['female'] / non_fiction_author_counts['total']) * 100


# Plot the average female author share for each 5-year interval
plt.figure(figsize=(12, 6))
plt.plot(year_intervals, author_counts_interval['female_share'], label='Female Share (5-year interval average)', marker='o',color='blue', linestyle='-', linewidth=2.5)
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Author Share (%)', fontsize=14, fontweight='bold')
plt.title('Female Author Share on NYT Best Seller List', fontsize=16, fontweight='bold')
#plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.xticks(year_intervals)  # Set the x-axis ticks to the defined year intervals
plt.legend()
plt.grid(True)
# Increase the font size of x and y ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Set the y-axis limits to 0 - 50
plt.ylim(12.5 , 47.5)

# Save the plot as a high-resolution PNG image
plt.savefig('nyt_author_share_v2.png', dpi=300, bbox_inches='tight')

# Save the plot as a PDF
plt.savefig('nyt_author_share_v2.pdf', format='pdf', bbox_inches='tight')

plt.show()


# Plot the average female author share for fiction books
plt.figure(figsize=(12, 6))
plt.plot(year_intervals, fiction_author_counts['female_share'], label='Fiction Female Share (5-year interval average)', marker='o',color='blue', linestyle='-', linewidth=2.5)
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Author Share (%)', fontsize=14, fontweight='bold')
plt.title('Female Author Share on NYT Best Seller List (Fiction)', fontsize=16, fontweight='bold')
plt.xticks(year_intervals)
plt.legend()
# Increase the font size of x and y ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(12.5, 47.5)  # Set the y-axis limits for fiction books
plt.grid(True)
# Save the plot as a high-resolution PNG image
plt.savefig('nyt_author_share_fiction_v2.png', dpi=300, bbox_inches='tight')

# Save the plot as a PDF
plt.savefig('nyt_author_share_fiction_v2.pdf', format='pdf', bbox_inches='tight')

# Show the first graph
plt.show()

# Plot the average female author share for non-fiction books
plt.figure(figsize=(12, 6))
plt.plot(year_intervals, non_fiction_author_counts['female_share'], label='Non-Fiction Female Share (5-year interval average)', marker='o',color='blue', linestyle='-', linewidth=2.5)
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Author Share (%)', fontsize=14, fontweight='bold')
plt.title('Female Author Share on NYT Best Seller List (Non-Fiction)', fontsize=16, fontweight='bold')
plt.xticks(year_intervals)
plt.legend()
plt.ylim(12.5, 47.5)  # Set the y-axis limits for non-fiction books
plt.grid(True)
# Increase the font size of x and y ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Show the second graph

# Save the plot as a high-resolution PNG image
plt.savefig('nyt_author_share_non_fiction_v2.png', dpi=300, bbox_inches='tight')

# Save the plot as a PDF
plt.savefig('nyt_author_share_non_fiction_v2.pdf', format='pdf', bbox_inches='tight')
plt.show()




