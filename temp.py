#!/usr/bin/python3

##
# This script measure the current temperature of the device and append it to the end of a file. 
# The only param is a path to a file. It will be created if it's not exist.
# vcgencmd must be installed.
##

# process arguments
import sys
filename = sys.argv[1]

# measure temperature
import subprocess
temp = subprocess.Popen('sudo vcgencmd measure_temp', shell=True, stdout=subprocess.PIPE).stdout.read()

# print the temp
import datetime
f = open(filename, 'a')
f.write('[')
f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
f.write('] ')
f.write(temp[5:].decode('utf-8'))
f.close()
