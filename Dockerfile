# Use the official Python image as a parent image
FROM python:3.11.1
# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the necessary dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
# Copy the DAG file into the container
COPY dag_file_airflow.py /app/dags/

# Set the AIRFLOW_HOME environment variable
ENV AIRFLOW_HOME=/app

# Initialize the Airflow database
RUN airflow db init

# Start the scheduler and webserver
CMD ["sh", "-c", "airflow scheduler & airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin & airflow webserver"]
