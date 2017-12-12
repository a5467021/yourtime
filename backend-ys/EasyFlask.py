#! /usr/bin/python3

from flask import Flask, make_response
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
    if request.form.get('type') == 'test':
        res = GetAuth(request.form.get('username'), request.form.get('password'));
    else:
        form = json.loads(request.data);
        res = GetAuth(form['username'], form['password']);
    # User.userid = form['username']
    # 查询userid，如果有记录的话直接返回，否则创建条目后返回
    return pack(json.dumps(res));

@app.route('/login', methods = ['GET'])
def test_login():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">SLog In</button></p>
              </form>
           ''';

@app.route('/profile', methods = ['POST']) # provides student profile
def profile_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('username');
        info = GetProfile(username, token);
    else:
        info = json.loads(request.data);
        info = GetProfile(info['username'], info['token']);
    return pack(json.dumps(info));
    

@app.route('/profile', methods = ['GET'])
def profile_get():
    return '''<form action="/profile" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logr In</button></p>
              </form>
           ''';

@app.route('/schedule', methods = ['POST'])
def schedule_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('username');
        info = GetWeek(username, token);
    else:
        info = json.loads(request.data);
        info = GetWeek(info['username'], info['token']);
    return pack(json.dumps(info));
    
@app.route('/schedule', methods = ['GET'])
def schedule_get():
    return '''<form action="/schedule" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logr In</button></p>
              </form>
           ''';

@app.route('/current', methods = ['POST'])
def current_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('username');
        info = GetCurrentClass(username, token);
    else:
        info = json.loads(request.data);
        info = GetCurrentClass(info['username'], info['token']);
    return pack(json.dumps(info));
    
@app.route('/current', methods = ['GET'])
def current_get():
    return '''<form action="/current" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logc In</button></p>
              </form>
           ''';

@app.route('/start', methods = ['POST'])
def start_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('username');
        info = TimerStart(username, token);
    else:
        info = json.loads(request.data);
        info = TimerStart(info['username'], info['token']);
    return pack(json.dumps(info));
    
@app.route('/start', methods = ['GET'])
def start_get():
    return '''<form action="/start" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logc In</button></p>
              </form>
           ''';

@app.route('/stop', methods = ['POST'])
def stop_post():
    if request.form.get('type') == 'test':
        token = request.form.get('token');
        username = request.form.get('username');
        info = TimerStop(username, token);
    else:
        info = json.loads(request.data);
        info = TimerStop(info['username'], info['token']);
    return pack(json.dumps(info));
    
@app.route('/stop', methods = ['GET'])
def stop_get():
    return '''<form action="/stop" method="post">
              <p><input name="username"></p>
              <p><input name="token"></p>
              <input type="hidden" name="type" value="test" />
              <p><button type="submit">Logc In</button></p>
              </form>
           ''';

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3000);
