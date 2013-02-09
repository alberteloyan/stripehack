import argparse 
import subprocess
import logging
from subprocess import PIPE, STDOUT
import re

#depending on installation type 

def install_system(system_type, command_list, log_file):

	if system_type == 'lamp':
		for command in command_list:
			print 'Executing:' + command
			system_execute = subprocess.Popen(command, stdin =PIPE, stderr=STDOUT, stdout=PIPE, shell=True)
			system_response = system_execute.stdout.read()
			print system_response
			log_file.write(system_response)
			#log_file.write(system_message)
			log_file.write('\n')
	print 'System successfully installed. Log file in same directory.'

#===============================================================================

lamp_commands = [
'sudo apt-get install mysql',
'sudo apt-get install mysql-server',
'sudo /sbin/chkconfig mysql on',
'service mysqld start',
'pwd']
rails_commands = []

log_file = open('log.txt', 'w+')

system_type = raw_input('What type of system will you be using? \n')
app_name = raw_input('What is your app going to be called? \n')

rails = re.match('(^R)', system_type, flags = re.IGNORECASE)
lamps = re.match('(^L)', system_type, flags = re.IGNORECASE)
django = re.match('(^D)', system_type, flags = re.IGNORECASE)

if (rails is not None):
  system_type = 'rails'
elif (lamps is not None):
	system_type = 'lamp'
	#launch lamp subroutine
	install_system(system_type, lamp_commands, log_file)
elif (django is not None):
	system_type = 'django'
else:
	print('System not available in directory')

log_file.write('Log file for '+app_name+':\n')

log_file.close()