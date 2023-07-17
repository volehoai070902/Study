import psycopg2
from . import envHSM 

class ConnectDatabase(object):
    def __new__(cls):
        print("Create object")
        if not hasattr(cls,'instance'):
            cls.instance = super(ConnectDatabase,cls).__new__(cls);
        return cls.instance;
    def __init__(self):
        self.__conn = psycopg2.connect(database = envHSM.Config("DATABASE"), 
                            user = envHSM.Config("USER_DB"), 
                            host= envHSM.Config("HOST"),
                            password = envHSM.Config("PASSWORD"),
                            port = 5432)
    def getConnect (self):
        return self.__conn;