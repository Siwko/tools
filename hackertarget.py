#!/usr/bin/python

import requests
import re
from time import sleep as sleep

hackertarget = 'http://api.hackertarget.com/'
action = 'whois/?q='

targets = []

reg = re.compile('^\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{2,3}$')

with open('targets.txt') as targetfile:
	for line in targetfile:
		if reg.match(line.strip()):
			targets.append(line.strip())

for ip in targets:
	print " ***** Going with {} ***** \n".format(ip)
	req = requests.get(hackertarget+action+ip)
	if req.status_code == 200:
		print(req.text)
		sleep(3)
	
	

