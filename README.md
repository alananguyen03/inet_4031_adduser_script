# INET 4031 Automating User Management 

## Program Description
This program uses Python to automate the creation of user accounts on an Ubuntu system. Automating these commands will help the user save time and reduce the chances of mistakes. Normally to add a user, the following commands would need to be used: 'sudo adduser <username>,' 'sudo passwd <username>,' and 'sudo adduser <username> <group>.' The code reads a file containing user information and executes comamnds to create users and assign group assignments, which is equivalent to running the above commands. 

## Input File Format
The program reads from the file 'create-users.input'. Each line in the file contains the following fields: username, password, last name, first name, and groups. Each field is seperated by colons ':' and the program will skip the line if it doesn't contain 5 fields or if it is a comment. If the user does not want to a new user to be added to any groups, they will need to keep the following lines commented out in the code: 'print(cmd)' and 'os.system(cmd).'

-username: the user's login name
-password: the user's password
-last_name: user's last name
-first_name: user's first name
-groups: comma-separated list of groups or '-' if none

## Command Execution
   1. Run 'chmod +x create-users.py'
   2. Run 'sudo ./create-users.py < create-users.input'

## "Dry Run"

To do a dry run, the following lines will need to be commented out in the code: 'print(cmd)' and 'os.system(cmd).' During a dry run, all system commands are printed but not executed. This allows the user to verifiy the commands and make necessary changes without modifying the system.
