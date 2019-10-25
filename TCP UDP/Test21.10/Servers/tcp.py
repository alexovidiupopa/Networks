Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import socket
from threading import Thread



def handleClient(conn, addr):
    ret = "Message recieved"
    print("Connected to", addr)
    while(1):
        message = conn.recv(1024).decode("utf-8")
        print("From", addr, ":", message)
        conn.send(ret.encode("utf-8"))
        if("close" in message):
            break
    print("Connection to ", addr, " was closed")
    conn.close()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 4444))
s.listen(5)

while(1):
    conn, addr = s.accept()
    thr = Thread(target=handleClient, args=(conn, addr))
    thr.start()
