from data_acquisition.thread_scrapping import launch_threading
import pandas as pd
import os

def main() :
    filename = "data/financeYahoo_dataframe.csv"
    if os.path.exists(filename):
        os.remove(filename)
    df1,df2 = launch_threading()
    #concat the 2 DataFrame
    df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
    #export it as a CV
    df_concat.to_csv(filename, index=False)

if __name__ == "__main__" :
    main()