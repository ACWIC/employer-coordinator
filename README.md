# employer-coordinator
Operations management for the employer services

This app contains the recipes for development and deployment of the employer services together.
 
 ## How to run:
 First clone the project with the submodules. These submodules include the individual services.
 
 `git clone --recurse-submodules git@github.com:ACWIC/employer-coordinator.git`
 
 
 to run for development
``` shell script
    docker-compose -f local.yml build
    docker-compose -f local.yml up
```
The services will be available on port 8081, and 8082

Open `localhost:8081/docs` for the `callback` service swagger documentation.
Open `localhost:8082/docs` for the `admin` service swagger documentation.



## Production configuration:
There's two expected environment variables:

`STAGE_PREFIX`: API gateways add a prefix after the domain, but it's not passed down to the service.
But if the service is called from a Javascript application like swagger UI, the prefix has be provided.
`STAGE_PREFIX` should is expected to be provided by the serverless runner.


`SERVICE_PREFIX`: When deploying more than one service under the same API gateway, a prefix is used to
map to each service. this prefix is passed to the service itself, and all URLs are expected to be prepended
with it. (unlike the `STAGE_PREFIX`)
