#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(".")  #.表示当前目录
import common.common

for i in range(0,5):
    target_url = common.common.get_target_url('ssd',i)
    result = common.common.fetch_data(target_url)

    if result != 0 :
        print result
        break


print 'SUCCESS'