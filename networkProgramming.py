import socket
serversocket=socket.socket(
    socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999

serversocket.bind((host,port))
serversocket.listen(5)
while True:
    clientsocket,addr=serversocket.accept()
    print(f"Got a connection from str{addr}")
    msg="Thank you for connecting"
    clientsocket.send(msg.encode("ascii"))
    clientsocket.close()