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
		
## Deploy Apache Spark Cluster on AWS EC2

  * Deployment
 	
	Execute the following command
	
	```
	cd ~/github/cloudmesh-community/$HID/project-code
	ansible-playbook site.yml --tags "provision"
	```

	Deployment will perform following tasks
	
	* Create Security Group in AWS
	* Create Key Pair in AWS
	* Provision EC2 instance for Spark master
	* Provision EC2 instance for Spark worker
	* Create Spark user and group on Spark master
	* Setup Spark specific directories on Spark master
	* Download and unarchive Spark on Spark master
	* Download and install Java on Spark master
	* Setup Spark configuration files on Spark master
	* Start Spark master service on Spark master
	* Create Spark user and group on Spark worker
	* Setup Spark specific directories on Spark worker
	* Download and unarchive Spark  on Spark worker
	* Download and install Java  on Spark worker
	* Setup Spark configuration files on Spark worker
	* Spark worker service and add to Spark master

  * Add Apache Spark worker into cluster	
  
	* Open hosts file and find out the IP address in [sparkmaster] and [sparkworker] section.
	
	  ```
	  cd ~/github/cloudmesh-community/$HID/project-code/inventory
	  cat hosts
	  ```

	* Connect to the Spark worker node using ssh
	  `ssh -i ec2_spark_stg_key-private.pem ubuntu@[Spark worker IP address]`

	* Execute the following command on Spark worker machine 
      `sudo start-slave.sh spark://[Spark master IP address]`
	
  * Deployment Validation	
	
	Login to AWS console and validate following services/components have been created
	
	* Security group 
	* Key pair 
    * One AWS EC2 instance for Spark master
    * One AWS EC2 instance for Spark worker
	
	Validate Spark Apache cluster up and running by typing the below url in browser
	`http://[EC2 master IP address]:8080`
	




