# Amazon Web Services (AWS) Lambda

hid-sp18-511

AWS Lambda is serverless computing model. It has the following features

*	No servers to manage - There is no server to manage in terms of patching, upgrade etc. AWS will take care of all these things.
*	Scales with usage - It increase or decrease the capacity as per the demand
*	Never pay for idle - Customer will pay only for the time when the function was called
*	Availability and fault tolerance are build in and AWS take care of this

## Steps to create Python function using AWS lambda.

#### Step 1 - Login to AWS console using credentials

Open https://aws.amazon.com/ and provide the credentials

#### Step 2 - Select Lambda services from the dropdown

![AWS Lambda Selection](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_selection.png?raw=true)

#### Step 3 - The following screen will appear once Lambda service is selected

![AWS Lambda Screen](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_screen.png?raw=true)

#### Step 4 - Click on Create a function button. The following screen will appear to create the function 

![AWS Lambda Type](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_type.png?raw=true)

There are three type of to create the function

*	Author from scratch - Create the function from scratch
*	Blueprints - Create function using AWS provided templates
*	Serverless Application Repository - Use the code developed by other developers, companies and partners of AWS

#### Step 5 - We will use Author from scratch type to create the function for this tutorial. Select the Author from scratch option and provide the following details

##### Name - Provide meaningful name for the function. We will provide awsTutorialFunction as function name for this tutorial

![AWS Lambda Function Name](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_name.png?raw=true)	

##### Runtime - Provide the programming language in which the function will be created and appropriate run time for that

![AWS Lambda Function Runtime](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_runtime.png?raw=true)	

Following runtime environment are available

* C# (.NET Core 1.0)
* C# (.NET Core 2.0)
* Go 1.x
* Java 8
* Node.js 4.3 
* Node.js 6.10
* Python 2.7
* Python 3.6

We will use Python programming language for this tutorial to create the function hence select Python 3.6 Runtime environment

![AWS Lambda Function Runtime Python](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_runtime_python.png?raw=true)	
