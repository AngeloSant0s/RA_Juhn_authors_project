'''

Author: Angelo Santos

This code aims to create a life cycle dataset

'''
import os
import time
import pandas as pd
import numpy as np
import cre_func_life_cycle as lc
'''
## Uploanding and cleaning the dataset 

First we need to call the best sellers dataset and get the columns related to the  authors
that we want to use in the life cycle. The columns are:
    - Author id
    - Author name
    - Gender 
    - Birth year
    - Publication year 
    - Fiction

We will also restrict the sample to those born at least in 1900

```{warning}
We will use cre_bs_v2.xlsx, wich is the best sellers with non missing in birth year and
gender.
```
'''
os.chdir("/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/bs")
bs = pd.read_excel('cre_bs_v2.xlsx')
columns = ['author_id','author_name','gender_combined','birth_year','pub_year','fic_score']
bs = bs[columns]
bs = bs.loc[bs.birth_year >= 1900].reset_index().drop('index', axis = 1)
'''

## Creating the dataset 

We want to create a data set wich will be composed by pooling all the authors yearly info. 
We will create the life cycle from 20 to 80 years old.

'''

start = time.process_time() # To count the time of the code

lf = lc.life_cycle(bs,id_column = 'author_id')

print(time.process_time() - start)  # Time of the code

drop_ids = bs.loc[bs['birth_year'] > bs['pub_year']]['author_id'].unique() # We need to adjust these errors
for d in drop_ids:
    lf = lf.loc[lf['ID'] != d]
    
lf.reset_index().drop('index', axis = 1)

'''

Now, we can use this data set to plot the graphs

'''
