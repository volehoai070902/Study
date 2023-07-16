import psycopg2

class ConnectDatabase(object):
    def __new__(cls):
        print("Create object")
        if not hasattr(cls,'instance'):
            cls.instance = super(ConnectDatabase,cls).__new__(cls);
        return cls.instance;
    def __init__(self):
        self.__conn = psycopg2.connect(database = "HSM_DB", 
                            user = "lehoai", 
                            host= 'localhost',
                            password = "lehoai123",
                            port = 5432)
    def getConnect (self):
        return self.__conn;

# a = ConnectDatabase();
# cur = a.getConnect().cursor();
# cur.execute(query="INSERT INTO public.\"BANK_CODE\"(id, code, index) VALUES ('d8c85ed2-2392-11ee-be56-0242ac120002', 'acb',2);");
# a.getConnect().commit();
# cur.close();
# a.getConnect().close();

