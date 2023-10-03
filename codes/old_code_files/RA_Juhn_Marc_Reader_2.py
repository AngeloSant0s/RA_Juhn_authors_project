
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:50:33 2021

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
import random
from selenium import webdriver
from pandas.io.json import json_normalize


start_time = datetime.datetime.now()

######################################################################################################
############################################ PYMARC MARC FILES INFO ##################################

# WE NEED TO FIND A WAY TO GET THE MARC FILES

from pymarc import MARCReader

results_rows = []
#with open('C:/Users/jcholbro/Desktop/MARC/total_books_authors_project_mrc.mrc', 'rb') as fh:
with open('C:/Users/jcholbro/Desktop/MARC/ISBN_search_results.mrc', 'rb') as fh:

    reader = MARCReader(fh)
    for record in reader:
        df={}
        #print(record.title())
        sheadings = record.get_fields('650')
        sheadings_len = len(sheadings)
        gheadings = record.get_fields('655')
        gheadings_len = len(gheadings)      
        for i in range(4):
            try:
                h = sheadings[i].value()
                df['subhead_'+str(i+1)] = h
            except:
                df['subhead_'+str(i+1)] = np.nan
        for i in range(4):
            try:
                h = gheadings[i].value()
                df['genre_'+str(i+1)] = h
            except:
                df['genre_'+str(i+1)] = np.nan
        df['title'] =record.title()
        try:
            df['author'] = record['100'].value()
        except:
            df['author'] = np.nan
        try:
            df['pub_info'] = record['260'].value()
        except:
            df['pub_info'] = np.nan
        try:
            df['isbn'] = record['020'].value()
        except:
            df['isbn'] = np.nan
        #df['issr'] = record['022'].value()
        try:
            df['pages'] = record['300'].value()
        except:
            df['pages'] = np.nan  
        try:
            df['DDC'] = record['082'].value()
        except:
            df['DDC'] = np.nan  
        try:
            df['LCC'] = record['050'].value()
        except:
            df['LCC'] = np.nan 
        try:
            df['LCCN'] = record['010'].value()
        except:
            df['LCC'] = np.nan
        try:
            df['Country'] = record['257'].value()
        except:
            df['Country'] = np.nan
        results_rows.append(df)
        #break
 

df1 = pd.DataFrame(results_rows)
df1 = df1.drop_duplicates(subset = ['title']).reset_index().drop('index', axis = 1)
df1=df1.fillna('$$')
#df1 = df1.tail(25) ## Creating a smaller dataframe to inspect, that doesn't take so long to load




##################################################################################
# This cleans isbn

for i in range(df1.shape[0]):
    try:
        x = isbnlib.get_canonical_isbn(df1['isbn'][i])
        df1.isbn[i] = x
        x
    except:
        pass

###################################
# This cleans page numbers

for i in range(df1.shape[0]):
    try:
        i
        string = df1['pages'][i]                  
        string
        string_pattern = re.compile(r'[0-9]+\s+(?:pages)', flags = re.M)
        pg = string_pattern.findall(string)
        string_pattern1 = re.compile(r'[0-9]+', flags = re.M)
        pg = string_pattern1.findall(pg[0])[0]
        df1['pages'][i] = int(pg)
    except:
        pass

#######################################
# This Cleans genre category 
for n in range(4):    
    for i in range(df1.shape[0]):
        try:
            i
            string = df1['genre_'+str(n+1)][i]                  
            string
            string_pattern = re.compile(r'.+(?=\.)', flags = re.M)
            genre = string_pattern.findall(string)
            genre
            df1['genre_'+str(n+1)][i] = genre[0]
        except:
            pass

#######################################
# This Cleans subhead category 
for n in range(4):    
    for i in range(df1.shape[0]):
        try:
            i
            string = df1['subhead_'+str(n+1)][i]                  
            string
            string_pattern = re.compile(r'.+(?=\.)', flags = re.M)
            genre = string_pattern.findall(string)
            genre
            df1['subhead_'+str(n+1)][i] = genre[0]
        except:
            pass

#######################################
# This Cleans title category 

for i in range(df1.shape[0]):
    df1['title'][i]= str(df1['title'][i])
    df1['title'][i] = df1['title'][i].replace('/', ' ').strip() 

#######################################

broad_genre_cat_fiction = {'Action/Adventure':['spy','spy stories','adventure','superhero', 'adventure fiction'],
                           'Childrens Stories':["children's stories","children's books",'children'],
                           'Fantasty':['wizard','magic','elves','fantasy fiction','fantasy'],
                           #'Fiction General':['fiction general'],
                           'Horror/Pyschological':['horror','pyschological','horror fiction'],
                           'Mystery/Detective':['mystery','detective','mystery fiction','murder mystery'],
                           'Romance':['love','romance fiction','romance','romantic stories'],
                           'Science Fiction':['star wars','space','technology','science fiction','scifi'],
                           'Thrillers/Crime':['thriller','suspense','crime','suspense fiction'],
                           'Travel':['travel','world','jounrey','global'],
                           'Historical Fiction':['historical fiction','history','historical stories']}



