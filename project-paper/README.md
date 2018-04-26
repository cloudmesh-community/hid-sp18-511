# Automated Spark Cluster Deployment on AWS EC2

hid-sp18-511

## Prerequisites 

### Make sure you have AWS account created. Download the AWS access key and secret access key after account is created.

### Setup the AWS access key and secret access key on Unix console
	export AWS_ACCESS_KEY_ID='<Access Key>'
	export AWS_SECRET_ACCESS_KEY='<Secret Access Key>'

Validate AWS access key and secret access key by typing echo command and check he displayed value
	echo $AWS_ACCESS_KEY_ID
	echo $AWS_SECRET_ACCESS_KEY

### Make sure Ansible is installed on Unix machine where deployment automation script will be executed. Validate Ansible installation by typing the following command on Unix console
	$ ansible-playbook --version
	
Download Ansible from ![Download Ansible](https://www.ansible.com/resources/get-started) is not installed already.

### Clone the source code from Github 
	export HID.git=hid-sp18-511 
	mkdir -p ~/github/cloudmesh-community
	cd ~/github/cloudmesh-community 
	git clone https://github.com/cloudmesh-community/$HID.git//project-code

You will not need to pull the hid-sample directory on a weekly
schedule with

    git pull

to see new additions and improvements, as expected from any open
source project.  Now clone your own repository either with ssh or
https. SSH naturally requires you to have uploaded your public key to
github. Let us use for now https.

Let us assume your hid is hid-sp18-999. You need to clone your own
repo as follows

    cd ~/github/cloudmesh-community
    git clone https://github.com/cloudmesh-community/hid-sp18-999.git
    cp -r hid-sample/technology hid-sp18-999
    
Warning: Please make sure there is no / after the technology directory
name.
  
Next you need to go into that directory and correct them with your
information. Make sure to not checkin the sample files from
hid-sample, but modify them. If we find sample files from hid-sample
in your github repository we will deduct points.

After you have modified your files you want to make a test compile with

    cd ~/github/cloudmesh-community/hid-sp18-999/technology
    make
    
You will see that in dest a pdf file is created that you can look at

You will need in all five abstracts in the technology folder.   Each file name should have the following format:

    abstract-<technology>.tex

as well as the bibliography file

    hid-sp18-999.bib

Make sure all references are changed to include your hid prefix as a
label. For more information see the text in abstract-xms.tex

Before you commit, delete the following files that are should be in your directory:

    hid-sample.bib
    abstract-xms.tex



