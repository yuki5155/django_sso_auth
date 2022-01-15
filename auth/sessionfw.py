import redis
import json
from .session import RedisController

r = RedisController('localhost')

class main_recoder:
    def __init__(self):
        self.data = self.get_data()
    @property
    def sessionid(self):
        return self._sessionid
    
    @sessionid.setter
    def sessionid(self, id):
        self._sessionid = id
    
    @sessionid.deleter
    def sessionid(self):
        del self._sessionid
    
    @property
    def all_data(self):
        return self.userdata


class UserDao:
    def __init__(self):
        self.screen_name = None
        self.account_id = None
    
    def userdata(self):
        return self.data['User']
    
    @property
    def screenname(self):
        return self.screen_name
    
    @screenname.setter
    def screenname(self, screenname):
        self.screen_name = screenname
    
    @property
    def accountid(self):
        return self.screen_name

    @accountid.setter
    def accountid(self, accountid):
        self.account_id = accountid

    def add_user(self, screen_name, account_id):
        self.screenname = screen_name
        self.accountid = account_id
        self.data['User'] = {
            'screen_name': screen_name,
            'accountid': account_id
        }


# redis
class DaoInterface(main_recoder, UserDao):
    def __init__(self, sessioid):
        self._sessionid = sessioid
        main_recoder.__init__(self)
        UserDao.__init__(self)

    def save(self):
        
        r.save(self._sessionid, self.data, timeout=900)

    def delete(self):
        r.delete_session(self._sessionid)
    
    def get_data(self):
        
        try:
            data = r.get(self._sessionid)

        except TypeError:
            data = {}

        return data