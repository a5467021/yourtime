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

    def __init__(self,name,userid,school,gender,percentage,avatar,total_time,total_study,this_class_start,this_class_end,this_start,this_study,last_name,last_total,last_study):
        self.name=name
        self.userid=userid
        self.school=school
        self.gender=gender
        self.percentage=percentage
        self.avatar=avatar
        self.total_time=total_time
        self.total_study=total_study
        self.this_class_start=this_class_start
        self.this_class_end=this_class_end
        self.this_start=this_start
        self.this_study=this_study
        self.last_name=last_name
        self.last_total=last_total
        self.last_study=last_study

    def save_name_userid_avatar_gender_school(self):
        conn=get_conn()
        cursor=conn.cursor()
        sql="insert into user (name,userid,avatar,gender,school) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql,(self.name,self.userid,self.avatar,self.gender,self.school))
        conn.commit()
        cursor.close()
        conn.close()


    def save_thisstart(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set this_start = %s where userid=%s"
        cursor.execute(sql, (self.this_start,self.userid))
        conn.commit()
        cursor.close()
        conn.close()

    def save_thisclassstart(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set this_class_start = %s where userid=%s"
        cursor.execute(sql, (self.this_class_start, self.userid))
        conn.commit()
        cursor.close()
        conn.close()

    def save_thisclassend(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set this_class_end = %s where userid=%s"
        cursor.execute(sql, (self.this_class_end, self.userid))
        conn.commit()
        cursor.close()
        conn.close()


    def save_thisstudy(self):
        conn=get_conn()
        cursor=conn.cursor()
        sql="update user set this_study = %s where userid=%s"
        cursor.execute(sql,(self.this_study,self.userid))
        conn.commit()
        cursor.close()
        conn.close()

    def save_lastname(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set last_name = %s where userid = %s"
        cursor.execute(sql, (self.last_name,self.userid))
        conn.commit()
        cursor.close()

    def save_lasttotal(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set last_total = %s where userid = %s "
        cursor.execute(sql, (self.last_total,self.userid))
        conn.commit()
        cursor.close()

    def save_laststudy(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set last_study = %s where userid =%s "
        cursor.execute(sql, (self.last_study,self.userid))
        conn.commit()
        cursor.close()

    def save_totalstudy(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set total_study = %s where userid=%s"
        cursor.execute(sql, (self.total_study,self.userid))
        conn.commit()
        cursor.close()
        conn.close()

    def save_totaltime(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set total_time = %s where userid=%s"
        cursor.execute(sql, (self.total_time, self.userid))
        conn.commit()
        cursor.close()
        conn.close()

    def save_percentage(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set percentage = %s where userid =%s"
        cursor.execute(sql, (self.percentage,self.userid))
        conn.commit()
        cursor.close()

    def clean_thisstudy(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = "update user set this_study = 0 where userid =%s "
        cursor.execute(sql,(self.userid))
        conn.commit()
        cursor.close()

    def query_all():
        conn=get_conn()
        cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql="select * from user"
        cursor.execute(sql)
        rows=cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_totaltime(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select total_time from user where userid=%s"
        cursor.execute(sql,(self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_totalstudy(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select total_study from user where userid=%s"
        cursor.execute(sql,(self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_thisclassstart(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select this_class_start from user where userid=%s"
        cursor.execute(sql, (self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_thisclassend(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select this_class_end from user where userid=%s"
        cursor.execute(sql, (self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_thisstart(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select this_start from user where userid=%s"
        cursor.execute(sql, (self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_thisstudy(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select this_study from user where userid=%s"
        cursor.execute(sql, (self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def query_n_u_s_g_p_a(self):
        conn = get_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select name,userid,school,gender,percentage,avatar from user where userid=%s"
        cursor.execute(sql, (self.userid))
        rows = cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def paiming100():
        conn = get_conn()
        cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql="select name,achievement from user order by achievement desc limit 100 "
        cursor.execute(sql)
        rows=cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

    def chaxunmingci(self):
        conn = get_conn()
        cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql="select rank from (select userid,(@rank:=@rank+1)as rank from user,(select(@rank :=0))temp order by percentage desc)userid where userid=%s"
        cursor.execute(sql,(self.userid))
        rows=cursor.fetchall()
        print(rows)
        conn.commit()
        cursor.close()
        conn.close()

