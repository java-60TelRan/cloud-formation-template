# HW 51 Definition
## Create Template CloudFormation YAML file
### ALB -> HTTP/HTTPS -> ECS/Fargate with Auto-Scaling 
#### Auto-Scaling policy number of requests per one minute
#### Fargate tasks family (like launch template) running Docker container 
Docker container runs fastapi-test very small application with three endpoints (health (GET), greeting (GET), user (POST))
#### Fargate service attached to tasks family 
#### Think of test cases for testing auto-scaling
some simple Python application sending many requests to ALB
viewing number of tasks from AWS console ECS/Fargate service
