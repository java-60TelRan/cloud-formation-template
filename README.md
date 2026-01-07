# HW#48 Definition
## Update travel_info application and create & push new docker image
### introduce environment variable for ollama model<br>
- update code containing request to ollama model implying using environment variable containing a model name value 
- set default value of environment variable as phi3:mini inside Dockerfile. It allows updating of  model with no rebuild / redeployment, just run another model and restart container with appropriate env. variable
### introduce security with authorization
- Each user in Cognito user's pool may have groups array for authorization like the roles
- Write dependent function for admin role and use it in GET /travel/info with countryFrom and  cuntryTo/cityTo parameters. This function should check x-cognito-groups header in request and array "groups" should contain "admin". How to get the x-cognito-groups header see below
## Update some user implied to be the admin from Cognito user's pool
- add groups containing "admin"

## Update existing YAML file for stack running travel_info application
- cloud-init script should install ollama, pull phi3 model (better phi3:mini)<br>
- add section RequestParameters inside NlbIntegration section adding mapping of header x-cognito-groups with Cognito authorizer appropriate request context parameter (Ask ChatGPT how to do it)
## Create CloudFormation stack based on updated YAML template and parameters
- instance type should be t3.2_xlarge (not less than t3.xlarge)
- project name: travel_info_app
## Run tests using Postman
## VERY IMPORTANT: after testing MUST delete whole stack (having YAML template file creating/deleting stack will be a deal of several minutes only)