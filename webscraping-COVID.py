# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)

from colorsys import hls_to_rgb
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import certifi
import ssl


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers= headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tablerows = soup.findAll('tr')

swd = ''
sbd = ''
hdr =  0.0
ldr = 100.0

sbt = ''
swt = ''
htr = 0.0
ltr = 100.0

for row in tablerows[2:52]:
    td = row.findAll('td')
    state = td[1].text
    total_cases = int(td[2].text.replace(',',''))
    total_deaths = int(td[4].text.replace(',',''))
    total_tests = int(td[10].text.replace(',',''))
    population = int(td[12].text.replace(',',''))

    death_rate = round((total_deaths / total_cases) * 100, 2)
    test_rate = round((total_tests / population) * 100, 2)

    if death_rate > hdr:
        swd = state
        hdr = death_rate

    if death_rate < ldr:
        sbd = state
        ldr = death_rate


    if test_rate > htr:
        swt = state
        htr = test_rate

    if test_rate < ltr:
        sbt = state
        ltr = test_rate

print(f'State with the worst death rate: {swd}')
print(f'Death rate: {hdr}%')
print()
print()
print(f'State with the best death rate: {sbd}')
print(f'Death rate: {ldr}%')
print()
print()

print(f'State with the worst test rate: {swt}')
print(f'Test rate: {ltr}%')
print()
print()
print(f'State with the best test rate: {sbt}')
print(f'Test rate: {htr}%')
print()
print()


    #print(f'State: {state}')
    #print(f'Total Cases: {total_cases}')
    #print(f'Total Deaths: {total_deaths}')
    #print(f'Total Tests: {total_tests}')
    #print(f'Population: {population}')
    #print()
    #print()



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

