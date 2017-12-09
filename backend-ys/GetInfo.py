#! /usr/bin/python3

from GetAuth import *
from TimeProc import *
import requests
import json


infohost = 'weixin.ncuos.com';

def GetWeek(username = '', token = ''): # get week schedule
    dest = '/schedule/api/schedule';
    url = 'http://' + infohost + dest;
    headers = GenHeader(token = token);
    data = (json.dumps({'studentId': username})).encode('utf-8');
    week = requests.post(url = url, headers = headers, data = data);
    if(week.json()['data']):
        print('Have such student.');
    else:
        print('No such student!!');
    return week.json();

def GetClassInfo(username = '', password = '', coursename = ''): # get specific info about a class
    dest = '/schedule/api/schedule/exam';
    url = 'http://' + infohost + dest;
    headers = GenHeader(username, password);
    print('headers:', headers);
    data = json.dumps({'courseName': coursename}).encode('utf-8');
    print('searched course is:', data.decode('utf-8'));
    info = requests.post(url = url, headers = headers, data = data);
    return info.json();

def GetProfile(username = '', token = ''):
    dest = '/api/user/profile/basic';
    url = 'http://' + loginhost + dest;
    headers = GenHeader(token = token);
    print('headers:', headers);
    profile = requests.get(url = url, headers = headers);
    print(profile.text);
    return profile.json();

def GetGender(username = '', token = ''):
    return {'gender': GetProfile(username, token)['base_info']['xb']['mc']};

def GetCurrentClass(username = '', token = ''):
    schedule = GetWeek(username, token);
    week = schedule['currentWeek'];
    schedule = schedule['data']['lessons'];
    t = ClassTime();
    for course in schedule:
        course['week'] = course['week'].split('-');
        print(course['week']);
        if not (week >= int(course['week'][0]) and week <= int(course['week'][1])):
            print(0);
            continue;
        elif IsClassOn(course['time'], t):
            print(1);
            return {'courseName': course['name']};
    return [];
