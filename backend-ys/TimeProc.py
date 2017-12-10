#! /usr/bin/python3

import time


class_begin = {
    1: 7 * 3600 + 50 * 60,
    2: 8 * 3600 + 40 * 60,
    3: 9 * 3600 + 45 * 60,
    4: 10 * 3600 + 35 * 60,
    5: 11 * 3600 + 25 * 60,
    6: 13 * 3600 + 50 * 60,
    7: 14 * 3600 + 40 * 60,
    8: 15 * 3600 + 45 * 60,
    9: 16 * 3600 + 35 * 60,
    10: 17 * 3600 + 25 * 60,
    11: 19 * 3600 + 0 * 60,
    12: 19 * 3600 + 50 * 60,
    13: 20 * 3600 + 40 * 60
    };

class_end = {
    1: 8 * 3600 + 35 * 60,
    2: 9 * 3600 + 25 * 60,
    3: 10 * 3600 + 30 * 60,
    4: 11 * 3600 + 20 * 60,
    5: 12 * 3600 + 10 * 60,
    6: 14 * 3600 + 35 * 60,
    7: 15 * 3600 + 25 * 60,
    8: 16 * 3600 + 30 * 60,
    9: 17 * 3600 + 20 * 60,
    10: 18 * 3600 + 10 * 60,
    11: 19 * 3600 + 45 * 60,
    12: 20 * 3600 + 35 * 60,
    13: 21 * 3600 + 25 * 60
    };

def IsClassOn(t = '', now = []): # t is time string, now contains [currentclass, currentweek]
    day = int(t[0]);
    t = int(t[1:]);
    classes = [];
    while t:
        classes.append(t % 100);
        t = int(t / 100);
    print('now day', now[1], 'class day', day);
    if not now[1] == day:
        return 0;
    if now[0] in classes:
        return 1;
    else:
        return 0;

def ClassTime():
    print('In \'ClassTime():\'');
    t = time.localtime(time.time());
    current = -1;
    day = t[6] + 1;
    t = t[3] * 3600 + t[4] * 60 + t[5];
    for n in range(1, 14):
        if t >= class_begin[n] and t <= class_end[n]:
            current = n;
            break;
    print(current);
    return [current, day];

if __name__ == '__main__':
    ClassTime();
