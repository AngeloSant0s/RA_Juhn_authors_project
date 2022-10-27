# Life Cycle plottings

In this routine we will plot the graphs related to authors life cycles for the [Library of Congress](https://www.loc.gov) and [New York Best sellers](https://www.nytimes.com/books/best-sellers/) datasets. We will plot two graphs:

1. Probabilities of publishing
2. Female male ratio of publishing probabilities
 
These graphs will be ploted for three groups: All books, fiction and non fiction.

## Packages needed

```{code-cell}
:tags: ["hide-input"]

import os 
import pandas as pd
import seaborn as sns
import p_func_life_cycle as plc
from matplotlib import pyplot as plt
```
## To make our graphs looking good
To make your graphs looking better, we will use some predefined settings. You can customize it as you want. These
are our settings.

```{code-cell}
:tags: ["hide-cell"]

plt.rcParams['figure.dpi'] = 500
plt.rcParams['savefig.dpi'] = 500
sns.set_style('ticks')
sns.despine(left=False, bottom=True)
sns.set_context("paper")
```

```{warning}
**p_func_life_cycle** is a file with the [functions](functions) used through the routines.
```

(functions)=
## Functions

These are the set of functions used in the following routine

```{code-cell}
:tags: ["hide-input"]

def lc_cohort(lc_frame , st = 1900, ed = 2000, size = 15):
    """
    
    This function creates the cohort variable for the life cycle data

    Parameters
    ----------
    lc_frame : DataFrame
        Life cycle dataframe
    st : int, optional
        Starting year of birth, by default 1900
    ed : int, optional
        Last year of birth, by default 2000
    size : int, optional
        Size of cohorts years window, by default 15

    Returns
    -------
    DataFrame
        The life cycle DataFrame with a colum that indicates the authors' cohort
    """
    nb_co = int((ed-st)/size)
    for c in range(nb_co):
        start = st+ c*size
        print(start)
        end = st + (c+1)*size
        print(end)
        lc_frame['Cohort_'+str(start)[2:] +'_' + str(end)[2:]] = 0
        lc_frame.loc[(lc_frame['birth_year'] >= start) & (lc_frame['birth_year'] < end), 'Cohort_'+str(start)[2:] +'_' + str(end)[2:]] = 1
    return lc_frame



def cohorts_fun(start,end,size):
    """
    
    This function creates two lists with labels and cohort variable

    Parameters
    ----------
    start : int, optional
        Starting year of birth, by default 1900
    end : int, optional
        Last year of birth, by default 2000
    size : int, optional
        Size of cohorts years window, by default 15


    Returns
    -------
    coh and cys
        two lists with labels and cohort variable
    """
    coh = []
    cys = []
    for c in range(start,end,size):
        co = 'Cohort_'+str(c)[2:]+'_'+str(c+size)[2:]
        cy = str(c)+' - '+str(c+size)
        cys.append(cy)
        coh.append(co)
    return coh, cys

def coh_columns(data, coh, cys, cols, col_g_f, col_g_m, coh_all = []):
    """
    
    This function creates a data set with information based on the life cycle dataset

    Parameters
    ----------
    data : DataFrame
        dataset used to create the new Dataframe
    coh : list
        Column name for cohorts in the lifecycle dataset (e.g.: 'Cohort_35_50')
    cys : list
        Label for cohorts (e.g.: '1935 - 1950')
    cols : list
        columns where the information are seen in the lifecycle dataset
    col_g_f : list
        Colum for females 
    col_g_m : list
        Colum for males 
    coh_all : list, optional
        Empty list to append rows, by default []

    Returns
    -------
    DataFrame
        DataFrame with cohort level information 
    """
    for c, ch in enumerate(coh):
        cohort = data.loc[data[ch] == 1].reset_index().drop('index', axis = 1)
        cohort_male = len(cohort.loc[cohort['gender'] == 'male']['ID'].unique())
        cohort_female = len(cohort.loc[cohort['gender'] == 'female']['ID'].unique())
        cohort = cohort[['age','gender','published','qt_published','fic_and_nfic','fiction','non_fiction']]
        cohort = cohort.groupby(['age','gender']).sum().reset_index()
        cohort = cohort.loc[cohort['age'] >19]
        life_coh = []
        for age in range(20,cohort.age.max()+1):
            sliced = cohort.loc[cohort['age'] == age].reset_index().drop('index', axis = 1)
            dic = {}
            dic['Age'] = age
            for c_nb,col in enumerate(cols):
                dic[col_g_f[c_nb]] = sliced.loc[sliced['gender'] == 'female'][col][0]/cohort_female
            dic_m = {}
            dic['Age'] = age
            for c_nb,col in enumerate(cols):
                dic[col_g_m[c_nb]] = sliced.loc[sliced['gender'] == 'male'][col][1]/cohort_male
    #        for c_nb,col in enumerate(cols):
    #           dic[col_g_r[c_nb]] = (cohort_male/cohort_female)*(sliced.loc[sliced['gender'] == 'female'][col][0]/sliced.loc[sliced['gender'] == 'male'][col][1])
            dic['Cohort'] = cys[c]
            life_coh.append(dic)
        coh_all.append(pd.DataFrame(life_coh))
    coh_all = pd.concat(coh_all, axis = 0).reset_index().drop('index',axis=1)
    return coh_all
```