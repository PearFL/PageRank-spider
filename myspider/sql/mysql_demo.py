import pymysql


class Base(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='*',
            port=3306,
            database='*',
            user='*',
            passwd='*',
            charset='utf8',
        )


class WxMysql(Base):
    global table
    table = "pagerank_demo"

    def test_insert(self, url, title):
        cursor = self.conn.cursor()

        sql_insert = 'insert into '+table+'(url, title, in_sum, out_sum, pg) values(%s, %s, %s, %s, %s);'

        print(sql_insert)
        cursor.execute(sql_insert, (url, title, 0, 0, '1'))

        rest = self.conn.commit()
        cursor.close()

        return rest

    def test_update_in_out_sum(self, url_out, url_in):
        cursor = self.conn.cursor()

        sql_update_out_sum = 'update '+table+' set out_sum=out_sum+1 where url=%s'
        sql_update_in_sum = 'update '+table+' set in_sum=in_sum+1 where url=%s'

        cursor.execute(sql_update_out_sum, url_out)
        cursor.execute(sql_update_in_sum, url_in)

        rest = self.conn.commit()
        cursor.close()

        return rest

    def end(self):
        self.conn.close()


# if __name__ == '__main__':
#     t = WxMysql()
#     t.test_update_in_out_sum("www.hfuu.edu.cn", "www.baidu.com")
#     t.end()