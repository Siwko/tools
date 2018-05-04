#!/usr/bin/python
"""
Performs nslookup on a set of given adresses. 
Source from nslookup_targets.txt
@TODO 
implement param'd source file 
"""

import requests
import re
from time import sleep as sleep
import os

cmd = 'nslookup'

targets = []

reg = re.compile('^\w+\.\w+\.\w+(\.\w+){,1}$')

with open('nslookup_targets.txt') as targetfile:
	for line in targetfile:
		if reg.match(line.strip()):
			targets.append(line.strip())
		else:
			print('ignore %s ' % line.strip())

for ip in targets:
	print " ***** Going with {} ***** \n".format(ip)
	print('%s %s' % (cmd, ip))
	cmd_res = os.system('%s %s' % (cmd, ip) )
	print(cmd_res)
	sleep(3)
	
	

