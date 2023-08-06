import json

from os import error
from stockly_python.client import Client
from stockly_python.messageEmbed import messageEmbed

myClient = Client()





@myClient.ee.on("open")
def on_open():
    print("Bot Connection Is Open")


@myClient.ee.on("command")
def command(data):
    myMessage = messageEmbed()
    myMessage.setColor('#0099ff')
    myMessage.setTitle('Some title')
    myMessage.setURL('https://discord.js.org/')
    myMessage.setAuthor('Some name', 'https://i.imgur.com/AfFp7pu.png', 'https://discord.js.org')
    myMessage.setDescription('Some description here')
    myMessage.setThumbnail('https://i.imgur.com/AfFp7pu.png')
    myMessage.setImage('https://i.imgur.com/AfFp7pu.png')
    myMessage.setTimestamp()    
    myMessage.setFooter('Some footer text here', 'https://i.imgur.com/AfFp7pu.png')
    print("Get Command From Mobile", data, type(myMessage))
    myClient.sendMessage(data['roomId'], 'hello i am from python')
    myClient.sendMessage(data['roomId'], myMessage)

    # myClient.sendSms(data['userId'], 'hello i am from python')
    # myClient.sendMessage(data['roomId'], 'hello i am from python')
    # myClient.sendMessage(data['roomId'], 'hello i am from python')

# @myClient.ee.on("setting")
# def setting(data):
#     print("setting", data)


@myClient.ee.on("error")
def setting(err):
    print("Bot get Socket error", err)


@myClient.ee.on("close")
def close():
    print("Bot Connection Is Close")

# myClient.sendMessage('qvtF5LdE01622750386728', 'hello i am from python')
# myClient.sendSms('MtZtrcTTz1622724929084', 'hello i am from python')
# myClient.sendPushNotification('qvtF5LdE01622750386728', 'hello i am from python')
# myClient.sendEmail('MtZtrcTTz1622724929084', 'test', '<h1>TEST</h1>')


myClient.login('N0f9qIa1640586773849a6805a7e989a', '237592481216856171')
