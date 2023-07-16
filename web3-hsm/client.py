import socket
from threading import Thread
from helper.hsm_func import HSM
HOST = "117.4.241.150"
PORT = 7500


class Client():
    s = None;
    server = None;
    HSM = None;
    def __init__(self,server:socket.socket=None):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        self.s.connect((HOST,PORT));
        self.server = server;
        self.HSM = HSM(self.s);
        

    def HandleMsg(msg):
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


        
    def run(self):
        try:
            while True:
                data = self.server.recv(1024);
                str_data :str= data.decode("utf8")
                str_data = str_data.strip();

                #2553SCB16 ->  0255-03SCB-08A501F7663A693F76
                
        finally:
            self.s.close();

