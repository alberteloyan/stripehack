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

static_commands = [
'yes | sudo apt-get install nginx',
'sudo rm /etc/nginx/sites-enabled/*',
'sudo cp static_nginx /etc/nginx/sites-enabled',
'sudo service nginx start']

log_file = open('log.txt', 'w+')

app_name = raw_input('What is your app going to be called? \n')

system_type = 'static'
install_system(system_type, static_commands, log_file, app_name)

print """System Installed!:
Git URL: username@<server_host>:/opt/git/app.git"""

log_file.write('Log file for '+app_name+':\n')

log_file.close()