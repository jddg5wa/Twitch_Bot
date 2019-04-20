import string
import os
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import *

users = ["gingerbreadybot"]

def run():
	s = openSocket()
	userListFile = open("userlist.txt", "w")
	joinRoom(s)
	readbuffer = ""

	while True:
		readbuffer = readbuffer + s.recv(1024).decode()
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			if "PING" in line:
				s.send((line.replace("PING", "PONG")+ "\r\n").encode("utf-8"))
				break

			user = getUser(line)
			message = getMessage(line)
			print (user + " typed :" + message)

			#Greet New User
			if isUserNew(user):
				welcomeNewUser(s,user)
				users.append(user)
				userListFile.write(user + " ")
				print(users)

			# reply(message, user)

def loadUserList():
	users = [line.split(" ") for line in userListFiles.readLines()]
	print(users)


def isUserNew(user):
	if (user not in users):
		return True

def welcomeNewUser(socket, user):
    print ("greeted " + user)
    sendMessage(socket, "@" + user + " " + welcomeMessage)

run()

