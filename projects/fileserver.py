import socket
import os
import threading

def File(name,sock):
    filename=sock.recv(1024)
    print(filename)
    print(os.path.isfile(filename))
    if os.path.isfile(filename):
        sock.send("EXISTS" +str(os.path.getsize(filename)))
        userResponse=sock.recv(1024)
        if userResponse[:2]=='OK':
            with open(filename, 'rb') as f:
                bytestosend=f.read(1024)
                sock.send(bytestosend)
                while bytestosend!="":
                    bytestosend=f.read(1024)
                    sock.send(bytestosend)

def Main():
    host ="127.0.0.1"
    port = 5004
    s=socket.socket()
    s.bind((host,port))
    s.listen(5)
    print("server started")
    while True:
        c,addr=s.accept()
        print("client connected ip:{}").format(addr)
        try:
            t=threading.Thread(target=File, args=("File",c))
            t.start()
        except socket.error:
            print("There was an error")
    s.close()

if __name__== "__main__":
    Main()