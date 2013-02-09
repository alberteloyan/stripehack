import argparse 
import commands
import logging

#depending on installation type 

def install_system(system_type, command_list, log_file):

	if system_type == 'lamp':
		for command in command_list:
			print command
			log_file.write(commands.getstatusoutput(command)[1])
			log_file.write('\n')
	print 'System successfully installed. Log file in same directory.'

#===============================================================================

log_file = open('log.txt', 'w+')

system_type = raw_input('What type of system will you be using? \n')
app_name = raw_input('What is your app going to be called? \n')

log_file.write('Log file for '+app_name+':\n')

lamp_commands = ['pwd','pwd','pwd']
rails_commands = []

if system_type == 'lamp':
	#launch lamp subroutine
	install_system('lamp', lamp_commands, log_file)
else:
	#launch other subroutine
	pass

log_file.close()