#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(".")  #.表示当前目录
import common.fetch_coolshell
import fetch_urls

fetch = common.fetch_coolshell.insert_data(fetch_urls.urls)


print fetch