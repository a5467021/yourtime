#! /usr/bin/python3

import time

def IsClass(username = '', token = ''):
    day = time.localtime(time.time())[6];
    print(day)


if __name__ == '__main__':
    IsClass();
