#!/usr/bin/python

import sys
import argparse
import urllib
import requests
import json

def get_arg(args=None):
    parser = argparse.ArgumentParser(description='generate/retrieve token from given service')
    parser.add_argument('-u', '--username',
                        help='Useranme',
                        default='john')
    parser.add_argument('-p', '--password',
                        help='password',
                        default='1234')
    parser.add_argument('--url',
                        help='URL of target API')
       
    results = parser.parse_args(args)
    if len(args) == 0:
        print "At least one argument is needed to procced.\n"
        sys.exit(1)

    return (results.username,
            results.password,
            results.url)

def generateToken(username, password, portalUrl):
    '''Retrieves a token to be used with API requests.'''

    parameters = urllib.urlencode({'username' : username, 'password' : password, 'client' : 'referer','referer': portalUrl,'expiration': 60, 'f' : 'json'})
    response = req = requests.get(portalUrl + '/sharing/rest/generateToken?' + parameters, verify=False)
    print(response)
    response = response.text
    try:
        jsonResponse = json.loads(response)
        if 'token' in jsonResponse:
            return jsonResponse['token']
        elif 'error' in jsonResponse:
            print jsonResponse['error']['message']
            for detail in jsonResponse['error']['details']:
                print detail
    except ValueError, e:
        print 'An unspecified error occurred.'
        print e

if __name__ == '__main__':
    u, p, url = get_arg(sys.argv[1:])
    generateToken(u, p, url)

