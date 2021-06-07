import socket

# AF_INET Address Family of IPv4
# SOCK_STREAM TCP Protocol

IP = "127.0.0.1"

s = socket.socket()
s.connect((IP, 9945))

received = ''

while True:
    msg = s.recv(4096)
    if (len(msg) <= 0):
        break

    received += msg.decode("utf-8")

print(received)
