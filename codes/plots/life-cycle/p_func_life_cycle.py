
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



