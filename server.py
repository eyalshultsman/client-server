import socket
import os

HOST = "localhost"
size = 1024
port = 4455
ADDR = (HOST,port)
listoffiles = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()
os.chdir ('C:\\Users\\user1\\Desktop\\files upload')
while True:
    conn , ADDR = s.accept()
    bol = conn.recv(1024).decode()
    if (bol == "get"):
            filename = conn.recv(1024).decode()
            data = conn.recv(1024).decode()
            file = open(filename, "wb")
            file.write (data)
            break
    if (bol == "send"):
        filename = conn.recv(size).decode()
        s.close()
        conn.close()
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(ADDR)
        try:
            conn.send("file was found".encode())
            file = open (filename, "rb")
            data = file.read()
            s.sendall(data)
            s.close()
            break
        except Exception as error:
             print(error)
             s.send("file wasn't found".encode())
             break
    
        