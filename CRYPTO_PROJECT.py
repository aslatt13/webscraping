from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)
TNum = '+14847465299'
myCell = '+19137447034'

### Find a 'scrappable' cryptocurrencies website where you can scrape the 
# top 5 cryptocurrencies and display as a formatted 
# output one currency at a time. 
# The output should display the:
# name of the currency
# the symbol (if applicable)
# the current price
# % change in the last 24 hrs and corresponding price (based on % change)
#
# Furthermore, for Bitcoin and Ethereum, the program should alert you via 
# text if the value falls below $40,000 for BTC and $3,000 for ETH.


url = 'https://crypto.com/price'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers= headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

row = soup.findAll('tr')

num = 0
for i in row[1:6]:
    cell = i.findAll('td')
    ptag = i.findAll('p')
    divtag = cell[3].findAll('div')
    num += 1

    name = ptag[0].text
    symbol = cell[2].text
    symbol = symbol.replace(name, '')
    
    if symbol == '':
        symbol = name

    price = divtag[0].text
    change = cell[4].text
    price = price.replace(change, '')

    print(f'Number: {num}')
    print(f'Name: {name} ')
    print(f'Symbol: {symbol} ')
    print(f'Price: {price}')
    print(f'% Change 24hr: {change}')
    print()

    if symbol == 'BTC':
        if float(price.replace('$', '').replace(',', '')) < 40000:
            message = client.messages.create(to= myCell, from_= TNum, body= 'BTC is below $40,000. \nCurent price: ' + price)

    if symbol == 'ETH':
        if float(price.replace('$', '').replace(',', '')) < 3000:
            message = client.messages.create(to= myCell, from_= TNum, body= 'ETH is below $3,000. \nCurrent price: ' + price)




