# __FinancialData_training__

## __deliverables :
* This is a collaborative learning project involving multiple individuals. As a data engineer, it was my responsibility to ensure the following tasks were completed:
    * Create a scrapper that obtains financial information from at least two sources (e.g. Yahoo Finance and Google News). 
    * Adapt your solution to use Airflow to schedule and update the data from your sources. 
* Create a tutorial on how to use Airflow, Docker, and Selenium together :
      * [Tutorial with exercises](https://github.com/chipsi44/SeleniumAirflowDocker).
      * [Corrected tutorial](https://github.com/chipsi44/SeleniumAirflowDocker/tree/Corrected_Tuto).

## __How to use?__

Install Docker and pull the Selenium Grid images for Firefox.
Create a Docker network and run the Selenium Grid images in the network :
* docker pull selenium/standalone-firefox 
* docker network create my-network
* docker run -d --network my-network --name selenium-container -p 4444:4444 selenium/standalone-firefox:latest

You can now create a Docker image with my Dockerfile and run the image in the same network :

* docker build -t my_airflow_container:latest . 
* docker run -d --network my-network --name monapp-container -p 8080:8080 my_airflow_container:latest     

You can now access the Selenium Grid on local port 4444 and the Airflow web interface on local port 8080. You can manually launch my DAG and see that sessions will be created on the Selenium Grid. Afterwards, you can extract the file using:

* docker cp monapp-container:/app/dags/data/financeYahoo_dataframe.csv ./data 

## __How to do it ?__ 
### &nbsp; __1. The scrapping :__
&nbsp;&nbsp;&nbsp;&nbsp;While this project does not primarily focus on web scraping, I have developed a simple scraping code to extract data from Yahoo Finance. Using Selenium and Pandas, I have scraped the [first two pages of the most active stocks](https://finance.yahoo.com/most-active) to obtain information.
### &nbsp;__2. Threading :__
&nbsp;&nbsp;&nbsp;&nbsp;To improve the efficiency of the web scraping process, I have implemented threading to run the scraping of the two pages simultaneously. Each thread returns a Pandas dataframe which is then concatenated and transformed into a CSV file upon completion of both threads. 
### &nbsp;__3. Deployment :__
&nbsp;&nbsp;&nbsp;&nbsp;In order to automate the web scraping process on a daily basis, I have decided to use Apache Airflow. However, I soon realized that using Airflow with Docker would be necessary to facilitate the deployment of the pipeline. Additionally, due to the usage of Selenium for web scraping, Selenium Grid would be required for Dockerized deployment.
### &nbsp;__Selenium grid :__
__&nbsp;&nbsp;*What's Selenium grid ?*__

&nbsp;&nbsp;&nbsp;&nbsp;Using Selenium Grid with Docker provides a scalable and efficient solution for running automated tests or web scraping tasks across multiple environments. Docker enables the creation of lightweight, isolated containers that can be easily deployed and managed. By integrating Selenium Grid with Docker, users can easily distribute tests or web scraping tasks across multiple containers, each running on different operating systems and browsers.

__&nbsp;&nbsp;*How to use selenium grid ?*__

&nbsp;&nbsp;&nbsp;&nbsp;To utilize Selenium Grid in my project, I first pulled the Docker image of the Selenium Grid for Firefox and then ran the image within my Docker environment to create a container of Selenium Grid. The container was then configured to run on port 4444.
To modify my code for the web scraping process, I had to specify that the browser being used was no longer Firefox, but a remote WebDriver using the Selenium Grid container running on selenium-container:4444.

&nbsp;&nbsp;&nbsp;&nbsp;After configuring my project to utilize Selenium Grid with Docker, I was able to successfully run my web scraping process from my IDE (VSC). By checking the Selenium Grid dashboard, I could see that sessions were created and successfully executed.Once the web scraping process was completed, I obtained the resulting data in a CSV file format, similar to my previous implementation. However, the key difference now is that the web scraping process is executed on the Selenium Grid, providing the benefits of distributed execution.
### &nbsp;__*Apache airflow* :__
__&nbsp;&nbsp;*What's Apache airflow ?*__

&nbsp;&nbsp;&nbsp;&nbsp;Apache Airflow is a platform for creating and managing complex data processing workflows. It uses Directed Acyclic Graphs (DAGs) to represent workflows as a collection of tasks with dependencies between them. Airflow provides a web interface for monitoring and managing workflows, allowing users to view the status of running and completed tasks, and to visualize the workflow as a DAG. Workflows can be scheduled to run at specific times or in response to certain events, providing a powerful tool for automating data processing tasks.

__&nbsp;&nbsp;*How to use Apache airflow ?*__

&nbsp;&nbsp;&nbsp;&nbsp;First of all, I created a Python file where I wrote the necessary code to set up my DAG. I configured the DAG to start at 11 PM and run once every day. The goal of the DAG was to scrape data from the first two pages of the most active stocks and retrieve updated information every day at 11 PM.

&nbsp;&nbsp;&nbsp;&nbsp;Now that my DAG is created, I can launch it manually using the Apache Airflow web interface. To set up the web interface, I need to create a Dockerfile that launches the Airflow scheduler, creates an admin user, and then starts the Airflow web server.

&nbsp;&nbsp;&nbsp;&nbsp; With my DAG created and the Apache Airflow web interface up and running, I attempted to manually execute the DAG. However, the execution failed due to issues with accessing Firefox and communicating with the Selenium grid. To resolve this issue, I need to dive into Docker and configure it appropriately.

### &nbsp;__*Docker* :__
__&nbsp;&nbsp;*What's Docker ?*__

&nbsp;&nbsp;&nbsp;&nbsp;Docker is a containerization platform that allows developers to package applications and their dependencies into lightweight and portable containers. It provides a consistent environment for running applications, regardless of the underlying operating system or hardware.

&nbsp;&nbsp;&nbsp;&nbsp;In the case of Apache Airflow, it can be difficult to run the web interface on Windows due to differences in how Windows and Linux handle certain system resources. However, by using Docker, Windows users can run Apache Airflow and its web interface within a Linux-based container, which avoids these compatibility issues. Docker provides a way to create and manage these containers easily, allowing Windows users to run Apache Airflow and other applications seamlessly on their machines.

__&nbsp;&nbsp;*How to use Docker ?*__

&nbsp;&nbsp;&nbsp;&nbsp;As mentioned earlier, I encountered two issues while using airflow. Firstly, Firefox was unable to run inside the Docker container and secondly, Selenium grid was not accessible. To resolve these issues, I had to install Firefox dependencies inside the Docker container by adding the relevant command in my Dockerfile. Once the installation was complete, I created a Docker network to enable communication between the two containers.

&nbsp;&nbsp;&nbsp;&nbsp;I have successfully launched both containers inside the same network and ran the DAG manually from the Apache Airflow web interface. I can see that the sessions are getting created in the Selenium Grid. The next step is to extract the file created in the Docker containers.

### &nbsp; __4. Getting the file :__
&nbsp;&nbsp;To retrieve a file from a Docker container, the "docker cp" command is used. The final step of my project involved executing this command to verify the correctness of the CSV file containing the relevant information. When I ran the command, I was able to retrieve the file without any issues and verify that all the required information were present in the file.


### &nbsp; __5. Possible improvement__ :
* To enhance the project further, I could have implemented the following improvements given more time: 
    * Get other data from other sources.
    * Automate the process of retrieving the CSV file by creating a DAG that uses the docker cp command.
    * Transition from CSV file to a database for better data management.
    * Host the database online and update it directly during the scraping process instead of retrieving the CSV file.

### &nbsp; __6. What's next ?__ :
&nbsp;&nbsp;During the project, I realized that there is a lack of up-to-date tutorials, exercises, and documentation on using Apache Airflow in conjunction with Selenium and Docker. As a result, I have decided to create some exercises and tutorials and provide resources to assist individuals working with this technology stack. 

&nbsp;&nbsp;I will be creating a new repository for this project, which will include a [notebook](https://github.com/chipsi44/SeleniumAirflowDocker) detailing the various steps involved. In addition, I will create a detailed and [comprehensive README](https://github.com/chipsi44/SeleniumAirflowDocker/tree/Corrected_Tuto) file to guide users through the project and provide clear instructions on how to get started. 

### &nbsp; __Contributor__ :
* [Cyril Verwimp](https://www.linkedin.com/in/cyril-verwimp-8a0457208/)
### &nbsp; __TimeLine__ :
* 10 days : 
    * FIrst day : Scrapping
    * Second day : Threading and start selenium grid
    * Third to six : Selenium, Airflow and docker
    * Six to end : Readme, tuto and exercice on another repo.
