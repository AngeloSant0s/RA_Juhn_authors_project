'''

Author: Angelo Santos

This code aims to plot the life cycle graphs

'''
import os 

import pandas as pd
import seaborn as sns
import p_func_life_cycle as plc
from matplotlib import pyplot as plt

plt.rcParams['figure.dpi'] = 500
plt.rcParams['savefig.dpi'] = 500
sns.set_style('ticks')
sns.despine(left=False, bottom=True)
sns.set_context("paper")

'''

# Plotting the life cycle graphs
## Uploanding the NY best sellers life cycle dataset

'''
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/loc/authors/lifecycles')
lfcy = pd.read_pickle('life_cycle.pkl')
lfcy = lfcy.dropna().reset_index().drop('index', axis = 1)
years = lfcy.groupby('ID').first().reset_index()
years = years[['ID','year']].rename(columns = {'year':'birth_year'})
lfcy = lfcy.merge(years, on='ID', how = 'left')

start = 1935
end = 1995
size = 15
lfcy = plc.lc_cohort(lfcy, size = size, st = start, ed = end)

'''

Now, save the file 

'''
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/loc/authors/lifecycles')
lfcy.to_pickle('cre_life_cycle_loc_'+str(size)+'y.pkl')

'''

Using the dummies that we created, we will define a simple function that we will produce 
two lists.

    - coh: Label for the cohort
    - cys: Time window of the cohort
    
You can see them in the output

'''

coh, cys = plc.cohorts_fun(start,end,size)
print(coh,cys)
'''

We will use this in our plotting code. Now, define the columns for our plots, these are 
different life cycle plots that we can produce. We will plot the following for both men 
and women:

    - Probability of publishing
    - Probability of publishing fiction
    - Probability of publishing non fiction
    - Ratio of publishing
    - Ratio of fiction
    - Ratio of non fiction

The probabilities are defined as:

The ratio can be obtained by dividing female probability by male probability

Let's define the columns.
'''

cols = ['published','qt_published','fiction','non_fiction']

col_g_f = ['Female probability of publishing',
            'Female probability of publishing more than one',
            'Female probability of publishing fiction',
            'Female probability of publishing non fiction']

col_g_m = ['Male probability of publishing', 
            'Male probability of publishing more than one',
            'Male probability of publishing fiction',
            'Male probability of publishing non fiction']

col_g_r = ['Ratio publishing',
            'Ratio quantity',
            'Ratio Fiction',
            'Ratio Non Fiction']
    
'''

Now we will use a function that calculate all the probabilities and the ratios 
for each cohort.

'''
lfcy['age'] = lfcy['year'] - lfcy['birth_year']

coh_all = plc.coh_columns(data = lfcy, coh = coh,
                         cys = cys, cols = cols,
                         col_g_f = col_g_f,
                         col_g_m = col_g_m)

coh_all['Ratio publishing'] = coh_all['Female probability of publishing']/coh_all['Male probability of publishing']
coh_all['Ratio Fiction'] = coh_all['Female probability of publishing fiction']/coh_all['Male probability of publishing fiction']
coh_all['Ratio Non Fiction'] = coh_all['Female probability of publishing non fiction']/coh_all['Male probability of publishing non fiction']

coh_all = coh_all.loc[coh_all['Ratio publishing'].notna()]

coh_all['Age Group'] = 0
for ageg in range(20,85,5):
    print(ageg)
    coh_all.loc[(coh_all['Age'] >= ageg) & (coh_all['Age'] < ageg + 5), 'Age Group'] = ageg

age_group = coh_all.groupby(['Age Group','Cohort']).mean().reset_index()
age_group = age_group.loc[age_group['Ratio publishing'] != 0]


'''

Now, using coh_all, we call plot all the graphs

'''

