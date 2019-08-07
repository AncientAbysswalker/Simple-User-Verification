import socket
import hashlib


def start_service():
    """Start main script to connect to service on port 5000"""
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('SERVER_IP', 5000)
    print('Connecting to %s port %s' % server_address)
    try:
        sock.connect(server_address)
    except ConnectionRefusedError:
        print("Service unavailable. Connection refused from %s port %s" % server_address)
        return

    try:
        # Define data for test
        user = b'test_user'
        passkey = b'test_pass'
        rand_num = b'key'
        separator = u'\u0003\u0000\u0002'.encode('utf-8')

        message = user + separator + passkey + separator + rand_num

        # Send all data
        sock.sendall(message)

        # Look for the response
        data = sock.recv(64)

        # Is response valid?
        if data == hashlib.sha3_256(rand_num + user).hexdigest().encode('utf-8'):
            print("Valid user")
        else:
            print("Invalid user")

    finally:
        print('Closing socket')
        sock.close()


if __name__ == '__main__':
    start_service()
