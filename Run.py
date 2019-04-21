import string
import os
import datetime
import time
import argparse
import json
import pickle
import requests
import random
from urllib.request import *
from urllib.error import *
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import *

start = time.time()
uptime = 0
s = openSocket()


class Stream:
	uptime = 0
	users = []

	def __init__(self, name, title, category):
		self.name = name
		self.title = title
		self.category = category

	def getUptime(self):
		if hasattr(self, "startTime"):
			print (self.startTime)
			print (time.time())
			print (time.time() - self.startTime)
			uptime = str(datetime.timedelta(0, time.time() - self.startTime))
			return uptime[2:-7]
		else:
			return None

	def getStartTime(self):
		setattr(self, "startTime", time.time())

class User:
	def __init__(self, name):
		self.name = name
		self.firstSeen = datetime.datetime.now()

	def userSpotted(self):
		setattr(self, "lastSeen", datetime.datetime.now())

	def getFirstSeen(self):
		return self.firstSeen.strftime("%m/%d/%Y, %H:%M:%S")

	def getLastSeen(self):
		return self.lastSeen.strftime("%m/%d/%Y, %H:%M:%S")

streamDataFile = "W:/Clients/Joe Gutman/Streaming/Bot/streamDataFile.txt"
users = []

def run():
	# print(users)
	joinRoom(s)
	readbuffer = ""

	print (stream.getUptime())

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
			message = getMessage(line).lower()
			print (user + " typed : " + message)

			
			if user != "gingerbreadybot":
				if getUserObject(user) != None:
					getUserObject(user).userSpotted()

				#Greet New User
				if isUserNew(user):
					print("NEW USER? " + user)
					welcomeNewUser(s,user)
					saveUser(user, streamDataFile)	

				if message[0] == "!":
					if len(message) > 1:
						botCommands(message) 

				if "@gingerbreadybot" in message:
					reply(message, user)

# def getStreamInfo():
# 	htmlContent = requests.get('http://api.justin.tv/api/stream/list.json?channel=' + CHANNEL).json()
# 	print(htmlContent)

def loadUserList(file):
	global users
	if os.path.getsize(streamDataFile) > 0:
		with open(file, "rb") as usersFile:
			users = pickle.load(usersFile)
			# print(users)
			# str = "LOADED USERS: "
			# for each in users:
			# 	str += each.name + " "
			# print(str)
			return users

def saveUser(user, file):
	users.append(User(user))
	with open(file, "wb") as usersFile:
		pickle.dump(users, usersFile)

def isUserNew(user):
	if getUserObject(user) != None:
		return False
	return True

def getUserObject(user):
	for u in users:
		if u.name == user:
			return u

def welcomeNewUser(socket, user):
    print ("greeted " + user)
    sendMessage(socket, "@" + user + " " + welcomeMessage)


def reply(message, user):
	botReplies = ["no you", 
				  "what are you even saying", 
				  "aw, how sweet", 
				  "you're the best", 
				  "wut", 
				  "What about me?", 
				  "What did you say to me? I'll have you know I graduated...", 
				  "uwu", 
				  "oowoo", 
				  "owo", 
				  "WutFace", 
				  "CorgiDerp",
				  "LUL",
				  "TwitchUnity",
				  "KonCha",
				  "MrDestructoid",
				  "CoolCat"]
	reply = random.choice(botReplies)
	sendMessage(s, reply)

def botCommands(command):
	newCommand = command.split()
	print("BOT COMMAND: " + newCommand[0][1:])
	if newCommand[0][1:] == "uptime":
		uptime()
	if newCommand[0][1:] == "lastseen":
		lastSeen(getUserObject(newCommand[1]))
	if newCommand[0][1:] == "firstseen":
		firstSeen(getUserObject(newCommand[1]))

def uptime():
	uptime = stream.getUptime()
	if stream.getUptime() != None:
		sendMessage(s, "Stream Uptime is " + stream.getUptime())
	else:
		sendMessage(s, "Stream is OFFLINE")

def firstSeen(user):
	sendMessage(s, user.name + " first seen " + user.getFirstSeen())

def lastSeen(user):
	sendMessage(s, user.name + " last seen " + user.getLastSeen())

# getStreamInfo()
loadUserList(streamDataFile)
stream = Stream("gingerbreadyman", "test", "test")
run()

