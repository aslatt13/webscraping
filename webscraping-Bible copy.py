import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

webpage = 'https://biblehub.com/asv/john/'

randomch = random.randint(1,21)
randomch = str(randomch)

end = randomch + '.htm'
link = webpage + end

print(link)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(link, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
verses = soup.findAll('p', class_='reg')

print(verses)

for verse in verses:
    vlist = verse.text.split('.')
    #print(vlist)

myverse = random.choice(vlist[:-5])

print(f'Chapter : {randomch}, Verse: {myverse}')

message = 'Chapter: ' + randomch + ' Verse:' + myverse

print(message)

import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)
TNum = '+14847465299'
myCell = '+19137447034'

txtmsg = client.messages.create(to=myCell,from_=TNum,body=message)
print(txtmsg.status)
