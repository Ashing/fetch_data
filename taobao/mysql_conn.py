__author__ = 'such'
#-*-coding:utf-8-*-
import sys
sys.setdefaultencoding('utf-8')

class mysql_connect:

    def __init__(self):
        import conf
        __db_host = conf.db_host
        __db_user = conf.db_user
        __db_passwd = conf.db_passwd
        __db_name = conf.db_name
        __db_charset = conf.db_charset
        import MySQLdb
        # 連接到 MySQL
        conn = MySQLdb.connect(host=__db_host, user=__db_user, passwd=__db_passwd, db=__db_name,charset=__db_charset)
        self.conn = conn

    def retrn_conn(self):
        return self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.conn.close()