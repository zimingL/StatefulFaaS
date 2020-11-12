import sys
sys.path.append('../../')

from cloudburst.client.client import CloudburstConnection
from StatefulFaaS.functions.function import square, inc

cloudburst_client = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)

''' REGISTER DAG'''
dag_name = 'composition'
functions = ['square', 'inc']
connections = [('inc', 'square')]
cloudburst_client.register_dag(dag_name, functions, connections)

'''TEST DAG'''

arg_map = {"inc": [2]}
dag_result = cloudburst_client.call_dag(dag_name, arg_map)

if dag_result.get() != 9:
	print('Unexpected result from composition(2): %s' % (str(dag_result)))
	sys.exit(1)

print ('dag_test_successed')

