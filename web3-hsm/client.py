import socket
from threading import Thread
from helper.hsm_func import HSM
from config.connectDatabase import ConnectDatabase;
HOST = "12.1.78.164"
PORT = 17000

class Client:
    def __init__(self,server:socket.socket=None):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        self.s.connect((HOST,PORT));
        self.server = server;
        self.HSM = HSM(self.s);
        self.Conn = ConnectDatabase().getConnect();

    def HandleMsg(self, message:str):
        msg = bytes.fromhex(message);
        read_byte = int(msg[0]);
        information =[];
        index = 0;
        n = 0;
        while read_byte != None:
            str_ = []
            for i in range (0, read_byte):
                str_.append (msg[index + i + 1]);
                n = n + 1;
            
            information.append(str_);
            if n + 1== len(msg):
                break;
            index = n + 1;
            
            read_byte = msg[index];
            n = n + 1;


        hex_string = str(information[2]).split();

        COMMAND = information[0][0];
        BANK_CODE="";
        PIN = "";

        for i in information[1]:
            BANK_CODE = BANK_CODE + chr(i);

        for i in information[2]:
            PIN = PIN + hex(i)[2:];

        return COMMAND, BANK_CODE, PIN;


    

    def run(self):
        try:
            while True:
                data = self.server.recv(1024);
                str_data :str= data.decode("utf8")
                str_data = str_data.strip();

                #01370356434208A501F7663A693F76 -> 55 vcb  A501F7663A693F76
                command, bank_code, pin = self.HandleMsg(message=str_data);
                print (command, bank_code, pin );
                match str(command):
                    case "10":
                        response = self.HSM.GenerateKey("<10#1##D#>");
                        self.server.sendall(bytes(response.encode()));
                    case "55":
                        cur = self.Conn.cursor();
                        query = "SELECT index FROM public.\"BANK_CODE\" where code = '{}';".format(bank_code);
                        cur.execute(query=query);
                        row = cur.fetchone();
                        indexofkeybank = row[0];
                       
                        response = self.HSM.TranslatePin("<55#T0##T{}##00#{}#1111#####>".format(indexofkeybank,pin));
                        self.server.sendall(bytes(response.encode()));
                
        finally:
            self.s.close();

