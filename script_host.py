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
        conn, client_address = sock.accept()
        conn.setblocking(False)

        # Receive data until the end
        try:
            print('Connection from', client_address)

            # Receive the data
            data_stream = b''
            while True:

                try:
                    data_stream += conn.recv(1024)
                except BlockingIOError:
                    data_stream = data_stream.split(u'\u0003\u0000\u0002'.encode('utf-8'))
                    print('Recieved data: ', data_stream)
                    print('Data stream complete from ', client_address)
                    break


            print("Properly closed loop")
            # if data:
            # connection.sendall(b"8")  # data)

        finally:
            # Clean up the connection
            conn.close()

        # hashlib.sha3_256(variable.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    start_service()