#!/usr/bin/python
import os
import sys
import time
import logging
import flask

app = Flask(__name__)

@app.route('/node/<node>', methods=['GET'])
def get_node_info(node):
        # returns the node info in the form of a json object
		# {
		#     "node": "name",
		#     "tags": ["tag"],
		#     "attributes": {
		#     "attr": "value"
		#     {
		# }
        return node_info

@app.route('/attr/<attr>', methods=['GET'])
def get_nodes(attr):
        # Get nodes for a certain attr
        return attr_nodes

@app.route('/tag/<tag>', methods=['GET'])
def get_nodes(attr):
        # Get nodes for a certain attr
        return attr_nodes

@app.route('/acls/allow/<node>', methods=['GET'])
def get_nodes(node):
        # Get the whitelisted users who can make changes to this hmm node
        return permitted_users

def main(args):
    LOG_FORMAT = '%(asctime)-15s %(message)s'
    LOG_DATE = '%m/%d/%Y %H:%M:%S %Z  '
    LOG_LVL = logging.INFO
    if args.verbose:
        LOG_LVL = logging.DEBUG
    logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE, level=LOG_LVL)
    logging.debug('Verbose output enabled')

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', '--verbose', help='enable verbose output',
                        action='store_true')
    parser.add_argument('-p', '--port', action='store', dest='port', type=int, default=5606, help='serving port, default is 5606')
    args = parser.parse_args()


    logging.debug("Starting HMMd - %s, %s" % (HOSTNAME, args.port))
    app.run(port=port,host=hostname)
    logging.debug("Stopping HMMd - %s, %s" % (HOSTNAME, args.port))


if __name__ == '__main__':
	sys.exit(main(sys.argv))
