from data_acquisition.scrapping import main_scrap_financeYahoo
from data_acquisition.to_csv import create_pandasDF_financeYahoo
from threading import Thread


class CustomThread(Thread):
    # constructor
    def __init__(self,link):
        # execute the base constructor
        Thread.__init__(self)
        # set a default value
        self.value = None
        self.link = link
    # function executed in a new thread
    def run(self):
        # store data in an instance variable
        #Scrapping
        entreprise_list,my_header_list = main_scrap_financeYahoo(self.link)
        #create data frame
        df = create_pandasDF_financeYahoo(entreprise_list,my_header_list)
        self.value = df
def scrap_it(link) :
    #Scrapping
    entreprise_list,my_header_list = main_scrap_financeYahoo(link)
    #create data frame
    df = create_pandasDF_financeYahoo(entreprise_list,my_header_list)
    return df


'''
Since we know that financeYahoo only display 200 entreprise,
we can hardcode the url to scrap on the two differents page (100 entreprise / page).
'''
def launch_threading() :
    thread1 = CustomThread("https://finance.yahoo.com/most-active?offset=0&count=100")
    thread2 = CustomThread("https://finance.yahoo.com/most-active?offset=100&count=100")
    # start the thread
    thread1.start()
    thread2.start()
    # wait for the thread to finish
    thread1.join()
    print('thread1 finished')
    thread2.join()
    print('thread2 finished')
    df1 = thread1.value
    df2 = thread2.value
    return df1,df2
