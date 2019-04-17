import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from BotTalk import *

# class Stream:
# 	viewers = ()
# 	oldViewers = ()

# class Viewer:
# 	joinDate = 0

# 	def checkToWelcome():

def run():
	s = openSocket()
	joinRoom(s)
	readbuffer = ""

	users = ["gingerbreadybot"]

	while True:
		readbuffer = readbuffer + s.recv(1024).decode()
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		
		for line in temp:
			# print(line)
			if "PING" in line:
				s.send((line.replace("PING", "PONG")+ "\r\n").encode("utf-8"))
				break

			user = getUser(line)
			message = getMessage(line)
			print (user + " typed :" + message)

			if user not in users:

				welcomeNewUser(user)
				users.append(user)
				print (users)
			
			reply(message, user)

run()