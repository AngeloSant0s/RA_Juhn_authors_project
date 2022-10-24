'''

Packages

'''
import os

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import p_func_female_shares_loc as pf

'''

Plotting  female shares for actual, fiction and non fiction

'''

start = 1930
end = 2010

fm = []
for i in ['Actual','Fiction','non Fiction']:
    fs = pf.female_share(start=start, end = end, g=i)
    fm.append(fs)
fm = pd.concat(fm, axis = 0).reset_index().drop('index', axis = 1)
fm['fs'] = fm['fs']*100
fm = fm.rename(columns = {
    'year': 'Year',
    'fs': 'Female Share',
    'genre' : 'Category'
})

sns.lineplot(data = fm, x = fm.columns[0], y = fm.columns[1], hue = fm.columns[2], palette = 'icefire')\
    .set(title = 'Female share between '+str(start)+ ' and ' + str(end))
sns.despine(left=False, bottom=False)
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/shares/loc/female_share')
plt.savefig('p_female_shares.png')
plt.close()
'''

Plotting female shares and genre shares (two scales) - One plot

'''
fics = [
        'Action/Adventure', 
        'Childrens Stories', 
        'Fantasty/Sci-Fi', 
        'Horror/Paranormal', 
        'Mystery/Crime',
        'Romance', 'Suspence', 
        'Spy/Politics', 
        'Literary_1'
        ]
i1 = 0 
i2 = 0
fig, axs = plt.subplots(3, 3, constrained_layout=True)

for f in fics:
    df1 = pf.subg_female_share(g = f)
    df2 = pf.subgenre_share(g = f)
    #define colors to use
    col1 = 'g'
    col2 = 'b'

    #define subplots
    #add first line to plot
    axs[i1][i2].plot(df1.year, df1.fs, color=col1)

    #add x-axis label
    if (i2 == 1) & (i1 == 2):
        axs[i1][i2].set_xlabel('Year', fontsize=10)

    #add y-axis label
    if (i2 == 0) & (i1 == 1):
        axs[i1][i2].set_ylabel('Female Share', color=col1, fontsize=10)

    #define second y-axis that shares x-axis with current plot
    ax2 = axs[i1][i2].twinx()

    #add second line to plot
    ax2.plot(df2.year, df2.fs, color=col2)

    #add second y-axis label
    if (i2 == 2) & (i1 == 1):
        ax2.set_ylabel('Genre Share', color=col2, fontsize=10)
    axs[i1][i2].set_title(f, fontsize=10)
    i2 = i2 + 1
    if i2 == 3:
        i2 = 0
    else: 
        pass
    if i2 == 0:
        i1 += 1
    else:
        pass
        
plt.suptitle('Two scales graphs')
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/shares/loc/two_scale')
plt.savefig('p_2sca.png')
plt.close()

'''

Plotting female shares and genre shares (two scales) - Separated

'''
fics = [
        'Action/Adventure', 
        'Childrens Stories', 
        'Fantasty/Sci-Fi', 
        'Horror/Paranormal', 
        'Mystery/Crime',
        'Romance', 'Suspence', 
        'Spy/Politics', 
        'Literary_1'
        ]

for f in fics:
    df1 = pf.subg_female_share(g = f)
    df2 = pf.subgenre_share(g = f)

    fig, axs = plt.subplots()
    #define colors to use
    col1 = 'g'
    col2 = 'b'

    #define subplots
    #add first line to plot
    axs.plot(df1.year, df1.fs, color=col1)

    #add x-axis label
    axs.set_xlabel('Year', fontsize=10)

    #add y-axis label
    axs.set_ylabel('Female Share', color=col1, fontsize=10)

    #define second y-axis that shares x-axis with current plot
    ax2 = axs.twinx()

    #add second line to plot
    ax2.plot(df2.year, df2.fs, color=col2)

    #add second y-axis label
    ax2.set_ylabel('Genre Share', color=col2, fontsize=10)
    axs.set_title(f, fontsize=10)
    os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/shares/loc/two_scale')
    plt.savefig('p_2sca_'+f.replace('/','_').replace(' ','_')+'.png')
    plt.close()

