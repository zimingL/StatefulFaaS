import sys
sys.path.append('../../')

from cloudburst.client.client import CloudburstConnection
from StatefulFaaS.functions.function import square, inc

cloudburst_client = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
cloud_square = cloudburst_client.register(square, 'square')
cloud_inc = cloudburst_client.register(inc, 'inc')

if cloud_inc and cloud_square:
	print('Successfully registered all functions')
else:
	sys.exit(1)

'''test functions'''
inc_test = cloud_inc(10).get()
square_test = cloud_square(10).get()


if inc_test != 11:
	print('Unexpected result from incr(2): %s' % (str(incr_test)))
	sys.exit(1)

if square_test != 100:
	print('Unexpected result from square(100): %s' % (str(square_test)))
	sys.exit(1)

print ('functions_test_successed')