# Guideline for application loop on the hypertable
- In this application, we will implement the clean architecture for creating the loop to insert the data into the timescale database in the time interval.
- The architecture will deploy the app on the container and the database will be hosted on the local VM.
- The local VM will need to setup the database for the application connect to.
- The database can be managed revisions by alembic modules
Step by step:
Config the database with the timescale database -> Setup the database with the hypertable -> Develop the application based on the clean architecture on python-> Setup the enviroment variables -> Build the image and the container for deploying steps
## Setup the database
Initally, the database will be run on the local by posgresql with the default schema. This version will need to create the database, user with the permission for the application. Install and config the timescale extension and config the permissions. The summary process:
Install the postgresql -> Create database, user and grant the permission -> Config the database for allowing connection with IPv4 -> Install timescale db extension -> Grant the permission if necassary for the application's user in the previous step. Create and connect the table to the hypertable.
## Build the application
Create the full application follow the clean architecture by the Python. We can setup the application as the web app or the normall one. From the config to setup database connection will follow this orders: local variable from application > value from .env files > enviroment variables
The general implementation steps:
Prepare the entities -> Build the dtos for ensuring the parameters tranmission between each layers. -> Build the database interaction command (querry for R operrations and command for CUD operations) -> Implement the interface if necessary
## Docker build
This application will be deployed on the docker manually. The project will organize based on the modules: application - database - docker built files
The docker command include:
docker build . -t webapp -f docker-files/webapp-Dockerfile
docker container run -d --name dumpapp --env-file ./.env webapp