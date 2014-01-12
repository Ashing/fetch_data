__author__ = 'such'
#-*-coding:utf-8-*-
import sys
sys.setdefaultencoding('utf-8')
import MySQLdb

class mysql_connect:

    def __init__(self):
        import conf
        __db_host = conf.db_host
        __db_user = conf.db_user
        __db_passwd = conf.db_passwd
        __db_name = conf.db_name
        __db_charset = conf.db_charset

        # 連接到 MySQL
        conn = MySQLdb.connect(host=__db_host, user=__db_user, passwd=__db_passwd, db=__db_name,charset=__db_charset)
        self.conn = conn

    def inser_data(self,sql_content):

        sql_content = MySQLdb.escape_string(sql_content)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_content)

        except MySQLdb.Error, e:
            err =  "error %d: %s" % (e.args[0], e.args[1])
            print sql_content
            return err
        return 0

    def __del__(self):
        self.conn.commit()
        self.conn.close()