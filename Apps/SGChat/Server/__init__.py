import sgplib,socket
#难死我了，不写这个傻逼玩意了
MODE_TABLE={
    "ping":bytes([0]),
    "pong":bytes([1]),
    "reg":bytes([2]),
    "open":bytes([3]),
    "close":bytes([4]),
    "chat":bytes([5]),
    "NameInUse":bytes([6])
}
class Server:
    def __init__(self,host="0.0.0.0",port=60134):
        self.host,self.port=host,port
        self.usernames=[]
        self._run()
    def _serve(self,cli,add):
        zcli=sgplib.Socket(cli)
        #Waiting for first ping
        assert zcli.recv(32) == MODE_TABLE["ping"], "Invaild Ping"
        #Pong
        zcli.send(MODE_TABLE["pong"])
        #Waiting for restiger
        regpack=zcli.recv(128)
        assert bytes(list(regpack)[0]) == MODE_TABLE["reg"], "Invaild restiger"
        #Unpack restiger
        regpack=bytes(list(regpack)[1:]).decode("utf-8")
        name=regpack
        if name in self.usernames:
            zcli.send(MODE_TABLE["NameInUse"])
            cli.close()
            return
        #ok then u got this name
        self.usernames.append(name)
        #PING again
        zcli.send(MODE_TABLE["ping"])
        #Wait for PONG
        assert zcli.recv(32) == MODE_TABLE["pong"], "Invaild Pong"
        #event-processing mainloop
        while 1:
            data=zcli.recv(65536)
            #this should be OPEN
            datatype=bytes(list(data)[0])
            assert datatype == MODE_TABLE['open'], "First package should be OPEN"
            

    def _run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((self.host,self.port))
        self.sock.listen(5)
        while 1:
            cli,addr=self.sock.accept()

print("""
     SpeedGo ChatServer Demo v1.0

A chat protocol in slow connection speed.
=========================================
""")
port=input("Server running port:")
assert port.isdigit() , "Invaild port"
port=int(port)
assert port>0 and port <65535 , "Invaild port range"
