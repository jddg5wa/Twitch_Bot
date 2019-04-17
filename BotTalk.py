import string
import random
from Socket import openSocket, sendMessage
from Settings import welcomeMessage

s = openSocket()
userGreetings = ["hello", "hi","sup", "hey"]

def reply(message, user):
    userMessage = message.lower()

    #Check if message is greeting.
    for string in userGreetings:
        # print (string + " @gingerbreadybot")
        # print ("user = " + userMessage)
        if (string + " @gingerbreadybot") in userMessage:
            # print ("TRUE")
            replyToGreeting(userMessage)
            break

def replyToGreeting(message):
    botGreetings = ["Hey",
                    "Hey!", 
                    "Hi", 
                    "Hello", 
                    "Sup!",
                    "Sup", 
                    "Whats up?"
                    "Hi, how are you?", 
                    "Hey, how are you doing?", 
                    "Hello, how you doin?",]
    reply = random.choice(botGreetings)
    sendMessage(s, reply)


def welcomeNewUser(user):
    print ("greeting " + user)
    sendMessage(s, "@" + user + " " + welcomeMessage)

# def welcomeOldUser(message, user):

