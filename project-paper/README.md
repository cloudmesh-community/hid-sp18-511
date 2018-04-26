# Automated Spark Cluster Deployment on AWS EC2

hid-sp18-511

## Prerequisites 

  * Make sure you have AWS account created. Download the AWS access key and secret access key after account is created.
	Setup the AWS access key and secret access key on Unix console
    
	`export AWS_ACCESS_KEY_ID='<Access Key>'`
    `export AWS_SECRET_ACCESS_KEY='<Secret Access Key>'`
	
	Validate AWS access key and secret access key by typing echo command and check he displayed value

	`echo $AWS_ACCESS_KEY_ID`
	`echo $AWS_SECRET_ACCESS_KEY`	

  * Make sure Ansible is installed on Unix machine where deployment automation script will be executed. Validate Ansible installation by typing the following command on Unix console
	`$ ansible-playbook --version`
	
	Download Ansible from the following link if not installed already 
	'https://www.ansible.com/resources/get-started'
	
  * Clone the source code from Github 
	'export HID.git=hid-sp18-511'
	'mkdir -p ~/github/cloudmesh-community'
	'cd ~/github/cloudmesh-community'
	'git clone https://github.com/cloudmesh-community/$HID.git//project-code'

  * Open a terminal on your VM and create a directory 
  
    `mkdir -p ~/.cloudmesh/chameleon`


