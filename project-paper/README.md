# Automated Spark Cluster Deployment on AWS EC2 using Ansible

hid-sp18-511

## Prerequisites 

  * Make sure you have AWS account created. Download the AWS access key and secret access key after account is created.
	Setup the AWS access key and secret access key on Unix console
	      
    ```
	export AWS_ACCESS_KEY_ID='<Access Key>'
	export AWS_SECRET_ACCESS_KEY='<Secret Access Key>'
	```
	
	Validate AWS access key and secret access key have been setup correctly by typing echo command and check he displayed value
	
	```	
	echo $AWS_ACCESS_KEY_ID
    echo $AWS_SECRET_ACCESS_KEY
	```

  * Make sure Ansible is installed on Unix machine where deployment automation script will be executed. Validate Ansible installation by typing the following command on Unix console
	
	`$ ansible-playbook --version`
	
	Download Ansible from the [download link](https://www.ansible.com/resources/get-started) if not installed already 
	
  * Clone the source code from Github 
	
	```
	export HID.git=hid-sp18-511
	mkdir -p ~/github/cloudmesh-community
	cd ~/github/cloudmesh-community
	git clone https://github.com/cloudmesh-community/$HID.git/project-code	
	``` 
	
	* Update configuration as per the requirement
		* AWS related configuration options
		
			`cd ~/github/cloudmesh-community/$HID.git/project-code/group_vars/all`
		
		* EC2 related configuration options
		
			`cd ~/github/cloudmesh-community/$HID.git/project-code/roles/provisionec2/defaults`

		* Apache Spark master related configuration options
		
			`cd ~/github/cloudmesh-community/$HID.git/project-code/roles/sparkmaster/defaults`

		* Apache Spark worker related configuration options
		
			`cd ~/github/cloudmesh-community/$HID.git/project-code/roles/sparkworker/defaults`


