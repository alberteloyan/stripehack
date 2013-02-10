import subprocess
import logging
from subprocess import PIPE, STDOUT
import re

#depending on installation type

def install_system(system_type, command_list, log_file, app_name):

	#installing git
	git_commands = ['git init --bare /opt/git/app.git','cp post-receive /opt/git/app.git/hooks', 'mkdir /var/www', 'cd /var/www && git clone /opt/git/app.git']
	execute_commands(git_commands)

	#installing system-specific stack
	execute_commands(command_list)
	print 'System successfully installed. Log file in same directory.'

def execute_commands(command_list):
	for command in command_list:
		print 'Executing:' + command
		system_execute = subprocess.Popen(command, stdin =PIPE, stderr=STDOUT, stdout=PIPE, shell=True)
		system_response = ""
		while True:
			line = system_execute.stdout.readline()
			if line != '':
				print line
				system_response += line + "\n"
			else:
				break

		log_file.write(system_response)
		#log_file.write(system_message)
		log_file.write('\n')

#===============================================================================

#list of commands to set up lamp stack
lamp_commands = [
'sudo apt-get install mysql-client-core-5.5',
'sudo /sbin/chkconfig mysql on',
'service mysqld start',
'sudo apt-get install php5',
'install php-xml php-pdo php-odbc php-soap php-common php-cli php-mbstring php-bcmath php-ldap php-imap php-gd',
'sudo apt-get install nginx'
'service nginx start']

static_commands = [
'yes | sudo apt-get install nginx',
'sudo rm /etc/nginx/sites-enabled/*',
'cp choku_nginx /etc/nginx/sites-enabled',
'service nginx start']

log_file = open('log.txt', 'w+')

system_type = raw_input('What type of system will you be using? \n')
app_name = raw_input('What is your app going to be called? \n')

rails = re.match('(^R)', system_type, flags = re.IGNORECASE)
lamps = re.match('(^L)', system_type, flags = re.IGNORECASE)
django = re.match('(^D)', system_type, flags = re.IGNORECASE)
static = re.match('(^S)', system_type, flags = re.IGNORECASE)


if (rails is not None):
  system_type = 'rails'
elif (lamps is not None):
	system_type = 'lamp'
	#launch lamp subroutine
	install_system(system_type, lamp_commands, log_file, app_name)
elif (django is not None):
	system_type = 'django'
elif (static is not None):
	system_type = 'static'
	install_system(system_type, static_commands, log_file, app_name)

else:
	print('System not available in directory')

log_file.write('Log file for '+app_name+':\n')

log_file.close()