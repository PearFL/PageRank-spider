import redis


class Base0(object):
    def __init__(self):
        self.r = redis.Redis(host='*', port=6379, db=0)


class Base1(object):
    def __init__(self):
        self.r = redis.Redis(host='*', port=6379, db=1)


class TestString(Base0):
    """
    set -- 设置值
    get -- 获取值
    mset -- 设置多个键值对
    mget -- 获取多个键值对
    append -- 添加字符串
    del -- 删除
    incr/decr -- 增加/减少 1
    """
    def test_set(self, key, val):
        ''' sadd -- 添加元素,val可以是dict '''
        rest = self.r.set(key, val)
        return rest

    def test_get(self, key):
        ''' srem -- 删除元素 '''
        rest = self.r.get(key)
        return rest

    def test_del(self, key):
        ''' srem -- 删除元素 '''
        rest = self.r.delete(key)
        return rest


class TestSet(Base1):
    """
    sadd/srem -- 添加/删除元素
    sismember -- 判断是否为set的一个元素
    smembers -- 返回该集合的所有成员
    sdiff -- 返回一个集合与其它集合的差异
    sinter -- 返回几个集合的交集
    sunion -- 返回几个集合的并集
    """

    def test_sadd(self, key, val):
        ''' sadd -- 添加元素,val可以是dict '''
        rest = self.r.sadd(key, val)
        return rest

    def test_srem(self, key, val):
        ''' srem -- 删除元素 '''
        rest = self.r.srem(key, val)
        return rest

    def test_sismember(self, key):
        ''' sismember -- 判断是否为set的一个元素 '''
        rest = self.r.sismbers(key)
        return rest

    def test_smembers(self, key):
        ''' smembers -- 返回该集合的所有成员 '''
        rest = self.r.smembers(key)
        return rest


# def main():
#     string_obj = TestString()
#     string_obj.test_set("url", 1)
#     print(string_obj.test_get("url"))
#     if string_obj.test_get("url").decode() == '1':
#         print("True")
#
#
# if __name__ == '__main__':
#     main()
