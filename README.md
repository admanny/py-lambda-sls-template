# py-lambda-sls-template
A template to kickstart development of a Python based AWS Lambda function. This template uses the npm package Serverless to deploy the needed resources. 

This template assumes the Lambda function will be triggered by an SQS Qeueue. You can modify this within the `serverless.yml` file. 

## Requirements
- You should have Node.js and npm installed on your system. Additionally, you can use npx to execute serverless commands without installing the package globally.


## Configuration
In the `/config` folder you will find a `config-example.json` file. This holds two variables that you can adjust based on your AWS environment. As previously mentioned, this template assumes a SQS queue was already created. The naming convention that is followed is `config-{stage}.json`. The stage value will be passed to the serverless deploy command as a parameter.  

## Deployment
To deploy you will have to first run:

`npx sls plugin install -n serverless-python-requirements`

Once you've installed the dependent plugin you can deploy the lambda function using:

`npx sls deploy --stage dev`

***Note:** You can pass whatever value you'd like to stage. Make sure you have a corresponding `config-{stage}.json`.*