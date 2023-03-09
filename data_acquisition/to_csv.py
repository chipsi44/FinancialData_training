import pandas as pd
def create_pandasDF_financeYahoo(entreprise_list,my_header_list) :
    for elem in entreprise_list :
        elem.pop()  # remove the last element of each inner list
    df = pd.DataFrame(data=entreprise_list, columns=my_header_list)
    return df

