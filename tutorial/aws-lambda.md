# Amazon Web Services (AWS) Lambda

hid-sp18-511

AWS Lambda is a serverless computing model. It has the following features as compared to traditional computing model:

*	There are no servers to manage: There is no server to manage in terms of patching, upgrade etc. 
  AWS will take care of all these things and customer need not to worry about it
*	It Scales up and down on demand: The capacity gets increased or decreased automatically on demand
*	Pay what is used: A customer will pay only for the time when the function was called. 
  A customer will not be charged when it is idle
*	Availability and fault tolerance is build in:  Availability and fault tolerance are build in and AWS takes care of 
  this as it leverages part of the AWS Global Infrastructure

## Steps to create Python function using AWS lambda

#### Step 1 - Login to AWS console

Open https://aws.amazon.com/ and provide the credentials

#### Step 2 - Select Lambda service from the dropdown

![AWS Lambda Selection](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_selection.png?raw=true)

The following screen will appear once Lambda service is selected

![AWS Lambda Screen](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_screen.png?raw=true)

#### Step 3 - Click on Create a function button. The following screen will appear to create the function 

![AWS Lambda Type](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_type.png?raw=true)

There are three options to create a lamda function

*	`Author from scratch`: Create the function from scratch
*	`Blueprints`: Create function using AWS provided templates
*	`Serverless Application Repository`: Use the code developed by other developers, companies and partners of AWS

We will use the `Author from scratch` option to create the function for this tutorial. 

#### Step 4 - Provide the following information for the function

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

We will use Python for the programming language of this tutorial to create the function.  Hence, select Python 3.6 Runtime environment.

![AWS Lambda Function Runtime Python](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_runtime_python.png?raw=true)	

##### Role - Create the role with permissions that AWS lambda will use to call the Lambda function

![AWS Lambda Function Role](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_role.png?raw=true)	

The following options are available to create the role

* `Create an existing role`:  Use existing role
* `Create new role from template(s)`: AWS Lambda will create the role with permission from the selected policy templates
* `Create a custom role`: User can create the role with customized permissions

We will use   `Create new role from template(s)` option to create the role for this tutorial. 
Please use the option from the dropdown list.

![AWS Lambda Function Role Selection](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_role_select.png?raw=true)	

##### Role name - Enter the meaningful name for the role. Provide awsTutorialFunctionRole role name for this tutorial

![AWS Lambda Function Role Name](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_role_name.png?raw=true)	

##### Policy templates - Choose the policy based on the requirement. These policy will be added to the role defined and AWS lambda will use those policy and permission to access resources. There are various policy available to be used.

![AWS Lambda Function Policy](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_policy.png?raw=true)	

Select `Simple Microservice permissions` from the list. This will be sufficient to run the code for this tutorial

![AWS Lambda Function Policy Select](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_policy_select.png?raw=true)	


#### Step 5 - Click on Create function button. The following screen will appear

![AWS Lambda Function Def](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_definition.png?raw=true)	

The following information has to be updated for this tutorial. Please go through AWS Lambda documentation for information about other options and configurations

![AWS Lambda Function Options](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_option.png?raw=true)	

##### Code entry type - Provide the options to provide the code. Following options are available 

* `Edit code inline`: Use this option to edit the code inline in the function page itself
* `Upload a .ZIP file`: Use this option if you would like to upload the code in zip format. Provide the zip file location and upload the file.
* `Upload a file from Amazon S3`: Use this option if you have the code in S3 bucket. Provide the bucket URL in the configuration.

We will use the `Edit code inline` option for this tutorial. Edit the code as per the requirement.

![AWS Lambda Function Edit](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_edit.png?raw=true)	

##### Runtime - Provide/Edit the programming language for the code that you are planning to provide for Lambda. For now keep it as Python 3.6.

WHY HEADING HERE

##### Handler - This is the function name in your code which will be calles by AWS Lambda to start the execution. Leave it as lambda_function.lambda_handler

WHY HEADING HERE

#### Step 6 - Click on Save button to save the configuration of the function. The function is ready to be used

![AWS Lambda Function Save](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_save.png?raw=true)	


## Steps to test Python function created using AWS Lambda

Click on the `Test` button to test the function created. The function will provide the result of the execution and summary of the resources being used.

![AWS Lambda Function Test](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_test.png?raw=true)	

## Steps to delete Python function created using AWS Lambda

Click on the  `Actions->Delete` function button to delete the AWS Lambda function if not required.

![AWS Lambda Function Delete](https://github.com/cloudmesh-community/hid-sp18-511/blob/master/tutorial/images/aws_lambda_function_delete.png?raw=true)	
