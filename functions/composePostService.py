import sys
sys.path.append("../../")

from cloudburst.client.client import CloudburstConnection

def ComposePostService(self, req_id, post_type, carrier):
	return req_id, post_type, carrier

cloudburst_client = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
cloud_composePostService = cloudburst_client.register(ComposePostService, 'ComposePostService')


if cloud_composePostService:
	print('Successfully registered cloud_composePostService')
else:
	sys.exit(1)