colors = ['Purples','Blues']
for c,g in enumerate(['Female', 'Male']):
    # PROBABILITY OF PUBLISHING
    sns.lineplot(data=age_group, x="Age", y= g +' probability of publishing', hue = 'Cohort', palette = colors[c] ).set(title = 'Published Books Life Cycle')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
    sns.despine(left=False, bottom=False)
    os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/loc/'+str(size)+'y/'+g.lower()+'/')
    plt.savefig(g+' prob_pub.png',bbox_inches='tight')
    plt.show()

    # PROBABILITY OF PUBLISHING FICTION
    sns.lineplot(data=age_group, x="Age", y= g +' probability of publishing fiction', hue = 'Cohort', palette = colors[c] ).set(title = 'Published Books Life Cycle - Fiction')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
    sns.despine(left=False, bottom=False)
    os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/loc/'+str(size)+'y/'+g.lower()+'/')
    plt.savefig(g+' prob_pub_fic.png', bbox_inches='tight')
    plt.show()

    # PROBABILITY OF PUBLISHING NON FICTION
    sns.lineplot(data=age_group, x="Age", y= g +' probability of publishing non fiction', hue = 'Cohort', palette = colors[c] ).set(title = 'Published Books Life Cycle - Non Fiction')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
    sns.despine(left=False, bottom=False)
    os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/loc/'+str(size)+'y/'+g.lower()+'/')
    plt.savefig(g+' prob_pub_nfic.png',bbox_inches='tight')
    plt.show()
    
############################################################################### Relative - Ratio

sns.lineplot(data=age_group, x="Age", y= 'Ratio publishing', hue = 'Cohort', palette = 'Greys' ).set(title = 'Ratio books Life Cycle')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/loc/'+str(size)+'y/')
plt.savefig('ratio_pub.png',bbox_inches='tight')
plt.show()

sns.lineplot(data=age_group, x="Age", y= 'Ratio Fiction', hue = 'Cohort', palette = 'Greys' ).set(title = 'Ratio for Fiction - Life Cycle')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
sns.despine(left=False, bottom=False)
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/loc/'+str(size)+'y/')
plt.savefig('ratio_fic.png',bbox_inches='tight')
plt.show()


sns.lineplot(data=age_group, x="Age", y= 'Ratio Non Fiction', hue = 'Cohort', palette = 'Greys' ).set(title = 'Ratio for Non Fiction - Life Cycle')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
sns.despine(left=False, bottom=False)
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/loc/'+str(size)+'y/')
plt.savefig('ratio_nfic.png',bbox_inches='tight')
plt.show()

### COMBINED 
col_g_f = ['Female probability of publishing',
            'Female probability of publishing fiction',
            'Female probability of publishing non fiction']

col_g_m = ['Male probability of publishing', 
            'Male probability of publishing fiction',
            'Male probability of publishing non fiction']
labels = ['publication','fiction','non_fiction']

age_group['Cohort_f'] = age_group['Cohort']
age_group['Cohort_m'] = age_group['Cohort']
for cs in list(age_group['Cohort'].unique()):
    print(cs)
    print(cs[2:4])
    print(cs[9:11])
    age_group['Cohort_f'] = age_group['Cohort_f'].replace(cs,'Female ' + cs[2:4] +'-'+ cs[9:11])
    age_group['Cohort_m'] = age_group['Cohort_m'].replace(cs,'Male ' + cs[2:4] +'-'+ cs[9:11])

for i in range(3):
    sns.lineplot(data=age_group, x="Age", y=col_g_f[i], hue = 'Cohort_f', palette = 'Oranges' ).set(title = 'Authors Life Cycle - Probability of '+labels[col_g_f.index(col_g_f[i])])
    plt.legend(bbox_to_anchor=(1.25, 1), loc=0, borderaxespad=0., title = 'Cohort')
    sns.lineplot(data=age_group, x="Age", y=col_g_m[i], hue = 'Cohort_m', palette = 'Blues' ).set(title = 'Authors Life Cycle - Probability of '+labels[col_g_f.index(col_g_f[i])].replace('_',' '), \
                ylabel = 'Probability of publishing')
    plt.legend(bbox_to_anchor=(1.25, 1), loc=0, borderaxespad=0., title = 'Cohort')
    sns.despine(left=False, bottom=False)
    os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/loc/'+str(size)+'y/')
    plt.savefig('prob_combined_'+labels[col_g_f.index(col_g_f[i])]+'.png',bbox_inches='tight')
    plt.show()
