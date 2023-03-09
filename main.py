from data_acquisition.scrapping import main_scrap_financeYahoo
from data_acquisition.to_csv import create_a_CSV

entreprise_list,my_header_list = main_scrap_financeYahoo("https://finance.yahoo.com/most-active?offset=0&count=100")
create_a_CSV(entreprise_list,my_header_list,"data/financeYahoo_dataframe.csv")