import pymysql
from operator import itemgetter, attrgetter
import Levenshtein


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


class ViewMysql(Base):
    global table
    table = "pagerank3"

    def test_select_all(self):
        cursor = self.conn.cursor()
        sql_select_all = 'select * from '+table+';'

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

    def end(self):
        self.conn.close()


def main():
    t = ViewMysql()
    datas = t.test_select_all()
    datas = list(datas)

    search = '合肥'

    result = []

    for data in datas:
        data = list(data)
        sim = Levenshtein.jaro_winkler(data[1], search)

        if sim:
            mydict = {}
            mydict["url"] = data[0]
            mydict["title"] = data[1]
            mydict["in"] = data[2]
            mydict["out"] = data[3]
            mydict["pg"] = data[4]
            mydict["rank"] = sim * 700 + data[4]
            # print(mydict["rank"])
            result.append(mydict)

    result = sorted(result, key=lambda k: (k.get('rank', 0)), reverse=True)
    result = result[0:9]
    return result


# if __name__ == '__main__':
#     main()
#     # ans = main()
#     # print(ans)

