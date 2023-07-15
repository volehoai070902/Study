import socket
import client
import threading
from _thread import *
from concurrent.futures import ThreadPoolExecutor

HOST= "127.0.0.1"
PORT= 5005;

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.bind((HOST,PORT));
s.listen();

try:
    while True:
        server, addr = s.accept();
        print("Connect by", addr);
        Client_HSM = client.Client(server=server);
        thread = threading.Thread(target=Client_HSM.run,);
        thread.start();
finally:
    s.close();
