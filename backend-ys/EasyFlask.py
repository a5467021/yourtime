#! /usr/bin/python3

from flask import Flask, Response, make_response
from flask import request
from ProjectLib import *

def pack(data = ''): # solves the access-control problem
    res = make_response(data);
    res.mimetype = 'application/json';
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
    return res;

app = Flask(__name__);

@app.route('/login', methods = ['POST', 'GET']) # provides authorization info
def login():
    if(request.method == 'GET'):
        return 'This is login page.<br />Please use POST method...';
    form = json.loads(request.data);
    res = GetAuth(form['username'], form['password']);
    return pack(res);

@app.route('/profile', methods = ['POST', 'GET']) # provides student profile
def profile():
    if(request.method == 'GET'):
        return 'This is login page.<br />Please login before using this page...';

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3000);

#schedule url: weixin.ncuos.com/schedule/api/schedule
