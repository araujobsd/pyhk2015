def server():
	import sys, os, socket

	port = 11111
	host = '10.0.1.23'
	backlog = 5
	buf_size = 1024

	try:
		listening_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		listening_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		listening_socket.bind((host, port))
		listening_socket.listen(backlog)
	except socket.error, (value, message):
		if listening_socket:
			listening_socket.close()
		print 'Could not open socket: ' + message
		sys.exit(1)

	while True:
		accepted_socket, adress = listening_socket.accept()
		data = accepted_socket.recv(buf_size)
		if data:
			accepted_socket.send('Hello, and goodbye.')
		accepted_socket.close()

server()
