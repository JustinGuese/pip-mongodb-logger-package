from requests import post

__version:__ = "0.1"

class MongoDBLogger:  
    def __init__(self, auth_pw, logging_url ='http://localhost:8888', appname ='mongodblogger') -> None:
        self.logurl = logging_url
        self.appname = appname
        self.auth_pw = auth_pw

    def send(self, log):
        temp = {
            "password": self.auth_pw,
            "appname" : self.appname,
            "errorjson" : log
        }
        return post(self.logurl, json=temp)