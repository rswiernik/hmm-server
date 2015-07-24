#!/usr/bin/python

import flask

app = Flask(__name__)

@app.route('/get_host_information/<host>', methods=['GET'])
def get_hosts(host):
        # Get info for the host
        return host_info

@app.route('/get_attr_hosts/<attr>', methods=['GET'])
def get_hosts(attr):
        # Get hosts for a certain attr
        return attr_hosts

@app.route('/get_acl_allow/<host>', methods=['GET'])
def get_hosts(host):
        # Get the whitelisted users who can make changes to this hmm host
        return permitted_users


