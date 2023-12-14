#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 07:48:52 2023

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

books_loc = pd.read_stata(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/library_of_congress_data/authors_dataset_loc_filtered.dta")

books = pd.read_stata(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/library_of_congress_data/books_dataset_filtered.dta")

# Assuming 'books' is your DataFrame
random_sample_books = loc.sample(n=100, random_state=42)  # You can change the random_state value for different random results

loc=books_loc[['ID','author_id','author','first','last','year','birth_year']]

loc=loc[['ID','author_id','author','first','last','year','birth_year']]

bs= bs[['author_iddemo','author_name','birth_year']]

# Assuming 'loc' is your DataFrame
# 'mask' list contains the column names you want to keep
selected_columns = [
    'author_id', 'author', 'first', 'last', 'year', 'birth_year', 'gender',
    'total_books', 'uni_isbns', 'fic_score'
]

# Use the loc[] method to select the desired columns
loc = loc[selected_columns]


import pandas as pd
import numpy as np

'''# Assuming 'loc' is your DataFrame
# Convert 'year' column to numeric (assuming it's a string)
loc['year'] = pd.to_numeric(loc['year'], errors='coerce')

# Create a mask to filter rows based on your criteria
mask = (
    loc['author_id'].notnull() &
    loc['author'].notnull() &
    loc['first'].notnull() &
    loc['last'].notnull() &
    loc['year'].between(1980, 2010) &
    loc['birth_year'].notnull() &
    loc['gender'].notnull() &
    loc['total_books'].notnull() 

)

# Apply the mask to your DataFrame
filtered_df = loc[mask]

# Get random authors from the filtered DataFrame (up to the number of available valid rows)
num_to_sample = min(10000, len(filtered_df))  # Ensure you don't sample more than available rows
random_authors = filtered_df.sample(n=num_to_sample, random_state=42)'''

# Now 'random_authors' contains up to 100 random authors that meet your criteria
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


loc['author_name'] = loc['first']+" "+loc['last']
loc['author_name'] = loc['author_name'].str.replace('[^\w\s]', '', regex=True)


loc['merge_name'] = loc['author_name'].apply(clean_digits_from_name)

loc['merge_name'] = loc['merge_name'].apply(clean_player_name)

random_authors = loc.sample(n=100, random_state=42)

# Assuming 'loc' is your DataFrame
toni_morrison = loc[loc['author_name'] == 'Harper Lee']

# Now, the 'toni_morrison' DataFrame contains all the rows where the author's name is "Toni Morrison."
toni_morrison = loc[loc['author_name'].str.contains('Toni Morrison', case=False, na=False)]

harper_lee = loc[loc['author_name'].str.contains('Harper Lee', case=False, na=False)]

alice_walker= loc[loc['author_name'].str.contains('Alice Walker', case=False, na=False)]

zadie_smith = loc[loc['author_name'].str.contains('Zadie Smith', case=False, na=False)]


jonathan_Franzen= loc[loc['author_name'].str.contains('jonathan franzen', case=False, na=False)]

john_ivring= loc[loc['author_name'].str.contains('john irving', case=False, na=False)]

g_sebald =loc[loc['author_name'].str.contains('g sebald', case=False, na=False)]

tom_wolfe =loc[loc['author_name'].str.contains('tom wolfe', case=False, na=False)]

douglas_adams=loc[loc['author_name'].str.contains('douglas adams', case=False, na=False)]

jk_rowling=loc[loc['author_name'].str.contains('j k rowling', case=False, na=False)]

no_id=loc[loc['author_id'].str.contains('n97108433', case=False, na=False)]

n80051692
n96123043


no_id=loc[loc['author_id'].str.contains('n96123043', case=False, na=False)]



filtered_authors = loc[(loc['birth_year'] >= 1900) & (loc['gender'] != 'None')]

no_id2=loc[loc['author_id']=='n80125518']

n80125518  


filtered_authors = authors_loc[(authors_loc['gender'] != 'None') & (authors_loc['pub_year'] >=  1900)]
filtered_authors = authors_loc[(authors_loc['gender'] != 'None')]


filtered_authors['author_id'].value_counts()
filtered_authors.loc[filtered_authors['author_id']==2]
z = filtered_authors['author_id'].value_counts()
z = pd.DataFrame(z)
z.loc[z['author_id']==2]
no_id2=loc[loc['author_id'].str.contains('n80125518 ', case=False, na=False)]