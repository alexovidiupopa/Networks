import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("0.0.0.0",5555))

buff, addr = s.recvfrom(10)

message = buff.decode("utf-8")
print("From ", addr[0], ": ", message)
count = 0
for letter in message:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        count+=1

s.sendto(count.to_bytes(4, 'little'), addr)
