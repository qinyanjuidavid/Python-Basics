import socket
socketserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()#Getting the machine name
port=9999
#Bind the host to the port
socketserver.bind((host,port))
socketserver.listen(5)
while True:
    clientsocket,addr=socketserver.accept()
    print(f"Got a connection from {addr}")
    msg="Thank you for connecting"
    clientsocket.send(msg.encode("ascii"))
    clientsocket.close()