#! /usr/bin/python3

import requests
import json


infohost = 'weixin.ncuos.com';

def GetWeek(username = '', password = ''): # get week schedule
    dest = '/schedule/api/schedule';
    url = 'http://' + infohost + dest;
    headers = GenHeader(username, password);
    data = ('{"studentId": "' + username + '"}').encode('utf-8');
    week = requests.post(url = url, headers = headers, data = data);
    if(week.json()['data']):
        print('Have such student.');
        #print(json.dumps(week.json()['data']));
    else:
        print('No such student!!');
    return json.dumps(week.json(), ensure_ascii = False, indent = 4, separators = (',', ': '));

def GetClass(username = '', password = '', coursename = ''): # get specific info about a class
    dest = '/schedule/api/schedule/exam';
    url = 'http://' + infohost + dest;
    headers = GenHeader(username, password);
    print('headers:', headers);
    data = ('{"courseName": "' + coursename + '"}').encode('utf-8');
    print('searched course is:', data.decode('utf-8'));
    info = requests.post(url = url, headers = headers, data = data);
    if(info.json()['data']):
        print('Have such course.');
        #print(json.dumps(info.json()['data']));
    else:
        print('No Such course!!');
    return json.dumps(info.json()['data'], ensure_ascii = False, indent = 4, separators = (',', ': '));

if __name__ == '__main__':
    GetClass();
