import pandas as pd
import uuid
from config.connectDatabase import ConnectDatabase;
database = ConnectDatabase();

df = pd.read_excel("banks.xlsx", usecols='A, B');
bankcode = df['bank_code'].tolist();
nameofbank = df['bank_name'].tolist();

conn =  database.getConnect();
print (conn)
cur = conn.cursor();

for i in range (0, len(bankcode)):
    id = str(uuid.uuid4());
    code = bankcode[i];
    name = nameofbank[i];
    query = "insert into public.\"BANK_CODE\"(id, code, index, name) values (%s,%s,%s,%s)";
    cur.execute(query=query, vars=(id,code,i,name));
    database.getConnect().commit()

cur.close() ;
conn.close();
