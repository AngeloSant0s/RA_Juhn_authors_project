'''

Author: Angelo Santos

This code aims to plot the life cycle graphs

'''
import os 
import pandas as pd
import seaborn as sns
import p_func_life_cycle as plc
from matplotlib import pyplot as plt
'''

# Plotting the life cycle graphs
## Uploanding the NY best sellers life cycle dataset

'''
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/bs/authors/lifecycles')
lfcy = pd.read_pickle('cre_life_cycle_bs.pkl')
'''

We want to plot the probability of publishing a book for female and male in their respective
cohorts. We will plot this using 15 years cohorts starting in 1900. To do it, we will create
a dummy variable for each cohort.

'''
years = lfcy.groupby('ID').first().reset_index()
years = years[['ID','year']].rename(columns = {'year':'birth_year'})
lfcy = lfcy.merge(years, on='ID', how = 'left')

size = 15
lfcy = plc.lc_cohort(lfcy, size = size)

os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/bs/authors/lifecycles')
lfcy.to_pickle('cre_life_cycle_bs_'+str(size)+'y.pkl')

