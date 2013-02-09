import re

system_type = input('What type of system would you like to use? ')

rails = re.match('(^R)', system_type, flags = re.IGNORECASE)
lamps = re.match('(^L)', system_type, flags = re.IGNORECASE)
django = re.match('(^D)', system_type, flags = re.IGNORECASE)

if (rails is not None):
  system_type = 'rails'
elif (lamps is not None):
	system_type = 'lamps'
elif (django is not None):
	system_type = 'django'
else:
	print('System not available in directory')
