from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from data_acquisition.thread_scrapping import launch_threading
import pandas as pd
import os

def dag_scrapping() :
    filename = "data/financeYahoo_dataframe.csv"
    if os.path.exists(filename):
        os.remove(filename)
    df1,df2 = launch_threading()
    #concat the 2 DataFrame
    df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
    #export it as a CV
    df_concat.to_csv(filename, index=False)

# Define default arguments for the DAG
default_args = {
    'owner': 'Cyril_AI',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 15, 23), # start at 23:00
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define the DAG
dag = DAG(
    'dag_scrapping', # DAG name
    default_args=default_args,
    description='Scrapp financial info on Yahoo finance',
    schedule_interval=timedelta(days=1) # run every day
)

# Define the Python Operators that will run the functions
scrap_financeYahoo_operator = PythonOperator(
    task_id='Yahoo_scrapping',
    python_callable=dag_scrapping,
    dag=dag
)

