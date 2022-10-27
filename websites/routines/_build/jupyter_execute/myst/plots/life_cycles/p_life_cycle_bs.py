#!/usr/bin/env python
# coding: utf-8

# # NY best sellers life cycle graphs 
# ## Uploading the NY best sellers life cycle dataset

# In[1]:


import os 
import pandas as pd
import seaborn as sns
import p_func_life_cycle as plc
from matplotlib import pyplot as plt


# In[2]:


os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/bs/authors/lifecycles')
lfcy = pd.read_pickle('cre_life_cycle_bs.pkl')


# We want to plot the probability of publishing a book for female and male in their respective cohorts. We will plot this using 15 years cohorts starting in 1920. To do it, we will create a dummy variable for each cohort.

# In[3]:


years = lfcy.groupby('ID').first().reset_index()
years = years[['ID','year']].rename(columns = {'year':'birth_year'})
lfcy = lfcy.merge(years, on='ID', how = 'left')

start = 1920
end = 1995
size = 15
lfcy = plc.lc_cohort(lfcy, size = size, st = start, ed = end)


# Now, save the file

# In[4]:


os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/bs/authors/lifecycles')
lfcy.to_pickle('cre_life_cycle_bs_'+str(size)+'y.pkl')


# ## Creting Dummies for the cohorts of birth
# 
# Using the dummies that we created, we will define a simple function that we will produce 
# two lists.
# - coh: Label for the cohort
# - cys: Time window of the cohort
#     
# You can see them in the output

# In[5]:


def cohorts_fun(start,end,size):
    coh = []
    cys = []
    for c in range(start,end,size):
        co = 'Cohort_'+str(c)[2:]+'_'+str(c+size)[2:]
        cy = str(c)+' - '+str(c+size)
        cys.append(cy)
        coh.append(co)
    return coh, cys

coh, cys = cohorts_fun(start,end,size)
print(coh,cys)


