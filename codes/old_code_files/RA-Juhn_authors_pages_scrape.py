# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:13:49 2020

@author: jcholbro
"""


import requests 
import pandas as pd
import numpy as np
#import BeautifulSoup
import bs4
import re







df_rows = []

links_list = ["https://en.wikipedia.org/wiki/Jean_M._Auel",
              "https://en.wikipedia.org/wiki/James_Clavell",
              "https://en.wikipedia.org/wiki/Nicholas_Evans",
              "https://en.wikipedia.org/wiki/Louis_L%27Amour",
              "https://en.wikipedia.org/wiki/Ken_Follett",
              "https://en.wikipedia.org/wiki/Garrison_Keillor",
              "https://en.wikipedia.org/wiki/Robert_Ludlum",
              "https://en.wikipedia.org/wiki/John_le_Carr%C3%A9",
              "https://en.wikipedia.org/wiki/Judith_Krantz",
              "https://en.wikipedia.org/wiki/Danielle_Steel",
              "https://en.wikipedia.org/wiki/Tom_Clancy",
              "https://en.wikipedia.org/wiki/Stephen_King"
              ]
#links_list = ["https://en.wikipedia.org/wiki/Nicholas_Evans"]

for link in links_list:
    response = requests.get(link)
    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')
    
        title = html.select("#firstHeading")[0].text
        paragraphs = html.select("p")
        #for para in paragraphs:
           #print (para.text)
        #print(title)
        # just grab the text up to contents as stated in question
        intro = '\n'.join([ para.text for para in paragraphs])
        # you can add paragraphs[0:2] to index to a certain number of paragraphs
        #print (intro)
        married_pattern = re.compile(r'([A-Z][^\\.;]*(?:married)[^\\.;]*)', flags = re.M)
        marr_sentence = married_pattern.findall(intro)
        spouse = re.compile(r'([A-Z]\w+\s[A-Z]\w+)', flags = re.M)
        
        if len(marr_sentence) != 0:
           spouse_name = spouse.findall(marr_sentence[0])
        else:
            spouse_name = []
        
        children_pattern = re.compile(r'([A-Z][^\\.;]*(?:children)[^\\.;]*)', flags = re.M)
        children_sentence = children_pattern.findall(intro)
        children = re.compile(r'([A-Z]\w+\s[A-Z]\w+)', flags = re.M)
        # We are going to have some errors here, the regex will find any two word combinations that
        # both capitalized. So it will pick up more than just the name of a kid. 
        if len(children_sentence) != 0:
            children_name = children.findall(children_sentence[0])
        else:
            children_name = []
        num_children = len(children_name)
        has_spouse = 0
        if len(spouse_name) != 0:
            has_spouse = 1
        else:
            has_spouse = 0
        
        # Now I need to store all this data in something so that when I loop through it 
        # it will build a beautiful dataframe.
        df_row = {}
        df_row['author_name'] = title
        df_row['marr_string'] = marr_sentence
        df_row['spouse_name'] = spouse_name
        df_row['children_string'] = children_sentence
        df_row['children_name'] = children_name
        df_row['num_children'] = num_children
        df_row['spouse'] = has_spouse
        
        
        df_rows.append(df_row)
        #i = i+1
    
df = pd.DataFrame(df_rows)


