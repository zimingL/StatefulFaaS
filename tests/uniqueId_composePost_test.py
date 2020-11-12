import sys
sys.path.append("../../")

from cloudburst.client.client import CloudburstConnection

cloudburst_client = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
dag_name = 'uniqueId_composePost'
arg_map = {"UniqueIdService": [1, 'type', 'msg']}
dag_result = cloudburst_client.call_dag(dag_name, arg_map)

print (dag_result.get())


