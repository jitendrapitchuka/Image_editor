# Steps to run the project

### First one need to install pip.

### STEP-1:- The command to install pip is 
    sudo apt install python3-pip


### STEP-2:- After installation of pip ,need to install virtualenvironment from pip.Command for installation of virtualenvironemt from pip is 
    pip install virtualenv


### STEP-3:- Next need to create a virtual environment and naming it.Here in my case the name for virtualenvironemt is myenv     
    python3 -m virtualenv myenv


### STEP-4:- Activate the virtualenvironment with this command   
    source my_env/bin/activate


### STEP-5:- After activating the virtualenvironemt paste this(pip install -r requirements.txt ) command.It will install all  libraries and framework from  requirements.txt  file to activated vrtual environment  
    pip install -r requirements.txt 


### STEP-6:- After completion of installations run the server
    python3 manage.py runserver


### STEP-7:- http://127.0.0.1:8000/       paste this in the browser to see the output.
