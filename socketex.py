import socket
import os
from tkinter import filedialog
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter as tk 
from tkinter import messagebox as mb 
from tkinter import messagebox
from tkinter import *
import time



host = "localhost"
port =4455
ADDR = (host,port)
SIZE = 1024


def call(): 
    res = mb.askquestion('Choosing action', 'do you want to upload a file?') 
      
    if res == 'yes' : 
        root.destroy() 
          # send a file
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        global file
        file = filedialog.askopenfile()
        file=file.name
        client.send(file.encode())
        fil = open(file, 'rb')
        data = fil.read()
        client.sendall(data)
        client.close()
        
    else :
        #get a file 
        root.destroy()
        res = mb.askquestion('Choosing action', 'do you want to download a file?') 
        if res == 'yes':
            filename = input("enter the file name")
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            client.send("send".encode())
            client.send(filename.encode())
    
            client.close
            client.bind("localhost", 9090)
            client.listen()
            while True:
                s , ADDR = client.accept()

                msg = s.recv(SIZE)
                if (msg == "file wasn't found"):
                    print('this file dosent exist')
                    break
                if (msg == "file wasn found"):
                
                    file = s.recv(SIZE)
                    file = open (filename, "wb")
                    data = client.recv(SIZE).decode()
                    file.write(data)
                    break
            client.close()
        else:
            root.destroy()
 
  
root = tk.Tk() 
root.geometry("200x200")
canvas = tk.Canvas(root, width = 500,  height = 500) 
canvas.pack() 
b = Button(root, text = "Choose action", command = call)
b.place(x=50,y=50)
canvas.create_window(100, 100, window = b) 
root.mainloop()


  
