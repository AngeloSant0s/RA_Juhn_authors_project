#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:10:26 2023

@author: jordanholbrook
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

books = pd.read_csv(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/extended_books_panel.csv")  

authors = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/cre_demo_bs_v1.xlsx")


###############################################################################
###############################################################################


'''
Create Authors Share Figure 
'''

# Merge 'books' and 'authors' DataFrames on 'author_id'
merged_df = books.merge(authors[['author_iddemo', 'gender']], on='author_iddemo', how='left')


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
#fiction_averages_df = calculate_5_year_averages(fiction_author_counts[['male_share', 'female_share']])

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
