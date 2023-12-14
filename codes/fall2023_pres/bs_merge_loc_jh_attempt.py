#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:53:40 2023

@author: jordanholbrook
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import logging
import requests
from bs4 import BeautifulSoup
import datetime
import re
import random
import string
import glob

# Define the directory for results relative to the current directory
results_dir = os.path.join(os.getcwd(), "results_log","bs_loc_merge")

# Create the directory for results if it doesn't exist
os.makedirs(results_dir, exist_ok=True)

# Define a custom log format
log_format = "%(message)s"  # Only log the message, excluding timestamp and level

# Configure logging with custom format and file output
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    filename=os.path.join(results_dir, "bs_loc_merge.txt")
)

# Log Project Information
logging.info("Project Information:")
logging.info("Project Name: Authors Project - Best Sellers & Library of Congress Merge")
logging.info("Author: Jordan Holbrook")
logging.info("")  # Add a new line
logging.info("")  # Add another new line


bs = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/OneDrive-UniversityOfHouston/General - Books Project/data/data_created/full_datasets/bs/cre_demo_bs_v1.xlsx")

loc = pd.read_stata(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/library_of_congress_data/authors_dataset_loc_filtered.dta")

loc=loc[['ID','author_id','author','first','last','year','birth_year']]

bs= bs[['author_iddemo','author_name','birth_year']]


'''
import pandas as pd

# Sample data for the best sellers dataframe
best_sellers_data = {
    'author_name': ['Author A', 'Author B', 'Author C', 'Author D', 'Author E'],
    'best_seller_book': ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'],
}
best_sellers = pd.DataFrame(best_sellers_data)

# Sample data for the authors library dataframe
library_data = {
    'author_name': ['Author A', 'Author B', 'Author F', 'Author G', 'Author H'],
    'library_book': ['Library Book 1', 'Library Book 2', 'Library Book 3', 'Library Book 4', 'Library Book 5'],
}
library = pd.DataFrame(library_data)

# Merge the dataframes
merged_data = best_sellers.merge(library, on="author_name", how="left", indicator=True)

# Create a summary of the merge result
merge_summary = merged_data['_merge'].value_counts().reset_index()
merge_summary.columns = ['Result', 'Number of obs']

print(merge_summary)'''

'''
Merge Attempt 1 - Naive Merge
'''
merged_data = loc.merge(bs, left_on="author", right_on="author_name", how='left',indicator=True)
# Create a summary of the merge result
merge_summary = merged_data['_merge'].value_counts().reset_index()
merge_summary.columns = ['Result', 'Number of obs']

logging.info("")  # Add a new line
logging.info("Attempt 1 - Naive merge:\n%s", merge_summary)
logging.info("")  # Add a new line
logging.info("")  # Add a new line

# Function to remove digits and punctuation
def clean_digits_from_name(name):
    if pd.notna(name):  # Check if name is not NaN
        # Remove digits and punctuation using regular expressions
        cleaned_name = re.sub(r'[0-9.,()\-]+', '', name)
        return cleaned_name
    else:
        return name  # Return the NaN value as is

def clean_player_name(name):
    
    name = str(name)
    name = name.upper()
    name = name.replace('[^\w\s]','')
    name = name.translate(str.maketrans("","", string.punctuation))
    name = name.strip()
    name = name.replace(" ","")
   
    return name

loc1 = loc.head(100)


bs['merge_name'] = bs['author_name'].apply(clean_player_name)

loc1['author_name'] = loc1['first']+loc1['last']

loc1['merge_name'] = loc1['author_name'].apply(clean_digits_from_name)

loc1['merge_name1'] = loc1['merge_name'].apply(clean_player_name)

'''
Merge Attempt 2 - Cleaned author names with functions
'''

loc['author_name'] = loc['first']+loc['last']

loc['merge_name'] = loc['author_name'].apply(clean_digits_from_name)

loc['merge_name'] = loc['merge_name'].apply(clean_player_name)


merged_data = loc.merge(bs, on='merge_name', how='outer',indicator=True)

# Create a summary of the merge result
merge_summary = merged_data['_merge'].value_counts().reset_index()
merge_summary.columns = ['Result', 'Number of obs']
print(merge_summary)

matched_names_df = merged_data[merged_data['_merge'] == 'both']




author_name_to_find = "50 Cent (Musician)"
author_50_cent = merged_data[merged_data['author'] == author_name_to_find]

author_name_to_find = "JK Rowling"
author_jk_rowling= loc[loc['author'] == author_name_to_find]


author_name_to_find = "JK Rowling"
author_jk_rowling = loc[loc['author'].str.contains(author_name_to_find)]


if not author_50_cent.empty:
    print("Found author:")
    print(author_50_cent)
else:
    print("Author not found.")


'''
	author
119506	Adams, James Truslow, 1878-1949, comp.
119507	Adams, James Truslow, 1878-1949, ed.
119505	Adams, James Truslow, 1878-1949.
588	Brown, Eleanor, 1926-
589	Brown, Eleanor, 1969-
590	Brown, Eleanor, 1973-
2159	Howard, Linda, 1950-
2160	Howard, Linda.
2661	Le May, Alan, 1899-1964.
2662	Le May, Alan, 1899-1964
2713	Lethem, Jonathan.
2827	Ludlum, Robert, 1927-2001.
2828	Ludlum, Robert, 1927-
'''


from fuzzywuzzy import fuzz
import jaro


author_names = [
    "Adams, James Truslow, 1878-1949, comp.",
    "Adams, James Truslow, 1878-1949, ed.",
    "Adams, James Truslow, 1878-1949.",
    "Adams, James Truslow, 1878-1949",
    "Adams, James Truslow, 1878"
]

query = "Adams, James Truslow"

# Define a threshold for similarity
threshold = 80  # You can adjust this threshold as needed

# Compare the query to each author name
for name in author_names:
    similarity_score = fuzz.ratio(query, name)
    
    if similarity_score >= threshold:
        print(f"'{query}' and '{name}' have a similarity score of {similarity_score}% and are likely the same.")
    else:
        print(f"'{query}' and '{name}' have a similarity score of {similarity_score}% and are different.")




author_name_to_find = "Arlen, Alice"

book_id_to_find = "34178"
found_book = books[books['ID'] == book_id_to_find]

book_id_to_find = "34178"
found_book = books[books['ID'] == book_id_to_find]

author_jk_rowling = df[df['author'].str.contains(author_name_to_find)]

author_name_to_find = "Dillon-Malone, A. (Aubrey)"
author_name_to_find = "Dillon-Malone"
author_jk_rowling = df[df['author'].str.contains(author_name_to_find)]

author_name_to_find = "Dillon-Malone, A. (Aubrey)"
author_to_find = df[df['author'].str.contains(author_name_to_find, case=False)]



# Name to find
author_name_to_find = "John Smith"

# Use .str.contains() to find authors with the name "John Smith"
authors_with_name = loc[loc['author'].str.contains(author_name_to_find, case=False)]

print(authors_with_name)

loc.groupby('author_id')['author'].count().value_counts()


author_name_to_find = "Maria Garcia"
author_name_to_find = "Mohammad Ali"

author_to_find1 = df[df['author'].str.contains(author_name_to_find, case=False)]
author_to_find2 = df[df['author'].str.contains(author_name_to_find, case=False)]




