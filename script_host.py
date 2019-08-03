# -*- coding: utf-8 -*-
"""This script governs the host server behaviours"""

import hashlib
import socket
import sys


def start_service():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('', 5000)
    print('Starting service on %s port %s' % server_address)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(5)

    while True:
        # Wait for connection
        print('Waiting for connection')
        connection, client_address = sock.accept()
        connection.setblocking(False)

        # Receive data until the end
        try:
            print('Connection from', client_address)

            # Receive the data
            fulldata = b''
            while True:

                try:
                    fulldata += connection.recv(1024)
                except BlockingIOError:
                    print('full data: ', fulldata)
                    print('no more data from', client_address)
                    break


            print("Properly closed loop")
            # if data:
            # connection.sendall(b"8")  # data)

        finally:
            # Clean up the connection
            connection.close()

        # hashlib.sha3_256(variable.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    start_service()