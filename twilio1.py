import keys2

from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TNum = '+14847465299'

myCell = '+19137447034'

textmsg = client.messages.create(to=myCell,from_=TNum,
            body='Hi there!')

print(textmsg.status)

call = Client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                            to=myCell,from_=TNum)
