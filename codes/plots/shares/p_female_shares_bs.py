import os 
import pandas as pd 
import seaborn as sns
import matplotlib as plt
from matplotlib import pyplot as plt
import p_func_female_shares_loc as pf

os.chdir("/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/data/data_created/full_datasets/bs")
books = pd.read_excel('cre_bs_v2.xlsx')

start = 1931
end = 2012

fm = []
for i in ['Actual','Fiction','non Fiction']:
    fs = pf.female_share(start=start, end = end, g=i, bs=1)
    fm.append(fs)
fm = pd.concat(fm, axis = 0).reset_index().drop('index', axis = 1)
fm['fs'] = fm['fs']*100
fm = fm.rename(columns = {
    'year': 'Year',
    'fs': 'Female Share',
    'genre' : 'Category'
})

fm['groups'] = 0
for i in range((end-start)//5):
    fm.loc[(fm['Year'] >= start + 5*i) & (fm['Year'] < start + 5*(i+1)), 'groups'] = start + 5*i

fm = fm.groupby(['Category','groups']).mean().reset_index()
fm = fm[['Year','Female Share','Category']]

sns.lineplot(data = fm, x = fm.columns[0], y = fm.columns[1], hue = fm.columns[2], palette = 'icefire')\
    .set(title = 'Female share between '+str(start)+ ' and ' + str(end))
sns.despine(left=False, bottom=False)
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/shares/ny_bs/female_share')
plt.savefig('p_female_shares.png')
plt.show()