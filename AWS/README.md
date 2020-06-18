# TTN DEVOPS SECURITY AUTOMATION REPOSITORY

## Purpose
The purpose of this repository to enforce all the fine-grained security rules & automations accross all the accounts being managed by TTN.

## Rules:
- Account level restrictions
    - Access Key Creation Denied 
    - S3 Bucket ACL off denied
    - Security group 0.0.0.0 denied
    - Regional access denied apart from the main region
    - Cloudtrail disable  denied
    - Launching instance beyond a particular Instance type denied 


## Maintainers
- Nitin Bhadauria
- Harkesh Kumar
- Bijoy Paul
- Tarun Saxena
- Prashant Vats
- Neeraj Gupta
- Ranjeet Gahlot

## This repository contains the following things:
- Lambdas For AWS account security
- AWS Hardened Policies
- Security Documentation

# Update: 3rd Mar
- Added lambda & Cloudformation automation for security group having 0.0.0.0/0 rule - Tarun

# Update: 4th Mar
- Added S3 ACL lambda and terraform for it's setup and values can be changed in the variable.tf directly - Ram

# Update: 17th Mar
- Added Prowler audit report for TTN Infra and added other resources required to run Prowler - Nitish & Ekansh
- Added hardening scripts for CentOS server - Nitish
