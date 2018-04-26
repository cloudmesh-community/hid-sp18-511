# Automated Apache Spark Cluster deployment on AWS EC2 using Ansible

hid-sp18-511

This project is a about Automated Apache Spark cluster deployment on AWS EC2 using Ansible deployment and configuration tool.

This project provide following functionalities to the user 

  * Automated Apache Spark cluster deployment on EC2 instances on a single click
  * User can perform various data processing tasks on Apache Spark cluster after the deployment and configuration
  * Automated decommission of Apache Spark cluster on a single click once data processing task completed
  
Please make sure following prerequisites are fulfilled before running the project.

## Prerequisites 

  * Make sure you have AWS account created. Create AWS account is not already created.
	Download the AWS access key and secret access key from AWS console. Please note don't share the keys with anyone.
	Setup the AWS access key and secret access key on Unix console
	      
    ```
	export AWS_ACCESS_KEY_ID='<Access Key>'
	export AWS_SECRET_ACCESS_KEY='<Secret Access Key>'
	```
	
	Validate AWS access key and secret access key have been setup correctly by typing echo command on Unix console and check the displayed value. Make sure the displayed values as same as specified during configuration.
	
	```	
	echo $AWS_ACCESS_KEY_ID
    echo $AWS_SECRET_ACCESS_KEY
	```

  * Make sure Ansible is installed on Unix machine where Ansible automation script will be executed. Validate Ansible installation by typing the following command on Unix console
	
	`$ ansible-playbook --version`
	
	Above command should return the version of Ansible installed on the machine. Download Ansible from the [download link](https://www.ansible.com/resources/get-started) if not installed. 
	
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
		
	* AWS EC2 instance related configuration options
		
	  `cd ~/github/cloudmesh-community/$HID.git/project-code/roles/provisionec2/defaults`

	* Apache Spark master related configuration options
		
	  `cd ~/github/cloudmesh-community/$HID.git/project-code/roles/sparkmaster/defaults`

	* Apache Spark worker related configuration options
		
	  `cd ~/github/cloudmesh-community/$HID.git/project-code/roles/sparkworker/defaults`
		
## References

* <https://aws.amazon.com/>
* <https://aws.amazon.com/ec2/>
* <https://www.ansible.com/>
