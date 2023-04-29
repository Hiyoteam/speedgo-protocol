import socket,sgplib
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",1145))
server.listen(5)
while 1:
    cli,add=server.accept()
    print(f"Accept new from {add}")
    zcli=sgplib.Socket(cli)
    awwa=zcli.recv(100).decode("utf-8")
    if awwa == "Hello SpeedGo World!":
        print('Recive a VAILD ZIPPED REQUEST!')
    else:
        print("invaild request")
        cli.close()
        continue
    zcli.send("Hello yo too!".encode("utf-8"))
    cli.close()