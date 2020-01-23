import hashlib
import redis

def create_hash(data):
    s = hashlib.sha256()  
    s.update(data.encode('utf-8')) # the input type of sha256 must be byte
    return s.hexdigest()

def encode(str):
    return str.encode('utf-8')

def decode(bytes):
    return bytes.decode('utf-8')

class Database():
    def __init__(self, host='localhost', port=6379, db=0, bucket='blocks'):
        self.bucket = bucket
        self.db = redis.Redis(host=host, port=port, db=db)

    def put(self, key, value): 
        self.db.hset(self.bucket, key, value)   # hset(name, key, value) name指定一个散列表的名称

    def get(self, key):
        return self.db.hget(self.bucket, key)

    def reset(self):
        self.db.flushdb()

# print(create_hash('kevin'))
# print(int(create_hash('kevin'), 16))

# import hashlib
# import redis

# def encode(str, code='utf-8'):
#     if not str:
#         return b''
#     return str.encode(code)


# def decode(bytes, code='utf-8'):
#     if not bytes:
#         return u''
#     return bytes.decode(code)
    
# def sha256(*args):
#     m = hashlib.sha256()
#     for arg in args:
#         m.update(arg)
#     return m.hexdigest()

# class DB(object):
#     def __init__(self, host='localhost', port=6379, db=0, bucket='blocks'):
#         self.bucket = bucket
#         self.db = redis.Redis(host='localhost', port=6379, db=0)

#     def put(self, key, val):
#         self.db.hset(self.bucket, key, val)

#     def get(self, key):
#         # return bytes
#         return self.db.hget(self.bucket, key)

#     def reset(self):
#         self.db.flushdb()
