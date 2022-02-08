#!/usr/bin/env python3

import os
import uuid
import sys
import json

def create_session():
    sessionid = uuid.uuid4().hex
    with open('/tmp/session/' + sessionid, 'wb'):
        pass
    print('Set-Cookie: sessionid=' + sessionid, end='\n')
    
def login():
    data = json.loads(sys.stdin.read())
    if 'username' not in data or 'password' not in data:
        print('Status: 400 Bad Request', end='\n\n')
        return
    with open('/users', 'r') as f:
        for line in f:
            tokens = line.strip().split('\t')
            if len(tokens) == 0:
                break
            if data['username'] == tokens[0] and data['password'] == tokens[1]:
                create_session()
                print('Status: 200 OK', end='\n\n')
                return
    print('Status: 401 Unauthorized', end='\n\n')

def check_session():
    cookies = os.environ.get('HTTP_COOKIE').strip().split(';')
    for cookie in cookies:
        tokens = cookie.strip().split('=')
        if len(tokens) != 2:
            continue
        if tokens[0] == 'sessionid':
            try:
                uuid.UUID(tokens[1], version=4)
                return True
            except:
                return False
    return False

def valid_url(url):
    for c in url:
        if ord(c) > ord('~') or ord(c) < ord(' '):
            return False
        if c in '~`$^*()\\|[]}{;\'"<>=#':
            return False
    return True

def curl():
    if not check_session():
        print('Status: 401 Unauthorized', end='\n\n')
        return
    data = json.loads(sys.stdin.read())
    if 'url' not in data or not valid_url(data['url']):
        print('Status: 400 Bad Request', end='\n\n')
        return
    print('Status: 200 OK', end='\n\n')
    print(os.system('curl ' + data['url']))

def handle_post():
    route = os.environ.get('QUERY_STRING')
    if route == 'login':
        login()
    elif route == 'curl':
        curl()
    else:
        print('Status: 404 Not Found', end='\n\n')

if __name__ == '__main__':
    method = os.environ.get('REQUEST_METHOD')
    if method == 'POST':
        handle_post()
    else:
        print('Status: 405 Method Not Allowed', end='\n\n')
