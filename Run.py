import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024).decode()
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG").encode())
				break

			user = getUser(line)
			message = getMessage(line)
			print (user + " typed :" + message)
			
			if "hi" in message.lower():
				sendMessage(s, "hi")
				break