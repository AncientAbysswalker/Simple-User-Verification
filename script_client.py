import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('SERVER_IP', 5000)
print('Connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Define data for test
    a = b'user'
    b = b'pass'
    r = b'key'
    s = u'\u0003\u0000\u0002'.encode('utf-8')

    message = a + s + b + s + r

    # Send all data
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(256)
        amount_received += len(data)
        print(sys.stderr, 'received "%s"' % data)

finally:
    print('Closing socket')
    sock.close()