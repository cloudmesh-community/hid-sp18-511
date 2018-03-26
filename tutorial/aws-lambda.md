# Amazon Web Services (AWS) Lambda

hid-sp18-511

AWS Lambda is serverless computing model. It has the following features

*	There is no servers to manage - There is no server to manage in terms of patching, upgrade etc. AWS will take care of all these things and customer need not to worry about it.
*	Scales up and down as per demand - The capacity gets increased or decreased as per the demand
*	Pay what is used - Customer will pay only for the time when the function was called
*	Availability and fault tolerance are build in and AWS take care of this as this is part of AWS Global Infrastructure

## Steps to create Python function using AWS lambda

#### Step 1 - Login to AWS console using credentials

Open https://aws.amazon.com/ and provide the credentials

#### Step 2 - Select Lambda services from the dropdown

![AWS Lambda Selection](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_selection.png?raw=true)

#### Step 3 - The following screen will appear once Lambda service is selected

![AWS Lambda Screen](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_screen.png?raw=true)

#### Step 4 - Click on Create a function button. The following screen will appear to create the function 

![AWS Lambda Type](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_type.png?raw=true)

There are three options to create the function

*	Author from scratch - Create the function from scratch
*	Blueprints - Create function using AWS provided templates
*	Serverless Application Repository - Use the code developed by other developers, companies and partners of AWS

We will use Author from scratch type to create the function for this tutorial. Select the Author from scratch option.

#### Step 5 - Provide the following information for the function

##### Name - Provide meaningful name for the function. Provide awsTutorialFunction as function name for this tutorial

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

##### Role - Create the role with permissions that AWS lambda will use to call the Lambda function

![AWS Lambda Function Role](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_role.png?raw=true)	

Following options are available to create the role

* Create new role from template(s) - AWS Lambda will create the role with permission from the selected policy templates
* Create a custom role - User can create the role with customized permissions

We will use Create new role from template(s) option to create the role for this tutorial. Please use Create new role from template(s) option from the dropdown list

![AWS Lambda Function Role Selection](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_role_select.png?raw=true)	

##### Role name - Enter the meaningful name for the role. Provide awsTutorialFunctionRole role name for this tutorial

![AWS Lambda Function Role Name](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_role_name.png?raw=true)	

##### Policy templates - Choose the policy based on the requirement. These policy will be added to the role defined and AWS lambda will use those policy and permission to access resources. There are various policy available to be used.

![AWS Lambda Function Policy](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_policy.png?raw=true)	

Select Simple Microservice permissions from the list. This will be sufficient to run the code for this tutorial

![AWS Lambda Function Policy Select](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_policy_select.png?raw=true)	


#### Step 6 - Click on Create function button. The following screen will appear

![AWS Lambda Function Def](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_definition.png?raw=true)	

Following information has to be updated for this tutorial. Please go through AWS Lambda documentation for information about other options and configurations

![AWS Lambda Function Options](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_option.png?raw=true)	

##### Code entry type - Provide the options to provide the code. Following options are available 

* Edit code inline - Use this option to edit the code inline in the function page itself
* Upload a .ZIP file - Use this option if you would like to upload the code in zip format. Provide the zip file location and upload the file.
* Upload a file from Amazon S3 - Use this option if you have the code in S3 bucket. Provide the bucket URL in the configuration.

We will use Edit code inline option for this tutorial. Edit the code as per the requirement.

![AWS Lambda Function Edit](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_edit.png?raw=true)	

##### Runtime - Provide/Edit the programming language for the code that you are planning to provide for Lambda. For now keep it as Python 3.6.
##### Handler - This is the function name in your code which will be calles by AWS Lambda to start the execution. Leave it as lambda_function.lambda_handler

#### Step 6 - Click on Save button to save the configuration of the function. The function is ready to be used

![AWS Lambda Function Save](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_save.png?raw=true)	


## Steps to test Python function created using AWS Lambda

Click on Test button to test the function created. The function will provide the result of the execution and summary of the resources being used.

![AWS Lambda Function Test](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_test.png?raw=true)	

## Steps to delete Python function created using AWS Lambda

Click on Actions->Delete function button to delete the AWS Lambda function if not required.

![AWS Lambda Function Delete](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_delete.png?raw=true)	
