This repository demonstrates how to automate the deployment process with AWS CodePipeline and CodeBuild.

## Overview

### Files Structure:

- **template.yml**: SAM template to define a Lambda function triggered by an API Gateway.
- **buildspec.yml**: Defines the build process for CodeBuild, including packaging the CloudFormation template.
- **lambda_function.py**: Python Lambda function that responds with a simple message.
- **requirements.txt**: Dependencies for the Python Lambda function.
- **SAM_Backend_Template.yml**: CloudFormation template for setting up IAM roles, CodePipeline, and CodeBuild.

### Main Components:

1. **Lambda Function**: A simple Python function (`lambda_function.py`) that gets triggered by an API Gateway endpoint (`/test`) using a GET request.
2. **API Gateway**: An endpoint `/test` that triggers the Lambda function.
3. **AWS CodePipeline**: Automates the deployment of the Lambda function and its associated resources using CloudFormation.
4. **AWS CodeBuild**: Used for building and packaging the Lambda code.

## Files Explained

### template.yml

This defines an AWS Lambda function (`MySAMLambda`) using the Serverless Application Model (SAM) that is triggered by an API Gateway endpoint `/test`.

```yaml
Resources:
  MySAMLambda:
    Type: AWS::Serverless::Function
    Properties:
      Handler: lambda_function.lambda_handler
      Runtime: python3.10
      CodeUri: ./lambda_function.py
      MemorySize: 128
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /test
            Method: get
```

### buildspec.yml

This file specifies the commands to be run during the build phase in AWS CodeBuild. It installs dependencies, packages the CloudFormation template, and uploads it to an S3 bucket.

```yaml
version: 0.2
phases:
  build:
    commands:
      - cd TabTestBackEndRepo
      - pip install -r requirements.txt -t .
      - aws cloudformation package --template-file template.yml --output-template-file template-out.yml --s3-bucket <your-s3-bucket>
artifacts:
  files:
    - template.yml
    - template-out.yml
  base-directory: TabTestBackEndRepo
```

### lambda_function.py

The Lambda function that returns a basic JSON message when triggered.

```python
def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from my Lambda version 03!"
        })
    }
    return response
```

### SAM_Backend_Template.yml

This template sets up the necessary IAM roles, CodePipeline, CodeBuild, and CloudFormation stack for deploying the backend service. It uses parameters to define the repository, branch, and S3 bucket for the pipeline.

### How to Deploy

1. **Upload Code to Remote Repository**:
   Upload following to remote repository I used bitbucket

   - `template.yml` file.
   - `buildspec.yml` file.
   - `lambda_function.py` file.
   - `requirements.txt` file.

   I placed above files in `TabTestBackEndRepo` folder and uploaded them

2. **Set up CodePipeline**:
   Use the `SAM_Backend_Template.yml` to create the necessary CodePipeline and CodeBuild resources.
   Deploy the template via CloudFormation to set up continuous integration and deployment.

### Notes

- Ensure to change configuration according to your needs.
- Some resources should already be created like **bitbucket connection** and **s3 bucket**

### Conclusion

This project demonstrates how to build a serverless application using AWS Lambda, API Gateway, and CloudFormation. The automation provided by CodePipeline and CodeBuild ensures that deployment is smooth and repeatable.

### 📺 [Watch on YouTube](https://www.youtube.com/watch?v=6SSLBfOZOtQ&t=548s)
