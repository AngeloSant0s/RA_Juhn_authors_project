# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:18:33 2022

@author: jcholbro
"""

import os
import pandas as pd 
import isbnlib 
import numpy as np
import time
import requests
from bs4 import BeautifulSoup
import datetime
import re
import matplotlib.pyplot as plt
import seaborn as sb



os.chdir(r'C:\Users\jcholbro\University Of Houston\Books Project - General\MARC\RE')
start_time = datetime.datetime.now()


male_counts = []
female_counts= []
for i in range(1,3):
     print(i)
     fr = pd.read_pickle('USA_LCC_'+str(i)+'.pkl')
     unique = fr.author.nunique()
     print("The number of unique authors for part "+str(i)+" is "+str(unique))
     print("Total obsverations for part "+str(i)+" is "+str(len(fr)))

     part_f = fr.groupby('gender')['author'].value_counts()['female']
     part_m = fr.groupby('gender')['author'].value_counts()['male']
      
     male_counts.append(part_m)   
     female_counts.append(part_f)  
        

df_m = pd.concat([male_counts[0], male_counts[1]], axis=1)
df_m.columns = ['books_1','books_2']
df_m.reset_index(inplace=True)
df_m=df_m.fillna(0)
df_m['total_books'] = df_m['books_1']+df_m['books_2']
df_m['total_books'].describe()

df_f = pd.concat([female_counts[0], female_counts[1]], axis=1)
df_f.columns = ['books_1','books_2']
df_f.reset_index(inplace=True)
df_f=df_f.fillna(0)
df_f['total_books'] = df_f['books_1']+df_f['books_2']
df_f['total_books'].describe()


data_m=np.array(df_m['total_books'])     
data_f=np.array(df_f['total_books'])       
       
     
sb.set_style("whitegrid")  # Setting style(Optional)
plt.figure(figsize = (10,5)) #Specify the size of figure we want(Optional)
#sb.distplot(x = data_m  ,  bins = 10 , kde = True , color = 'blue'\
       #      , kde_kws=dict(linewidth = 4 , color = 'blue'), label='Male')
sb.distplot(x = data_f  ,  bins = 5 , kde = True , color = 'red'\
            , kde_kws=dict(linewidth = 4 , color = 'red'),label='Female')
#sb.distplot(x = data  ,  bins = 10 , kde = True , color = 'teal'\
 #            , kde_kws=dict(linewidth = 4 , color = 'black'))
plt.title('LOC Author Publication Age Distribution', fontsize=18)
plt.xlabel('Publication Age', fontsize=16)
plt.ylabel('Density', fontsize=16)
#plt.legend(framealpha=1, frameon=True);
plt.show()  


df_m.to_csv(r'C:\Users\jcholbro\University Of Houston\Books Project - General\Data\male_author_frequency_loc.csv', index = False)
df_f.to_csv(r'C:\Users\jcholbro\University Of Houston\Books Project - General\Data\female_author_frequency_loc.csv', index = False)

# =============================================================================
# 
# df_f['total_books'].describe()
# Out[90]: 
# count    264159.000000
# mean          2.294039
# std           5.520208
# min           1.000000
# 25%           1.000000
# 50%           1.000000
# 75%           2.000000
# max         666.000000
# Name: total_books, dtype: float64
# 
# =============================================================================
# =============================================================================
# df_m['total_books'].describe()
# Out[84]: 
# count    685863.000000
# mean          2.417474
# std           5.575217
# min           1.000000
# 25%           1.000000
# 50%           1.000000
# 75%           2.000000
# max        1692.000000
# Name: total_books, dtype: float64
# 
# 
# =============================================================================

# =============================================================================
#                                         author  books_1  books_2  total_books
# 0             Shakespeare, William, 1564-1616.   1145.0    547.0       1692.0
# 1                            White, Anthony G.    408.0     10.0        418.0
# 2                 Dickens, Charles, 1812-1870.    352.0    168.0        520.0
# 3                      Twain, Mark, 1835-1910.    341.0    224.0        565.0
# 4                    Asimov, Isaac, 1920-1992.    291.0    104.0        395.0
# 5          Stevenson, Robert Louis, 1850-1894.    285.0    107.0        392.0
# 6                     James, Henry, 1843-1916.    262.0    107.0        369.0
# 7                         Pompey, Sherman Lee.    254.0      0.0        254.0
# 8                  Turner, David Reuben, 1915-    248.0      0.0        248.0
# 9                              Casper, Dale E.    244.0      0.0        244.0
# 10            Hawthorne, Nathaniel, 1804-1864.    214.0     90.0        304.0
# 11              Franklin, Benjamin, 1706-1790.    210.0     62.0        272.0
# 12           Gardner, Erle Stanley, 1889-1970.    210.0     23.0        233.0
# 13                    Ruskin, John, 1819-1900.    209.0     22.0        231.0
# 14  Harmon, Robert B. (Robert Bartlett), 1932-    201.0      9.0        210.0
# 15               Trollope, Anthony, 1815-1882.    200.0     65.0        265.0
# 16     Goethe, Johann Wolfgang von, 1749-1832.    196.0     43.0        239.0
# 17                      Brand, Max, 1892-1944.    194.0    137.0        331.0
# 18            Emerson, Ralph Waldo, 1803-1882.    194.0     46.0        240.0
# 19          Cooper, James Fenimore, 1789-1851.    191.0     39.0        230.0
# 20                   Scott, Walter, 1771-1832.    191.0     66.0        257.0
# 21            Thoreau, Henry David, 1817-1862.    190.0     63.0        253.0
# 22                Poe, Edgar Allan, 1809-1849.    189.0     70.0        259.0
# 23                    Milton, John, 1608-1674.    186.0     39.0        225.0
# 24                     Sullivan, George, 1927-    183.0     33.0        216.0
# 
# =============================================================================

# =============================================================================
#                                               author  ...  total_books
# 0                                     Vance, Mary A.  ...        666.0
# 1                                Moncure, Jane Belk.  ...        270.0
# 2                       Christie, Agatha, 1890-1976.  ...        287.0
# 3                                  Ziefert, Harriet.  ...        413.0
# 4                 Hill, Grace Livingston, 1865-1947.  ...        186.0
# 5                             Grey, Zane, 1872-1939.  ...        237.0
# 6                                    Doumato, Lamia.  ...        150.0
# 7                        Potter, Beatrix, 1866-1943.  ...        193.0
# 8                                Bunting, Eve, 1928-  ...        244.0
# 9                                       Yolen, Jane.  ...        294.0
# 10                    Alcott, Louisa May, 1832-1888.  ...        216.0
# 11                         Seifert, Elizabeth, 1897-  ...        133.0
# 12                                    Cable, Carole.  ...        130.0
# 13                          Bailey, Bernadine, 1901-  ...        124.0
# 14                            Wells, Carolyn, -1942.  ...        125.0
# 15                                   Keene, Carolyn.  ...        459.0
# 16                                   Crocker, Betty.  ...        186.0
# 17                          Austen, Jane, 1775-1817.  ...        216.0
# 18                        Baldwin, Faith, 1893-1978.  ...        125.0
# 19                  Brown, Margaret Wise, 1910-1952.  ...        190.0
# 20                          Lenski, Lois, 1893-1974.  ...        123.0
# 21                                 Rockwell, Anne F.  ...        172.0
# 22                                    Greene, Carol.  ...        155.0
# 23                        Wharton, Edith, 1862-1937.  ...        184.0
# 24  Buck, Pearl S. (Pearl Sydenstricker), 1892-1973.  ...        107.0
# =============================================================================
end_time = datetime.datetime.now()
print(end_time - start_time)

i=1
i=2
fr = pd.read_pickle('USA_LCC_'+str(i)+'.pkl')
fr2 = pd.read_pickle('USA_LCC_'+str(i)+'.pkl')



df2 = fr2[['author','last','first','year','pub_year','gender']]
df2 = df2.drop_duplicates(subset = ["author"])
df2['has_birthdate'] = df2.year.notnull().astype(int)

# =============================================================================
# authors with birthdays in part 1, 283638
# Unique Authors 658583
# total number of authors part 1, 1424092 
# 
# =============================================================================

df = pd.concat([df1, df2], axis=0).reset_index()

# =============================================================================
# authors with birthdays in part 2, 194157
# Unique Authors 552968
# total number of authors part 2, 1087765 
# 
# =============================================================================

frame['missing_genre'] = np.where((frame['fic_score']==1) & (frame['genre_info']==0) , 1, 0)
df['total']=1
df3=df.groupby(['pub_year'])['has_birthdate', 'total'].sum()

df3 = df3.reset_index()
df3 = df3[(df3.pub_year >=1930) & (df3.pub_year <=2014)]
df3 = df3.set_index('pub_year')

df3['%_birthyear'] = df3['has_birthdate'] / df3.total
df3['%_birthyear_missing'] = 1-df3['%_birthyear']
# Graph Missing by Time
x = list(df3['%_birthyear'])
y = list(angelo.index)

plt.figure(figsize=[9, 6])
plt.title('Fiction Genres 1930-2015', y=1.13, fontsize=13, fontweight='bold')
#plt.subplots_adjust(left=0.13, right=0.93, top=1.05, bottom= 0.27, wspace= 0.3, hspace=0.3)

plt.plot(y, x, linewidth=1)
plt.ylabel('% No Genre Information')
plt.xlabel('% Book Publication Year')
plt.show()

# Graph Missing by Gender and Time
x = list(df3['%_birthyear'])
x1 = list(df3['%_birthyear_missing'])

y = list(df3.index)

plt.figure()
plt.title('LOC Authors Demographic Info 1930-2015', y=1.13, fontsize=13, fontweight='bold')
#plt.subplots_adjust(left=0.13, right=0.93, top=1.05, bottom= 0.27, wspace= 0.3, hspace=0.3)
plt.plot(y, x, linewidth=1)
plt.plot(y, x1, linewidth=1)
plt.legend(["Has_Brithyear","Missing_Birthyear"])
plt.xlabel('Book Publication Year')

plt.ylabel('% of Unique Authors')
plt.show()





