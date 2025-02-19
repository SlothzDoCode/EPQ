import socket

class Client():
    def __init__(self):
        self.IP = "192.168.1.76"
        self.port = 2325
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.IP, self.port))
        
    def greenFlag(self):
        try:
            msg = "Green flag"
            
            self.client.send(msg.encode())
            
        except:
            pass  
        
    def yellowFlag(self):
        try:
            msg = "Yellow flag"
            
            self.client.send(msg.encode())
            
        except:
            pass        
        
    def redFlag(self):
        try:
            msg = "red flag"
            
            self.client.send(msg.encode())
            
        except:
            pass
        
    def blueFlag(self):
        try:
            msg = "Green flag"
            
            self.client.send(msg.encode())
            
        except:
            pass
        
    def shutdown(self):
        try:
            msg = "exit_server"
            
            self.client.send(msg.encode())
        
        except:
            pass     
        
    def PB(self):
        try:
            msg = "PB_alert"
            
            self.client.send(msg.encode())
            
        except:
            pass                   
        
    def updatePos(self,chosenPos):
        try:
            msg = str("pos " + chosenPos)
            
            self.client.send(msg.encode())
            
        except:
            pass
        
    def updateTimer(self,chosenTime):
        try:
            msg = str("time" + chosenTime)
            
            self.client.send(msg.encode())
            
        except:
            pass
        
    def PB_Close(self):
        try:
            msg = "PB_close"
        
            self.client.send(msg.encode())
            
        except:
            pass
        
    def pitstop(self):
        try:
            msg = "Pitstop"
            
            self.client.send(msg.encode())
            
        except:
            pass    
