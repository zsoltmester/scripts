#!/usr/bin/python

##
# Send a push message via the Google Cloud Messaging.
#
# Dependencies:
#	- python-gcm. Install it with pip: pip install python-gcm.
#
# Params:
#	1.: GCM API key.
#	2.: Target device registration id.
#	3. - : The message's key-value pairs, separated with ':'.
#
# Examples: 
#	$ send-push.py api_key reg_id title:mytitle detail:mydetail
##

# process args
import sys
api_key = sys.argv[1]
reg_id = sys.argv[2]
data = {}
try:
	argi = 3
	while True:
		splittedArg = sys.argv[argi].split(':')
		data[splittedArg[0]] = splittedArg[1]
		argi += 1
except IndexError:
	print 'Args processed. The message:'
	import pprint
	pprint.pprint(data, width=1)	
	
# send the request
from gcm import GCM
gcm = GCM(api_key)
response = gcm.json_request(registration_ids=[reg_id], data=data, priority='high')

# print successfully handled registration_ids
if response and 'success' in response:
	for reg_id, success_id in response['success'].items():
		print 'Successfully sent notification for reg_id {0}'.format(reg_id)
else:
	print 'Failed to send any notification'
