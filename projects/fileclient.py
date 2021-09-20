import socket
def Main():
    host ="127.0.0.1"
    port = 5004

    s= socket.socket()
    s.connect((host,port))
    filename=raw_input("filename .>")
    if filename !='q':
        s.send(filename)
        data=s.recv(1024)
        if data[:6]=='EXISTS':
            filesize=long(data[6:])
            message=raw_input('file exists ,' + str(filesize) + "Bytes, download?(Y/N) .>")
            if message =='Y':
                s.send('OK')
                f=open('new_'+filename,'wb')
                data=s.recv(filesize)
                totalRecv=len(data)
                f.write(data)
                while totalRecv<filesize:
                    data=s.recv(filesize)
                    totalRecv+=len(data)
                    f.write(data)
                print "download complete"
        else:
            print "file doesnt exist"
    s.close()
if __name__=="__main__":
    Main()
        