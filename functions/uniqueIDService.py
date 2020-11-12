import sys
sys.path.append("../../")

from cloudburst.client.client import CloudburstConnection

def UniqueIdService(self, req_id, post_type, carrier):
	return req_id, post_type, carrier

cloudburst_client = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
cloud_idService = cloudburst_client.register(UniqueIdService, 'UniqueIdService')


if cloud_idService:
	print('Successfully registered all functions')
else:
	sys.exit(1)