#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string


# Preset values:
accountSID = 'AC076e8901facea8276713211a58129707'
authToken = '3eb8cd89a72450c18d8a4a11418459d5'
myTwilioNumber = '+4083349'
myCellPhone = '+6527598'


from twilio.rest import Client


def textmyself(message):
   twilioCli = Client(accountSID, authToken)
   twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
   
