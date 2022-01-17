import redis
import json

class RedisController:

    def __init__(self, host):
        self.r = redis.Redis(host=host, port=6379)
    
    def save(self, sessionid, data, timeout=900):
        data = json.dumps(data)
        self.r.set(sessionid, data, ex=timeout)
    
    def get(self, sessionid):
        data = self.r.get(sessionid)
        data = json.loads(data)

        return data
    
    def delete_session(self, sesionid):
        self.r.delete(sesionid)