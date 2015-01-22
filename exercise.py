import socket
import sys
from thread import *

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print('Failed to create socket.  Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
	sys.exit()

host = '127.0.0.1'
port = 5050

try:
	s.bind((host,port))
except socket.error, msg:
	print('Socket bind failed! Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
	sys.exit()

print('Socket successfully bound on port ' + str(port))
s.listen(5) #allow for standard 5 connections at once

#Loop to keep the server running
def clientThread(conn):
	while 1:
		data = conn.recv(1024)
		reply = data.strip() + ' Zak\r\n'
		
		if not data:
			break
		
		conn.sendall(reply.encode('UTF8'))

	conn.close()

while 1:
	conn, addr = s.accept()
	start_new_thread(clientThread ,(conn,))
	print('Connection received - spawned new thread')
c
s.close()
