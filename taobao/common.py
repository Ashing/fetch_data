__author__ = 'suuuch'
#-*-coding:utf-8-*-
def get_target_url(q ,page=0 ,tab = 'all', sort = 'default'):
    '''拼装可请求的淘宝URL
    '''
    s = page * 40
    target_url = "http://s.taobao.com/search?tab=%s&q=%s&sort=%s&s=%d" %( tab , q , sort,s )
    return target_url

def fetch_data(target_url):
    '''通过传递经来的URL将数据入库
    '''
    import urllib2
    import urlparse
    from bs4 import BeautifulSoup
    import MySQLdb
    page = urllib2.urlopen(target_url)
    soup = BeautifulSoup(page)

    items = soup.find_all("div","item")
    for item in items:
        user_number_id = 0
        pro_id = item['nid']
        pro_name = item.find("h3",class_="summary").find("a")['title']
        pro_url = item.find("h3",class_="summary").find("a")['href']
        price = item.find("div",class_="price").contents[0]
        price_num = price.replace(u'￥','')
        loc = item.find("div","loc").find("div").contents[0]
        seller_url = item.find("div","seller").find("a")['href']
        r = urlparse.urlparse(seller_url)
        exec r[4]
        # 連接到 MySQL
        conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="rootroot", db="taobao",charset='utf8')
        cursor = conn.cursor()
        try:
            cursor.execute("""INSERT INTO t_product VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                (int(pro_id),pro_name.encode('utf8'),pro_url,price_num,seller_url,user_number_id,loc.encode('utf8')))
            conn.commit()
        except MySQLdb.Error, e:
            print "error %d: %s" % (e.args[0], e.args[1])
            return 1
    conn.close()
    return 0
