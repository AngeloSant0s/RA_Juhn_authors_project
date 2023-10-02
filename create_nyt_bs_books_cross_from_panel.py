#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:10:29 2023

@author: jordanholbrook
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
#import cluster_pipeline_functions as cpf
import os
import logging
import seaborn as sns
import matplotlib.pyplot as plt
import sys


books = pd.read_excel(r"/Users/jordanholbrook/Library/CloudStorage/Dropbox/authors_project_data_06.2023/new_york_time_best_sellers_data/best_sellers_book_file.xlsx")  

df = books.head(50)   

import pandas as pd

# Group by 'book_id' and calculate max, min, and total
agg_functions = {
    'weekly_rank': ['max', 'min'],
    'number_of_weeks': 'max'
}

book_stats = books.groupby('book_id').agg(agg_functions).reset_index()
book_stats.columns = ['book_id', 'max_weekly_rank', 'min_weekly_rank', 'total_number_weeks']
books = books.merge(book_stats, on='book_id', how='left')

# Assuming your dataset is named 'books'
grouped_books = books.groupby('book_id')


aggregation_functions = {
    'day': 'first',
    'month': 'first',
    'year': 'first',
    'max_weekly_rank': 'first',
    'min_weekly_rank': 'first',
    'title': 'first',
    'last_rank': 'mean',
    'total_number_weeks': 'mean',
    'fiction': 'first',
    'publisher': 'first',
    'author1': 'first',
    'author2': 'first',
    'author3': 'first',
    'author4': 'first',
    'author5': 'first',
    'duplicate_title_flag': 'first'
}

cross_sectional_books = grouped_books.agg(aggregation_functions)

cross_sectional_books.reset_index(inplace=True)




# Group by 'book_id' and calculate max, min, and total
agg_functions = {
    'weekly_rank': ['max', 'min'],
    'number_of_weeks': 'max',
    'day': ['first', 'last'],
    'month': ['first', 'last'],
    'year': ['first', 'last'],
}

book_stats = books.groupby('book_id').agg(agg_functions).reset_index()
book_stats.columns = ['book_id', 'max_weekly_rank', 'min_weekly_rank', 'total_number_weeks',
                      'first_appearance_day', 'last_appearance_day',
                      'first_appearance_month', 'last_appearance_month',
                      'first_appearance_year', 'last_appearance_year']
books = books.merge(book_stats, on='book_id', how='left')

# Assuming your dataset is named 'books'
grouped_books = books.groupby('book_id')

aggregation_functions = {
    'last_rank': 'mean',
    'fiction': 'first',
    'publisher': 'first',
    'author1': 'first',
    'author2': 'first',
    'author3': 'first',
    'author4': 'first',
    'author5': 'first',
    'duplicate_title_flag': 'first',
}

cross_sectional_books = grouped_books.agg(aggregation_functions)

cross_sectional_books.reset_index(inplace=True)
# Merge the 'book_stats' DataFrame with the 'cross_sectional_books' DataFrame
cross_sectional_books = cross_sectional_books.merge(book_stats, on='book_id', how='left')
cross_sectional_books['ave_rank'] = cross_sectional_books['last_rank'].round()+1
cross_sectional_books.drop(columns=['last_rank'], inplace=True)

cross_sectional_books.to_excel("NYT_BS_books_cross_section.xlsx")

