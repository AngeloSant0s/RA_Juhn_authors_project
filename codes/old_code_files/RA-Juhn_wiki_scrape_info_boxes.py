# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:41:51 2020

@author: jcholbro
"""

import requests 
import pandas as pd
import bs4
import re
import datetime

from pandas.io.html import read_html

start_time = datetime.datetime.now()
# =============================================================================
# 
# Part 1 - Scraping the Main wikipedia NYTBS Fiction List Page to Get the Year Links
# 
# =============================================================================
df_rows = []
website_url = requests.get("https://en.wikipedia.org/wiki/Lists_of_The_New_York_Times_Fiction_Best_Sellers").text
soup =bs4.BeautifulSoup(website_url,"lxml")

Main_page_table = soup.find("table",{"class":"nowraplinks mw-collapsible autocollapse navbox-inner"})
link_years_39_2020  = Main_page_table.findAll("a")


# =============================================================================
# Year_links = []
# link_headers = []
# for link in link_years_39_2020:
#     Year_links.append(link.get('href'))
#     link_headers.append(link.get("title"))
# =============================================================================

Year_links_list = ["https://en.wikipedia.org/wiki/The_New_York_Times_Fiction_Best_Sellers_of_1986",
                   "https://en.wikipedia.org/wiki/The_New_York_Times_Fiction_Best_Sellers_of_1987",
                   "https://en.wikipedia.org/wiki/The_New_York_Times_Fiction_Best_Sellers_of_1988"]

# =============================================================================
## # PART 2 - Scraping the Year Page Tables for the Authors Page Links
# =============================================================================


for link in Year_links_list:
    
    #website_url = requests.get("https://en.wikipedia.org/wiki/The_New_York_Times_Fiction_Best_Sellers_of_1986").text
    website_url = requests.get(link).text
    soup = bs4.BeautifulSoup(website_url,"lxml")
    #print(soup.prettify())
    
    ind_years_table  = soup.find("table", {"class":"wikitable"})
    
    
    findtr = ind_years_table.find_all("tr")
# 1st find all the table rows
# then inside each row find all the cells
# inside each cells find all the links, but 
# I only want the links in the 3rd column
# So start from the 3rd cell (ie index 2) go to the end indexing by 3
    authors_page_links = []
    for i in findtr:
        cells = i.find_all("td")
        if len(cells)==3:
            for i in cells[2::3]:
                finda = i.find_all("a")
                for i in finda:
                    authors_page_link= i['href']
                    text = i.get_text()
                    authors_page_links.append(authors_page_link)
                    #print(authors_page_links, text)
    real_authors_page_links = []
    https_string = "https://en.wikipedia.org"
    for author in authors_page_links:
        res =  https_string + author
        real_authors_page_links.append(res)
 

# To error and time check part 2 or parts 1&2 uncomment the following lines:
       
#print(real_authors_page_links)        
#end_time = datetime.datetime.now()
#print(end_time - start_time)   
        
        
        
# =============================================================================
#     
# Part 3 - Scraping Each Authors Page in order to get Marriage Status 
# and if they ever had kids   
#     
# =============================================================================

import requests 
import pandas as pd
import bs4
import re
import datetime

from pandas.io.html import read_html        
        
        
df_rows = []
real_authors_page_links =["https://en.wikipedia.org/wiki/Ken_Follett" ]       
for link in real_authors_page_links:

    page = link
    response = requests.get(link)
    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')
    
        title = html.select("#firstHeading")[0].text
        #print(title)
    
    
    infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})
    #wikitables = read_html(page, index_col=0, infer_types=False, attrs={"class":"wikitable"})
    
    #print( "Extracted {num} infoboxes".format(num=len(infoboxes)))
    #print "Extracted {num} wikitables".format(num=len(wikitables))
    df_1 = infoboxes[0]
    df_2 =df_1.T.astype(str)
    df_row = {}
    
    column_list = []
    for columnName in df_2:
        column_list.append(columnName)
    if 'Spouse' in column_list:
        marr_sentence = df_2['Spouse'][0]
        spouse = re.compile(r'([A-Z]\w+\s[A-Z]\w+)', flags = re.M)

        if len(marr_sentence) != 0:
            spouse_name = spouse.findall(marr_sentence)
            has_spouse=1
        else:
            spouse_name = []
    else: 
        df_row['has_spouse'] = 0



    if 'Children' in column_list:
        children_sentence = df_2['Children'][0]
        
        def children_getter(children_sentence):
            #children = re.compile(r'(\d)|([A-Z]\w+\s[A-Z]\w+)', flags = re.M)
            # Need to add in an or statement to pick up just single capitalized words
            
            children = re.compile(r'(\d)', flags = re.M)
            children_name = children.findall(children_sentence)
            if len(children_name) == 0:
                 children = re.compile(r'([A-Z]\w+\s[A-Z]\w+)', flags = re.M)
                 children_name = children.findall(children_sentence)
                 num_children = len(children_name)
            else: 
                
                num_children = int(children_name[0])
            return num_children
        
    else:
        df_row['has_children'] = 0 
        df_row['num_children']=0
        children_sentence = None
        children_name = None
        num_children= 0
        
    df_row['author_name'] = title
    df_row['spouse_name'] = spouse_name
    df_row['children_string'] = children_sentence
    df_row['children_name'] = children_name
    df_row['num_children'] = num_children
    df_row['spouse'] = has_spouse
    
    

    df_rows.append(df_row)
df = pd.DataFrame(df_rows)





# =============================================================================
# children_pattern = re.compile(r'([A-Z][^\\.;]*(?:children)[^\\.;]*)', flags = re.M)
#             children_sentence = children_pattern.findall(intro)
#             children = re.compile(r'([A-Z]\w+\s[A-Z]\w+)', flags = re.M)
#             # We are going to have some errors here, the regex will find any two word combinations that
#             # both capitalized. So it will pick up more than just the name of a kid. 
#             if len(children_sentence) != 0:
#                 children_name = children.findall(children_sentence[0])
#             else:
#                 children_name = []
#             num_children = len(children_name)
#             has_spouse = 0
#             if len(spouse_name) != 0:
#                 has_spouse = 1
#             else:
#                 has_spouse = 0
# =============================================================================







# =============================================================================
# This is for printing out the Info Boxes Line by Line
# null = len(infoboxes)==0
# 
# for x in range(len(infoboxes)):
#     first = infoboxes.iloc[x][0]
#     second = infoboxes.iloc[x][1] if not null.iloc[x][1] else ""
#     print(first,second,"\n")
# 
# 
# 
# import pandas
# urlpage =  'https://en.wikipedia.org/wiki/Star_Trek'
# data = pandas.read_html(urlpage)[0]
# null = data.isnull()
# 
# for x in range(len(data)):
#     first = data.iloc[x][0]
#     second = data.iloc[x][1] if not null.iloc[x][1] else ""
#     print(first,second,"\n")
# 
# 
# =============================================================================











