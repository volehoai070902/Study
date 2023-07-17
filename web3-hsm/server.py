import socket
import client
import threading

HOST= "0.0.0.0"
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
