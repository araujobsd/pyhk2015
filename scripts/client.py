def client():
	import sys, time, socket

	port = 11111
	host = '10.0.1.23'
	buf_size = 1024

	try:
		mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.connect((host, port))
	except socket.error, (value, message):
		if mySocket:
			mySocket.close()
		print 'Could not open socket: ' + message
		sys.exit(1)
	mySocket.send('Hello, server')
	data = mySocket.recv(buf_size)
	print data
	time.sleep(5)

	mySocket.close()

client()
