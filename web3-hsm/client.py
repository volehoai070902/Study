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
        print("Hello")
        
    def run(self):
        try:
            while True:
                data = self.server.recv(1024);
                str_data :str= data.decode("utf8")
                str_data = str_data.strip();
                #2553SCB16 ->  0255-03SCB-08A501F7663A693F76
                
        finally:
            self.s.close();

