# First of all import the socket library
import socket
def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


# Performs Modulo-2 division
def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]

    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0'*pick, tmp) + divident[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword


def decodeData(data, key):

    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)

    return remainder


# Creating Socket
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
PORT = 12345
IP = "127.0.0.1"

s.bind(('', PORT))
print("socket binded to %s" % (PORT))
# put the socket into listening mode
maxConnections = 5
s.listen(maxConnections)
print("socket is listening with maximum {} connections".format(maxConnections))

key = input("Enter the polynomial key: ")

while True:
    connection, address = s.accept()
    print('Got connection from', address)

    # Get data from client
    data = connection.recv(2048)
    print(data)
    data = data.decode("utf-8")

    print(data)

    if not data:
        break

    ans = decodeData(data, key)
    # print("Remainder after decoding is->"+ans)

    # If remainder is all zeros then no error occured
    temp = "0" * (len(key) - 1)
    if ans == temp:
        connection.sendall(bytes("Data: " + data[:-3] + " Received. No error FOUND", "utf-8"))
    else:
        connection.sendall(bytes("The received data is currupted.", "utf-8"))

    connection.close()
