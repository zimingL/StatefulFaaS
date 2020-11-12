import sys
sys.path.append('../../')

from cloudburst.client.client import CloudburstConnection

cloudburst_client = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)

''' REGISTER DAG'''
dag_name = 'uniqueId_composePost'
functions = ['UniqueIdService', 'ComposePostService']
connections = [('UniqueIdService', 'ComposePostService')]
cloudburst_client.register_dag(dag_name, functions, connections)


