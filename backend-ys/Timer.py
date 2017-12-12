#! /usr/bin/python3

from ProjectLib import *
from dbIO import *

def TimerStart(username = '', token = ''):
    print('In \'TimerStart(username, token):\'');
    user = User(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
    user.userid = username;
    status = GetCurrentClass(username, token);
    if not status['status']:
        return {'status': 0, 'message': 'Class not on now'};
    else:
        this_start = user.query_thisstart(user);
        # this_start = User.read(this_start)
        this_start = -1;
        # read end
        if this_start == -1:
            this_class_start = class_begin[int(status['time'][1:3])];
            # User.write(this_class_start)
            print('Write into MySQL this_class_start is', this_class_start);
            # write end
            this_class_end = class_end[int(status['time']) % 100];
            # User.write(this_class_end)
            print(status['time'], 'Write into MySQL this_class_end is', this_class_end);
            # write end
        this_start = GetRelTime()[0];
        # User.write(this_start)
        print('Write into MySQL this_start is', this_start);
        # write end
        return {'status': 1, 'message': 'Started successfully'};

def TimerStop(username = '', token = ''):
    print('In \'TimerStop(username, token):\'');
    # User.userid = username
    print('set userid as', username);
    # set end
    now = GetRelTime()[0];
    # this_class_end = User.read(this_class_end)
    this_class_end = 16 * 3600 + 10 * 60; # 3 pm
    print('Read from MySQL class_end is', this_class_end);
    # read end
    # this_start = User.read(this_start)
    this_start = 5 * 3600; # 5 am
    print('Read from MySQL this_start is', this_start);
    # read end
    if this_class_end > now:
        t = now - this_start;
        # User.add(this_study, t);
        print('In MySQL this_study add', t);
        # add end
        return {'status': 1, 'message': 'Stopped successfully'};
    else:
        t = this_class_end - this_start;
        # User.add(this_study, t);
        print('In MySQL this_study add', t);
        # add end
        Submit(username);
        return {'status': 1, 'message': 'Submitted successfully'};
    return {'status': 0, 'message': 'Unknown error'};

def Submit(username = ''):
    # User.userid = username
    print('set userid as', username);
    # set end
    # class_end = User.read(class_end)
    class_end = 15 * 3600;
    print('Read from MySQL class_end is', class_end);
    # read end
    # class_start = User.read(class_start)
    class_start = 8 * 3600;
    print('Read from MySQL class_start is', class_start);
    #read end
    this_total = class_end - class_start;
    # User.add(total_time, this_total)
    print('In MySQL total_time add', this_total);
    # add end
    # User.add(total_study, this_study)
    this_study = 233;
    print('In MySQL total_study add', this_study);
    # add end
    # total_time = User.read(total_time)
    total_time = 2333;
    print('Read from MySQL total_time is', total_time);
    # read end
    # total_study = User.read(total_study)
    total_study = 233;
    print('Read from MySQL total_study is', total_study);
    # read end
    percentage = float(total_study) / total_time;
    # User.write(percentage)
    print('Write into MySQL percentage is', percentage);
    #write end
    return {'status': 1};

if __name__ == '__main__':
    TimerStart();
