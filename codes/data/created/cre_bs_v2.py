
import os
import pandas as pd

os.chdir("/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/bs")
books = pd.read_excel('cre_bs_v1.xlsx')
books = books.rename(columns = {"year" : "pub_year",
                                "fiction" : "fic_score",
                                "gender" : "gender_combined"})
books = books.loc[~books['gender_combined'].isna()]
books = books.loc[(books['gender_combined'] == 'female') | (books['gender_combined'] == 'male')]
books = books.loc[~books['birth_year'].isna()].reset_index().drop('index', axis = 1)
books.to_excel('cre_bs_v2.xlsx')
