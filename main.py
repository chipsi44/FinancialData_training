from data_acquisition.scrapping import main_scrap_financeYahoo
from data_acquisition.to_csv import create_pandasDF_financeYahoo
import pandas as pd
def main() :
    #Scrapping
    entreprise_list,my_header_list = main_scrap_financeYahoo("https://finance.yahoo.com/most-active?offset=0&count=100")
    #create data frame
    df1 = create_pandasDF_financeYahoo(entreprise_list,my_header_list)

    '''Since we know that financeYahoo only display 200 entreprise,
    we can hardcode the url to scrap on the two differents page (100 entreprise / page).
    '''
    entreprise_list,my_header_list = main_scrap_financeYahoo("https://finance.yahoo.com/most-active?offset=100&count=100")
    #create data frame
    df2 = create_pandasDF_financeYahoo(entreprise_list,my_header_list)
    #concat the 2 DataFrame
    df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
    #export it as a CV
    df_concat.to_csv("data/financeYahoo_dataframe.csv", index=False)

if __name__ == "__main__" :
    main()