import redis


class Base(object):
    def __init__(self):
        self.r = redis.Redis(host='119.28.18.242', port=6379, db=0)


class TestSet(Base):
    """
    sadd/srem -- 添加/删除元素
    sismember -- 判断是否为set的一个元素
    smembers -- 返回该集合的所有成员
    sdiff -- 返回一个集合与其它集合的差异
    sinter -- 返回几个集合的交集
    sunion -- 返回几个集合的并集
    """

    def test_sadd(self, list, val):
        ''' sadd -- 添加元素,val可以是dict '''
        rest = self.r.sadd(list, val)
        return rest

    def test_srem(self, list, val):
        ''' srem -- 删除元素 '''
        rest = self.r.srem(list, val)
        return rest

    def test_sismember(self, list):
        ''' sismember -- 判断是否为set的一个元素 '''
        rest = self.r.sismbers(list)
        return rest

    def test_smembers(self, list):
        ''' smembers -- 返回该集合的所有成员 '''
        rest = self.r.smembers(list)
        return rest
