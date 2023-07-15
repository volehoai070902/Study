a = "01370373636208A501F7663A693F76".lower();
b = bytes.fromhex(a);

read_byte = int(b[0]);
information =[];
index = 0;
n = 0;
print (len(b))
while read_byte != None:
    str_ = ""
    for i in range (0, read_byte):
        str_ = str_ + str(b[index + i + 1]) + " ";
        n = n + 1;
    
    information.append(str_);
    if n + 1== len(b):
        break;
    index = n + 1;
    
    read_byte = b[index];
    n = n + 1;

hex_string = str(information[2]).split();

PIN = "";
BANK_CODE="";
for i in range (0, len(str(information[2]).split())):
    index = int (hex_string[i]);
    str_ = hex(index)[2:];
    PIN = PIN + str_;

abc = str(information[1]).split();
