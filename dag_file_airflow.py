from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from data_acquisition.thread_scrapping import launch_threading
import pandas as pd
import os
import sqlite3

def dag_scrapping() :
    filename = "dags/data/financeYahoo_dataframe.csv"
    if os.path.exists(filename):
        os.remove(filename)
    df1,df2 = launch_threading()
    #concat the 2 DataFrame
    df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
    #export it as a CV
    df_concat.to_csv(filename, index=False)
    ''' # Create a connection to the SQLite database file
    conn = sqlite3.connect('data/my_database.db')
    # Write the DataFrame to a SQLite database table
    df_concat.to_sql('stocks', conn, if_exists='replace', index=False)
    # Close the database connection
    conn.close()'''

# Define default arguments for the DAG
default_args = {
    'owner': 'Cyril_AI',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 12, 23), # start at 23:00
    'retries': 0
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


scrap_financeYahoo_operator

'''
t1 = DockerOperator(
        task_id='copy_file_to_local',
        image='docker',
        api_version='auto',
        command='cp monapp-container:/app/dags/data/financeYahoo_dataframe.csv ./data',
        network_mode='bridge',
        docker_url='unix://var/run/docker.sock',
        volumes=['C:/Users/Cyril/Desktop/BeCode/data/:/data'],
        auto_remove=True
    )
'''
# -------------------------
'''
from data_acquisition.thread_scrapping import launch_threading
import pandas as pd
import os
import sqlite3

def main() :
    filename = "data/financeYahoo_dataframe.csv"
    if os.path.exists(filename):
        os.remove(filename)
    df1,df2 = launch_threading()
    #concat the 2 DataFrame
    df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
    #export it as a CV
    df_concat.to_csv(filename, index=False)
    # Create a connection to the SQLite database file
    conn = sqlite3.connect('data/my_database.db')

    # Write the DataFrame to a SQLite database table
    df_concat.to_sql('stocks', conn, if_exists='replace', index=False)

    # Close the database connection
    conn.close()
if __name__ == "__main__" :
    main()

'''