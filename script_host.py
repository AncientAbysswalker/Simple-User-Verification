# -*- coding: utf-8 -*-
"""This script governs the host server behaviours"""

import hashlib
import socket
import sys
import sqlite3

def start_service():
    """Start main script loop to run server-side service on port 5000"""

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port 5000
    server_address = ('', 5000)
    print('Starting service on %s port %s' % server_address)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    # Main loop listening for connections and responding
    while True:
        # Wait for connection
        print('Waiting for connection')
        conn, client_address = sock.accept()
        conn.settimeout(1.0)

        # Receive data in blocks of 1024 bytes, concatenating the bytes after connection timeout
        try:
            print('Connection from', client_address)

            # Receive the data
            data_stream = b''
            while True:
                try:
                    data_stream += conn.recv(1024)
                except socket.timeout:
                    data_stream = data_stream.split(u'\u0003\u0000\u0002'.encode('utf-8'))
                    _user = data_stream[0].decode('utf-8')
                    _passkey = hashlib.sha3_256(data_stream[1]).hexdigest()
                    _random = data_stream[2]

                    # Clear data stream so the un-hashed password is not accessible
                    data_stream = None

                    print('I have recieved data!')
                    print('User: ', _user)
                    print('Hashed Passkey: ', _passkey)
                    print('Random number: ', _random)
                    print('Data stream complete from ', client_address)
                    break

            #print("Properly closed loop")

            # Connect to DB and see if user is there
            sql_conn = sqlite3.connect('user_db.db')
            sql_crsr = sql_conn.cursor()
            print(_user, _passkey)
            sql_crsr.execute("SELECT 1 FROM UserBase WHERE user_name=(?) AND user_pass=(?);", (_user, _passkey))
            valid_user = True if sql_crsr.fetchone() else False
            sql_conn.close()

            if valid_user:
                conn.sendall(b"valid user")  # data)
            else:
                conn.sendall(b"INVALIDDDDDD")  # data)
            # connection.sendall(b"8")  # data)

        finally:
            # Clean up the connection
            conn.close()

        # hashlib.sha3_256(variable.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    start_service()