import pandas as pd

def life_cycle(data, age_start = 20, age_end = 80,
               id_column = "ID", gender = 'gender_combined', birth = 'birth_year', pub = 'pub_year', fiction = 'fic_score'): 
    """
    
    This function creates the  lifecycle dataset 

    Parameters
    ----------
    data : DataFrame
        The dataframe used to create the life cycle
    age_start : int, optional
        Starting age for the authors life cycle, by default 20
    age_end : int, optional
        Lasr age for the authors life cycle, by default 80
    id_column : str, optional
        Column with authors ids, by default "ID"
    gender : str, optional
        Columns with gender information, by default 'gender_combined'
    birth : str, optional
        Birth year column, by default 'birth_year'
    pub : str, optional
        Publication year columns, by default 'pub_year'
    fiction : str, optional
        Column that tells if the publication was fiction or non fiction, by default 'fic_score'

    Returns
    -------
    DataFrame
        Returns a dataset with all the authors yearly production pooled 
    """
    lfcycles = []
    anb = 1
    for i in list(data[id_column].unique()):
            print('author:  ' + str(anb) +' of ' + str(len(list(data[id_column].unique()))))
            author = data.loc[data[id_column] == i].reset_index().drop('index', axis=1) # Finding author
            birth_y = author[birth][0].astype(int) 
            cur_year = author[birth][0].astype(int) + age_start                  # Finding year of birth
            for y in range(age_start,age_end+1): # Range of ages we want to have for each author
                if cur_year < 2022:
                    dic = {}
                    print(cur_year)
                    dic['ID'] = i
                    dic['year'] = cur_year
                    dic['age']  = cur_year - birth_y
                    dic['gender'] = author[gender][0]
                    if len(author.loc[author[pub] == cur_year]) > 0:
                        dic['published'] = 1
                    else:
                        dic['published'] = 0
                    dic['qt_published'] = len(author.loc[author[pub] == cur_year])
                    if len(author.loc[author[pub] == cur_year][fiction].unique())>1:
                        dic['fic_and_nfic'] = 1
                    else:
                        dic['fic_and_nfic'] = 0
                    try: 
                        author.loc[author[pub] == cur_year][fiction].unique()[0]
                        if author.loc[author[pub] == cur_year][fiction].unique()[0] == 1:        
                            dic['fiction'] = 1
                            dic['non_fiction'] = 0
                        else:
                            dic['fiction'] = 0
                            dic['non_fiction'] = 1                
                    except:
                        dic['fiction'] = 0
                        dic['non_fiction'] = 0 
                    lfcycles.append(dic)
                    cur_year += 1 # Add one year to create the next age row
                else:
                    continue
            anb += 1            
    lfcycles = pd.DataFrame(lfcycles)
    return lfcycles