import socket

IP = "127.0.0.1"

s = socket.socket()
s.bind((IP, 9945))

print("IP address of the server is {}".format(IP))


s.listen()
message = input("Enter the message to send to the receiver: ")

while True:
    connection, clientAddress = s.accept()
    print(f"Connection to {clientAddress} establised")
    connection.send(bytes(message, "utf-8"))
    connection.close()
