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

@app.route('/login', methods = ['POST']) # provides authorization info
def login():
    #form = json.loads(request.data);
    #res = GetAuth(form['username'], form['password']);
    res = GetAuth(request.form.get('username'), request.form.get('password'));
    return pack(json.dumps(res));

@app.route('/login', methods = ['GET'])
def test_login():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">SLog In</button></p>
              </form>
           ''';

@app.route('/profile', methods = ['POST']) # provides student profile
def profile_post():
    token = request.form.get('token');
    username = request.form.get('username');
    info = GetGender(username, token);
    return pack(json.dumps(info));
    

@app.route('/profile', methods = ['GET'])
def profile_get():
    return '''<form action="/profile" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <p><button type="submit">Logr In</button></p>
              </form>
           ''';

@app.route('/schedule', methods = ['POST'])
def schedule_post():
    token = request.form.get('token');
    username = request.form.get('username');
    info = GetWeek(username, token);
    return pack(json.dumps(info));
    
@app.route('/schedule', methods = ['GET'])
def schedule_get():
    return '''<form action="/schedule" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <p><button type="submit">Logr In</button></p>
              </form>
           ''';

@app.route('/current', methods = ['POST'])
def current_post():
    token = request.form.get('token');
    username = request.form.get('username');
    info = GetCurrentClass(username, token);
    return pack(json.dumps(info));
    
@app.route('/current', methods = ['GET'])
def current_get():
    return '''<form action="/current" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <p><button type="submit">Logc In</button></p>
              </form>
           ''';


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3000);

#schedule url: weixin.ncuos.com/schedule/api/schedule
