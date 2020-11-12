import sys
sys.path.append("../../")

from cloudburst.client.client import CloudburstConnection

cloudburst_client = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
cloud_uniqueIdService = cloudburst_client.get_function('UniqueIdService')
uniqueIdService_test = cloud_uniqueIdService(1, 'type', 'msg').get()

print (uniqueIdService_test)

#if inc_test != 11:
#	print('Unexpected result from incr(2): %s' % (str(incr_test)))
#	sys.exit(1)
