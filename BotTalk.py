import string
import random
from Socket import openSocket, sendMessage
from Settings import welcomeMessage

s = openSocket()
userGreetings = ["hello", "hi","sup", "hey", "hewwo", "bitch", "bithc", "owo"]
userCompliments = ["nice", "good"]

botReplies = ["no you", "what are you even saying", "aw, how sweet", "you're the best", "wut", "What about me?", "What did you say to me? I'll have you know I graduated...", "uwu", "oowoo", "owo", "WutFace", "CorgiDerp"]

def reply(message, user):
    userMessage = message.lower()

    if ("@gingerbreadybot" in userMessage):
        reply = random.choice(botReplies)
        sendMessage(s, reply)


    # #Check if message is greeting.
    # for string in userGreetings:
    #     # print (string + " @gingerbreadybot")
    #     # print ("user = " + userMessage)
    #     if (string in userMessage and "@gingerbreadybot" in userMessage):
    #         # print ("TRUE")
    #         replyToGreeting(userMessage)
    #         break
    
    # #Check if message is greeting.
    # for string in compliments:
    #     # print (string + " @gingerbreadybot")
    #     # print ("user = " + userMessage)
    #     if (string in userMessage and "@gingerbreadybot" in userMessage):
    #         # print ("TRUE")
    #         replyToGreeting(userMessage)
    #         break

def replyToGreeting(message):
    botGreetings = ["Hey",
                    "Hey!", 
                    "Hi", 
                    "Hello", 
                    "Sup!",
                    "Sup", 
                    "Whats up?",
                    "Hi, how are you?", 
                    "Hey, how are you doing?", 
                    "Hello, how you doin?",]
    reply = random.choice(botGreetings)
    sendMessage(s, reply)


def welcomeNewUser(user):
    print ("greeting " + user)
    sendMessage(s, "@" + user + " " + welcomeMessage)

# def welcomeOldUser(message, user):

