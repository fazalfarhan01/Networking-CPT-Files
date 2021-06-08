import socket			

def xor(a, b):

	# initialize result
	result = []
	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')
	return ''.join(result)

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


# Performs Modulo-2 division
def mod2div(divident, divisor):
	pick = len(divisor)
	tmp = divident[0 : pick]
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

def encodeData(data, key):

	l_key = len(key)

	# Appends n-1 zeroes at end of data
	appended_data = data + '0'*(l_key-1)
	remainder = mod2div(appended_data, key)

	# Append remainder in the original data
	codeword = data + remainder
	return codeword	
	
# Create a socket object
s = socket.socket()

# Define the IP & PORT on which you want to connect
PORT = 12345
IP = '127.0.0.1'

# connect to the server on local computer
s.connect((IP, PORT))

input_string = input("Enter data you want to send: ")
key = input("Enter the polynomial key: ")

data = (''.join(format(ord(x), 'b') for x in input_string))
print(data)

ans = encodeData(data,key)
print(ans)
s.sendall(bytes(ans, "utf-8"))


# receive data from the server
print (s.recv(1024).decode("utf-8"))

# close the connection
s.close()
