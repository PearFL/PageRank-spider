import pymysql


class Base(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='39.108.128.88',
            port=3306,
            database='spiders',
            user='root',
            passwd='1q2w3e4R!',
            charset='utf8',
        )


class WxMysql(Base):
    global table
    table = "pagerank"

    def test_insert(self, url, title):
        cursor = self.conn.cursor()

        sql_insert = 'insert into '+table+'(url, title, in_sum, out_sum, pg) values(%s, %s, %s, %s, %s);'

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

    def test_update_title(self, url, title):
        cursor = self.conn.cursor()

        sql_update_title = 'update '+table+' set title=%s where url=%s'

        cursor.execute(sql_update_title, (title, url))

        rest = self.conn.commit()
        cursor.close()

        return rest

    def end(self):
        self.conn.close()


class PgMysql(Base):
    global table
    table = "pagerank4"

    def test_select_all(self):
        cursor = self.conn.cursor()
        sql_select_all = 'select url from '+table+';'

        # sql_select_all = 'insert into '+table+'(url, title, in_sum, out_sum, pg) values(%s, %s, %s, %s, %s);'
        # print(sql_select_all)

        cursor.execute(sql_select_all)
        rest = cursor.fetchall()

        self.conn.commit()
        cursor.close()

        return rest

    def test_select_in_sum(self, url):
        cursor = self.conn.cursor()
        sql_select_in_sum = 'select in_sum, pg from '+table+' where url = %s;'

        cursor.execute(sql_select_in_sum, (url, ))
        rest = cursor.fetchone()

        self.conn.commit()
        cursor.close()

        return rest

    def test_select_out_sum(self, url):
        cursor = self.conn.cursor()
        sql_select_out_sum = 'select out_sum, pg from '+table+' where url = %s;'

        cursor.execute(sql_select_out_sum, (url, ))
        rest = cursor.fetchone()

        self.conn.commit()
        cursor.close()

        return rest

    def test_update_pg(self, url, pg):
        cursor = self.conn.cursor()

        sql_update_pg = 'update ' + table + ' set pg=%s where url=%s'

        cursor.execute(sql_update_pg, (pg, url))

        rest = self.conn.commit()
        cursor.close()

        return rest

    def end(self):
        self.conn.close()


if __name__ == '__main__':
    t = PgMysql()
    ans = t.test_update_pg("http://www.hfuu.edu.cn", '3')

