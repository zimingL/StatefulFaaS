import sys
sys.path.append('../../')

from flask import Flask
from cloudburst.client.client import CloudburstConnection
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

@app.route('/')
def hello_world():
	return "Hello, World!" 

@app.route('/test')
def test():
	cloudburst_client = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
	dag_name = 'composition'
	arg_map = {"inc": [2]}
	dag_result = cloudburst_client.call_dag(dag_name, arg_map)
	if dag_result.get() != 9:
		print('Unexpected result from composition(2): %s' % (str(dag_result)))
		sys.exit(1)
	return ('dag_test_successed')


if __name__ == '__main__':
	app.run(debug = True, host='127.0.0.1', port=5001)

