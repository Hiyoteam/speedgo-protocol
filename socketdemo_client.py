import socket,sgplib
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",1145))
zcli=sgplib.Socket(client)
zcli.send("Hello SpeedGo World!".encode("utf-8"))
print("Sent hello world")
data=zcli.recv(100)
if data == "Hello yo too!".encode("utf-8"):
    print("VAILD FEEDBACK,CLIENT OK!")