broad_genre_cat_non_fic = {'Biography':['biography','autobiography','biographies','autobiographies'],
                           'Memoir':['memoir'],
                           'Narrative':['narrative'],
                           'Self-help':['self-help','self help','self improvement'],
                           'Science':['science','statistics'],
                           'Textbook':['textbook'],
                           'Philosophy':['philosophy'],
                           'History':['history'],
                           'Health\Fitness':['health','fitness','exercise','diet','wellness','recreation'],
                           'Business/Economics':['business','economics','economy','money','banking','finance','management'],
                           'Hobbies':['arts','crafts','drawing','photography'],
                           'Sports':['sports','sports stories','sports reports'],
                           'True Crime':['murder','crime','criminal'],
                           'Politics':['politics','speeches','president','political','political party','political science']}


genre_words_fic= ["(spy|spy stories|adventure|superhero|adventure fiction)",
                           "(childrens stories|childrens books|children)",
                           "(wizard|magic|elves|fantasy fiction|fantasy)",
                           #"(fiction general)",
                           "(horror|psychological|horror fiction|murder|serial murder|murder mystery)",
                           "(mystery|detective|mystery fiction|detective|detectives)",
                           "(love|romance fiction|romance|romantic stories)",
                           "(star wars|space|technology|science fiction|scifi)",
                           "(thriller|suspense|crime|suspense fiction|thriller fiction|crimes|crime fiction)",
                           "(travel|world|jounrey|global)",
                           "(historical fiction|history|historical stories)"]

genre_words_nf = ["(biography|autobiography|biographies|autobiographies)",
                           "(memoir)",
                           "(narrative)",
                           "(self-help|self help|self improvement)",
                           "(science|statistics)",
                           "(textbook)",
                           "(philosophy)",
                           "(history)",
                           "(health|fitness|exercise|diet|wellness|recreation)",
                           "(business|economics|economy|money|banking|finance|management)",
                           "(arts|crafts|drawing|photography)",
                           "(sports|sports stories|sports reports)",
                           "(murder|crime|criminal)",
                           "(politics|speeches|president|political|political party|political science)"]


df1['genre_1'] = df1['genre_1'].str.lower()
df1['genre_2'] = df1['genre_2'].str.lower()
df1['genre_3'] = df1['genre_3'].str.lower()
df1['genre_4'] = df1['genre_4'].str.lower()

df1['subhead_1'] = df1['subhead_1'].str.lower()
df1['subhead_2'] = df1['subhead_2'].str.lower()
df1['subhead_3'] = df1['subhead_3'].str.lower()
df1['subhead_4'] = df1['subhead_4'].str.lower()

df1.iloc[:,0:8]=df1.iloc[:,0:8].fillna('$$')
###############################################

genre_labels_fic = list(broad_genre_cat_fiction.keys())
genre_labels_nf = list(broad_genre_cat_non_fic.keys())    
    
    

    
for g in range(len(genre_labels_fic)):
        df1[genre_labels_fic[g]]=np.nan
for i in range(df1.shape[0]):
    a = [ df1.iat[i,0] + ' ' + df1.iat[i,1] + ' ' + df1.iat[i,2]
             + ' ' + df1.iat[i,3] + ' ' + df1.iat[i,4]+ ' ' + df1.iat[i,5]
             + ' ' + df1.iat[i,6]+ ' ' + df1.iat[i,7]]
    
    for g in range(len(genre_labels_fic)):
        #print(genre_labels_fic[g])
        #df1[genre_labels_fic[g]][i] = 0
        string_pattern = re.compile(r'(?:[\s]|^)'+genre_words_fic[g]+'(?=[\s]|$)', flags = re.M)
        #print('(?:[\s]|^)'+genre_words_fic[g]+'(?=[\s]|$)')
        genre = string_pattern.findall(a[0])
        
        if len(genre)>0:
            #print(genre)
            print('match')
            df1.at[i, genre_labels_fic[g]]=1
            
        else:
            print('no match')
            df1.at[i, genre_labels_fic[g]]=0
            
for g in range(len(genre_labels_nf)):
        df1[genre_labels_nf[g]]=np.nan
for i in range(df1.shape[0]):
    a = [ df1.iat[i,0] + ' ' + df1.iat[i,1] + ' ' + df1.iat[i,2]
             + ' ' + df1.iat[i,3] + ' ' + df1.iat[i,4]+ ' ' + df1.iat[i,5]
             + ' ' + df1.iat[i,6]+ ' ' + df1.iat[i,7]]
    
    for g in range(len(genre_labels_nf)):
        #print(genre_labels_fic[g])
        #df1[genre_labels_fic[g]][i] = 0
        string_pattern = re.compile(r'(?:[\s]|^)'+genre_words_nf[g]+'(?=[\s]|$)', flags = re.M)
        #print('(?:[\s]|^)'+genre_words_fic[g]+'(?=[\s]|$)')
        genre = string_pattern.findall(a[0])
        
        if len(genre)>0:
            #print(genre)
            print('match')
            df1.at[i, genre_labels_nf[g]]=1
            
        else:
            print('no match')
            df1.at[i, genre_labels_nf[g]]=0
            
            
            
df1.iloc[:,17:].mean()*100
df1.iloc[:,17:].sum()
summary = df1.iloc[:,17:].sum()
summary.sum()

df1.to_excel(r'RA_Juhn_Marc_reader_test.xlsx', index=False)

end_time = datetime.datetime.now()
print(end_time - start_time) 


