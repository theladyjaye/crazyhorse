from uuid import uuid4
import datetime

"""
import M2Crypto
import hashlib

class RedisSessions(object):

    def __init__(self, request):
        self.key  = "SID"

        if request.cookies[self.key] is not None:
            self.id = request.cookies[self.key]
            #fetch session from store
        else:
            self.id = self.generate_session_id()

    def generate_session_id(self):

        hash = hashlib.md5()
        hash.update(M2Crypto.m2.rand_bytes(16)) # 128 bit
        return hash.hexdigest()

    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError as e:
            return None
"""
def feature_sessions(context):

    #time = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)

    if context.request.cookies["SID"] == None:
        sid = str(uuid4())
        context.response.cookies.add(name="SID", 
                                 value=sid, 
                                 path="/",
                                 #expires=time,
                                 #domain="orion",
                                 secure=None,
                                 httponly=None)

        context.session = {"test":sid}
    else:
        context.session = {"test":context.request.cookies["SID"]}
    
    return 

