#length field -> byte to read
import socket
import errorHSM.error

class HSM:
    def __init__(self, hsm_conn:socket.socket=None):
        self.HSM_Conn = hsm_conn;
    
    def HandleMsg(self, data:str):
        self.HSM_Conn.sendall(bytes(data.encode()));
        response = self.HSM_Conn.recv(1024);
        return response.decode();
    
    def SplitResponse(self,data:str = None):
        split_data = data[1:len(data)].split("#");
        if split_data[0] == "00":
            raise Exception(errorHSM.error.ErrorType(split_data));
        return split_data;

    def GenerateKey(self,data:str = None):
        data_ = self.HandleMsg(data= data);
        try:
            response = self.SplitResponse(data_);
            return response[1];
        except Exception as e:
            return str(e);

    def AddKeyToHSM(self, data:str):
        data_ = self.HandleMsg(data=data);
        try:
            response = self.SplitResponse(data_);
            return response[1];
        except Exception as e:
            return str(e);

    def EncryptData(self, data:str):
        data_ = self.HandleMsg(data=data);
        try:
            response = self.SplitResponse(data_);
            return response[8];
        except Exception as e:
            return str(e);

    def DecryptData(self, data:str):
        data_ = self.HandleMsg(data=data);
        try:
            response = self.SplitResponse(data_);
            return response[8];
        except Exception as e:
            return str(e);

    def TranslatePin(self, data:str):
        data_ = self.HandleMsg(data= data);
        print(data_);
        try:
            response = self.SplitResponse(data_);
            return response[2] ;
        except Exception as e:
            return str(e);

        

