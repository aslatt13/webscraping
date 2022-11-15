
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

###

tables = soup.findAll('table')
table = tables[0]
rows = table.findAll('tr')
 
for row in rows[1:6]:
    td = row.findAll('td')
    rank = int(td[0].text)
    title = (td[1].text)
    gross = int(td[5].text.replace(',','').replace('$',''))
    studio = td[9].text.replace(',','').replace('$','')
    theatre = int(td[6].text.replace(',',''))
    avggross = gross / theatre

    print(f'Rank: {rank}')
    print(f'Title: {title}')
    print(f'Gross: ${gross:,.2f}')
    print(f'Studio: {studio}',end='')
    print(f'Avg Gross per Theatre: ${avggross:,.2f}')
    print()
    print('#####')



