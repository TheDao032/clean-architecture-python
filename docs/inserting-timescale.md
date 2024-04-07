# Guideline for application loop on the hypertable
- In this application, we will implement the clean architecture for creating the loop to insert the data into the timescale database in the time interval.
- The architecture will deploy the app on the container and the database will be hosted on the local VM.
- The local VM will need to setup the database and the user for the application to manage
- Step by step:
+ Config the database with the timescale database
+ Setup the database with the hypertable
+ Develop the application based on the clean architecture on python
+ Setup the enviroment variable
# Build the application
## clean-architecture application
Prepare the entities -> Build the dtos for ensuring the parameters tranmission between each layers. -> Build the database interaction command (querry for R operrations and command for CUD operations) -> Implement the interface if necessary
## Docker build
docker build . -t webapp -f docker-files/webapp-Dockerfile
docker container run -d --name dumpapp --env-file ./.env webapp