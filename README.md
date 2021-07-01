# Overview
Deployment of production grade WAF is challenging. Usually it takes at least several weeks for an average team to learn, design, implement and automate a WAF deployment. However, system design principles are always the same and every team ends up building a similar system.

The main purpose of this project is to provide an AWS CloudFormation template that follows system design principles and deploys complete, production grade WAF solution to AWS cloud. 

# Solution
The idea behind this solution is to provide a production grade WAF data plane and streamline day to day WAF operations via user friendly interfaces for configuration and visibility. Following picture represents high level architecture.

![High-Level Architecture](images/high-level-architecture.png)

Solution consists of three main components:
1. WAF data plane
2. Interface for WAF configuration 
3. Interface for WAF visibility

Data plane uses official NGINX App Protect AMIs as a WAF engine. It is fully maintenance-less, automated and auto-scales up and down based on amount of traffic flying through.

GitOps is used as configuration approach. AWS CodeCommit git repo contains default configuration for a WAF. After that every configuration change user commits in git automatically applies to the running WAF data plane.

Data plane VMs continiously send logs and metrics to AWS CloudWatch. It in turn provides a dashboard with detailed visibility to WAF security and performace.

Therefore, the solution allows to use a WAF from day zero. It provides maintnaince free data plane, convinient tool for configuration management, and complehensive visibility to the system.

Once deployed solution becomes your own SaaS WAF. To protect an application just redirect traffic to your WAF and configure to forward it back to your backend. You are free to protect more than one application. All features for standalone NGINX applicatible here as well.

# Get Started

## Deployment
Deployment process is standard as for any other CloudFormation template.
1. Download template from `templates` folder to your filesystem
2. Open AWS CloudFormation console and click "Create Stack"
3. Select "Upload from a template file" and upload template from local filesystem
4. Give stack a name. All other parameters are optional.
5. Set a checkbox against "I acknowledge that AWS CloudFormation might create IAM resources with custom names."
6. Click create stack.

Or use following command to create a stack using aws cli:
```
$ aws cloudformation create-stack --stack-name NAME_OF_YOUR STACK \
    --capabilities CAPABILITY_NAMED_IAM \
    --template-body https://raw.githubusercontent.com/464d41/aws-waf-solutuon-template/master/templates/nginx-plus-app-protect-ubnt1804-dev.template.yaml
```

## Operations
Once stack deploys successfully you can access, configure and monitor a WAF.
### Access
Navigate to "CloudFormation -> Your Stack -> Outputs" and click on "AppProtectLBDNSName". WAF returns a default static page.
### Configuration
Navigate to "AWS CodeCommit Service -> nap-AppProtectRepo". NGINX configuration locates at "files/etc/nginx/nginx.conf". App Protect configuration lives in "files/etc/app_protect". Modify these files in the same way you would do for standalone NGINX and commit changes. New configuration will be applied to the data plane automatically. You can monitor config deployment process in "AWS CodePipeline Service -> nap-AppProtectPipeline"
### Monitoring
Open "AWS Cloudwatch -> Dashboards -> nap-AppProtectDashboard". This dashboard contains various security and performance related data.
![Dashboard](images/dashboard.png)
# Contribution
This is a community project. Everyone is welcome to contribute.
# License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)