import socket
import threading

# server socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(("127.0.0.1", 1234))
ss.listen(5)

conn, client_address = ss.accept()

def run_thread(conn):
    while True:
        data = conn.recv(1024).decode()
        print("\nClient: {}".format(data))
        print(">>> [SERVER] Send message: ",)




def send_msg(msg):
    conn.send(msg.encode())


while True:
    conn, client_address = ss.accept()
    print(">>> [SERVER] Send message:",)
    txt = input()
    send_msg(txt)
    thr = threading.Thread(target = run_thread,args = conn)
    thr.start()
