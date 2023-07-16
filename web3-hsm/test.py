a = "013709434f2d4f5042414e4b08A501F7663A693F76".lower();
b = bytes.fromhex(a);

read_byte = int(b[0]);
information =[];
index = 0;
n = 0;
while read_byte != None:
    str_ = []
    for i in range (0, read_byte):
        str_.append (b[index + i + 1]);
        n = n + 1;
    
    information.append(str_);
    if n + 1== len(b):
        break;
    index = n + 1;
    
    read_byte = b[index];
    n = n + 1;


hex_string = str(information[2]).split();

COMMAND = information[0][0];
BANK_CODE="";
PIN = "";

for i in information[1]:
    BANK_CODE = BANK_CODE + chr(i);

for i in information[2]:
    PIN = PIN + hex(i)[2:];
print(COMMAND, BANK_CODE, PIN);