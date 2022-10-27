---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Plotting  female shares 
In this section, we will plot the female shares for each year, dividing in three categories:

* **Actual:** Female shares using all books
* **Fiction:** Female shares in the fiction books samples
* **Non-Fiction:** Female shares in the non-fiction books samples

We wil plot the same graph for the [Library of congress](loc) and [New York best sellers](bs)

(loc)=
## Library of Congress
We will plot these shares for the 1930-2010.

```{code-block}
start = 1930
end = 2010
```

Now, we will use the function female_share using `start` and `end` as arguments to get the range we want. In addition to it, we will loop this on the three samples: `'Actual','Fiction','non Fiction'`

```{code-block}
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
```

Now, we can plot the following figure. 

```
sns.lineplot(data = fm, x = fm.columns[0], y = fm.columns[1], hue = fm.columns[2], palette = 'icefire')\
    .set(title = 'Female share between '+str(start)+ ' and ' + str(end))
sns.despine(left=False, bottom=False)
os.chdir('/Users/angelosantos/Library/CloudStorage/OneDrive-SharedLibraries-UniversityOfHouston/Books Project - General/outputs/plots/shares/loc/female_share')
plt.savefig('p_female_shares.png')
plt.close()
})
```
This will produce the following figure
```{figure} ../../../images/female_shares/p_female_shares_loc.png
:name: figure
```
(bs)=
## New York Best sellers
We will plot these shares for the 1931-2012. However, this is very noisy, so I did an average using 5 years windows.

```{code-block}

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
```

Creating 5 years groups and taking the mean to plot.

```{code-block}
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
```

This will produce the following figure

```{figure} ../../../images/female_shares/p_female_shares_bs.png
\```
