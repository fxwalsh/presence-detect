#!/usr/bin/env python
#coding=utf-8

import subprocess
from sense_hat import SenseHat
from time import sleep
import wiatest

sense = SenseHat()

#Names of device owners 
names = ["darragh","ronan"]

# MAC addresses of known devices
macs = ["d4:28:d5:37:7e:a2","xx:xx:xx:xx:xx:xx"]

lastScanResult=[False,False]

def arp_scan():
        try:
		output = subprocess.check_output("sudo arp-scan -l", shell=True)
		for i in range(len(names)):
			result = names[i]
			isHome=False
			if macs[i] in output:
				result=result+" is home"
				isHome=True
			else:
				result=result+" is not home"
			print(result)
			sense.show_message(result)
			if isHome!=lastScanResult[i]:
				lastScanResult[i]=isHome
				wiatest.publish_presence(names[i],result)
	except Exception as e:
		print("arp-scan failed")
		print(e)
		sense.show_message("arp-scan failed")
while True:
	arp_scan()
	sleep(10)
