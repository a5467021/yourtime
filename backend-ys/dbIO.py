#! /usr/bin/python3

import pymysql


def get_conn():
    host="65.49.212.163"
    port=3306
    db="focus"
    user="root"
    password="123"
    conn=pymysql.connect(host=host,
                         user=user,
                         passwd=password,
                         db=db,
                         port=port,
                         charset="utf8",)
    return conn

class User(object):

    def __init__(self,username,userid,avatar,gender,start_time,this_study,last_sudy,study_time,total_time,achievement):
        self.username=username
        self.userid=userid
        self.avatar=avatar
        self.gender=gender
        self.start_time=start_time
        self.this_study=this_study
        self.last_study=last_sudy
        self.study_time=study_time
        self.total_time=total_time
        self.achievement=achievement

    def savelogin(self):
        conn=get_conn()
        cursor=conn.cursor()
        sql="insert into user (username,userid) VALUES (%s,%s)"
        cursor.execute(sql,(self.username,self.userid))
        conn.commit()
        cursor.close()
        conn.close()

    def saveag(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "UPDATE 'test'.'user' SET (avatar,gender)=(%s,%s) WHERE 'userid'=" + id
        cursor.execute(sql, (self.avatar, self.gender))
        conn.commit()
        cursor.close()
        conn.close()

    def savest(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set start_time = %s where userid=" + id
        cursor.execute(sql, (self.start_time))
        conn.commit()
        cursor.close()
        conn.close()

    def savethistime(self):
        conn=get_conn()
        cursor=conn.cursor()
        sql="update user set this_study = %s where userid=" + id
        cursor.execute(sql,(self.this_study))
        conn.commit()
        cursor.close()
        conn.close()

    def savelasttime(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set last_study = %s where userid = " + id
        cursor.execute(sql, (self.this_study))
        conn.commit()
        cursor.close()

    def savestudytime(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set study_time = %s where userid = %s "
        cursor.execute(sql, (self.study_time,self.userid))
        conn.commit()
        cursor.close()

    def savetotaltime(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set total_time = %s where userid =%s "
        cursor.execute(sql, (self.total_time,self.id))
        conn.commit()
        cursor.close()

    def saveachievement(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set achievement = %s where userid =%s"
        cursor.execute(sql, (self.achievement,self.userid))
        conn.commit()
        cursor.close()

    def cleanthisstudy(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set last_study = 0 where userid =%s "
        cursor.execute(sql,(self.userid))
        conn.commit()
        cursor.close()

    def query_all(self):
        conn=get_conn()
        cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql="select * from user"
        cursor.execute(sql)
        rows=cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_starttime(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select start_time from user where userid=%s"
        cursor.execute(sql,(self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_thisstudy(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "SELECT this_study FROM user WHERE userid=%s"
        cursor.execute(sql,(self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def paiming100(self):
        conn = get_conn()
        cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql="select username,achievement from user order by achievement desc limit 100 "
        cursor.execute(sql)
        rows=cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.cursor()