# ## Creating the plotting dataset
# We will use this in our plotting code. Now, define the columns for our plots, these are 
# different life cycle plots that we can produce. We will plot the following for both men 
# and women:
#   - Probability of publishing
#   - Probability of publishing fiction
#   - Probability of publishing non fiction
#   - Ratio of publishing
#   - Ratio of fiction
#   - Ratio of non fiction
# 
# The probabilities are defined as:
# 
# ```{warning}
# include math here 
# ```
# 
# The ratio can be obtained by dividing female probability by male probability
# 
# Let's define the columns.
# 
# ```{code-block}
# coh_all = []
# 
# cols = ['published','qt_published','fiction','non_fiction']
# 
# col_g_f = ['Female probability of publishing',
#             'Female probability of publishing more than one',
#             'Female probability of publishing fiction',
#             'Female probability of publishing non fiction']
# 
# col_g_m = ['Male probability of publishing', 
#             'Male probability of publishing more than one',
#             'Male probability of publishing fiction',
#             'Male probability of publishing non fiction']
# 
# col_g_r = ['Ratio publishing',
#             'Ratio quantity',
#             'Ratio Fiction',
#             'Ratio Non Fiction']
# ```
# 
# Now we will use a function that calculate all the probabilities and use them to obtain the ratios 
# for each cohort.
# 
# ```{code-block}
# coh_all = plc.coh_columns(data = lfcy, coh = coh,
#                          cys = cys, cols = cols,
#                          col_g_f = col_g_f,
#                          col_g_m = col_g_m)
# 
# coh_all['Ratio publishing'] = coh_all['Female probability of publishing']/coh_all['Male probability of publishing']
# coh_all['Ratio Fiction'] = coh_all['Female probability of publishing fiction']/coh_all['Male probability of publishing fiction']
# coh_all['Ratio Non Fiction'] = coh_all['Female probability of publishing non fiction']/coh_all['Male probability of publishing non fiction']
# ```
# 
# Now, we will clean a bit the data and average the cohort observations using 5 years windowns (eg.: 20 - 25,...)
# 
# ```{code-block}
# coh_all = coh_all.loc[coh_all['Ratio publishing'].notna()]
# 
# coh_all['Age Group'] = 0
# for ageg in range(20,85,5):
#     print(ageg)
#     coh_all.loc[(coh_all['Age'] >= ageg) & (coh_all['Age'] < ageg + 5), 'Age Group'] = ageg
# 
# age_group = coh_all.groupby(['Age Group','Cohort']).mean().reset_index()
# age_group = age_group.loc[age_group['Ratio publishing'] != 0]
# ```
# ## Plotting the graphs
# ### Female and Male proobabilities of publishing
# Now, we call plot all the graphs
# 
# ```{code-block}
# colors = ['Purples','Blues']
# for c,g in enumerate(['Female', 'Male']):
#     # PROBABILITY OF PUBLISHING
#     sns.lineplot(data=age_group, x="Age", y= g +' probability of publishing', hue = 'Cohort', palette = colors[c] ).set(title = 'Published Books Life Cycle')
#     plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
#     sns.despine(left=False, bottom=False)
#     os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/bs/'+str(size)+'y/'+g.lower()+'/')
#     plt.savefig(g+' prob_pub.png',bbox_inches='tight')
#     plt.show()
# 
#     # PROBABILITY OF PUBLISHING FICTION
#     sns.lineplot(data=age_group, x="Age", y= g +' probability of publishing fiction', hue = 'Cohort', palette = colors[c] ).set(title = 'Published Books Life Cycle - Fiction')
#     plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
#     sns.despine(left=False, bottom=False)
#     os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/bs/'+str(size)+'y/'+g.lower()+'/')
#     plt.savefig(g+' prob_pub_fic.png', bbox_inches='tight')
#     plt.show()
# 
#     # PROBABILITY OF PUBLISHING NON FICTION
#     sns.lineplot(data=age_group, x="Age", y= g +' probability of publishing non fiction', hue = 'Cohort', palette = colors[c] ).set(title = 'Published Books Life Cycle - Non Fiction')
#     plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
#     sns.despine(left=False, bottom=False)
#     os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/bs/'+str(size)+'y/'+g.lower()+'/')
#     plt.savefig(g+' prob_pub_nfic.png',bbox_inches='tight')
#     plt.show()
# ```
# 
# The code above plots the female and male probabilities, here are some examples.
# 
# ```{figure} ../../../images/life_cycle/bs/female/female_prob_pub.png
# ```
# ```{figure} ../../../images/life_cycle/bs/male/male_prob_pub.png
# ```
# ### Ratio
# Now, we can plot the ratios
# 
# ```{code-block}
# sns.lineplot(data=age_group, x="Age", y= 'Ratio publishing', hue = 'Cohort', palette = 'Greys' ).set(title = 'Ratio books Life Cycle')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
# os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/bs/'+str(size)+'y/')
# plt.savefig('ratio_pub.png',bbox_inches='tight')
# plt.show()
# 
# sns.lineplot(data=age_group, x="Age", y= 'Ratio Fiction', hue = 'Cohort', palette = 'Greys' ).set(title = 'Ratio for Fiction - Life Cycle')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
# sns.despine(left=False, bottom=False)
# os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/bs/'+str(size)+'y/')
# plt.savefig('ratio_fic.png',bbox_inches='tight')
# plt.show()
# 
# sns.lineplot(data=age_group, x="Age", y= 'Ratio Non Fiction', hue = 'Cohort', palette = 'Greys' ).set(title = 'Ratio for Non Fiction - Life Cycle')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0., title = 'Cohort')
# sns.despine(left=False, bottom=False)
# os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/bs/'+str(size)+'y/')
# plt.savefig('ratio_nfic.png',bbox_inches='tight')
# plt.show()
# 
# ```
# 
# They will look like this:
# 
# ```{figure} ../../../images/life_cycle/bs/ratio_pub.png
# ```
# 
# ### Female and Male proobabilities of publishing combined
# In conclusion, we can combine female and male probabilities in one graph.
# 
# ```{code-block}
# col_g_f = ['Female probability of publishing',
#             'Female probability of publishing fiction',
#             'Female probability of publishing non fiction']
# 
# col_g_m = ['Male probability of publishing', 
#             'Male probability of publishing fiction',
#             'Male probability of publishing non fiction']
# labels = ['publication','fiction','non_fiction']
# 
# age_group['Cohort_f'] = age_group['Cohort']
# age_group['Cohort_m'] = age_group['Cohort']
# for cs in list(age_group['Cohort'].unique()):
#     print(cs)
#     print(cs[2:4])
#     print(cs[9:11])
#     age_group['Cohort_f'] = age_group['Cohort_f'].replace(cs,'Female ' + cs[2:4] +'-'+ cs[9:11])
#     age_group['Cohort_m'] = age_group['Cohort_m'].replace(cs,'Male ' + cs[2:4] +'-'+ cs[9:11])
# 
# for i in range(3):
#     sns.lineplot(data=age_group, x="Age", y=col_g_f[i], hue = 'Cohort_f', palette = 'Oranges' ).set(title = 'Authors Life Cycle - Probability of '+labels[col_g_f.index(col_g_f[i])])
#     plt.legend(bbox_to_anchor=(1.25, 1), loc=0, borderaxespad=0., title = 'Cohort')
#     sns.lineplot(data=age_group, x="Age", y=col_g_m[i], hue = 'Cohort_m', palette = 'Blues' ).set(title = 'Authors Life Cycle - Probability of '+labels[col_g_f.index(col_g_f[i])].replace('_',' '), \
#                 ylabel = 'Probability of publishing')
#     plt.legend(bbox_to_anchor=(1.25, 1), loc=0, borderaxespad=0., title = 'Cohort')
#     sns.despine(left=False, bottom=False)
#     os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/life_cycles/bs/'+str(size)+'y/')
#     plt.savefig('prob_combined_'+labels[col_g_f.index(col_g_f[i])]+'.png',bbox_inches='tight')
#     plt.show()
# ```
# 
# This will produce the following graphs
# 
# ```{figure} ../../../images/life_cycle/bs/prob_combined_publication.png
# ```
# ```{figure} ../../../images/life_cycle/bs/prob_combined_fiction.png
# ```
# ```{figure} ../../../images/life_cycle/bs/prob_combined_non_fiction.png
# ```
