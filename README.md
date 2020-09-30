# employer-coordinator
Operations management for the employer services

This app contains the recipes for development and deployment of the employer services together.
 
 ## How to run:
 First clone the project with the submodules. These submodules include the individual services.
 
 `git clone --recurse-submodules git@github.com:ACWIC/employer-coordinator.git`
 
 
 to run for development
``` shell script
    docker-compose build
    docker-compose up
```
The admin service will run on port 8082, and the callback service on port 8081