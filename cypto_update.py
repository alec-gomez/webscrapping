from unicodedata import name
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client




url = 'https://cryptoslate.com/coins/'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)
print('Ranked by Market Capitalization')
print()

coin_row = soup.findAll('tr')

accountSID = 'ACb0363a92e2e44614b28aa80526632631' 

authToken = 'b7847120b869111aacfae08df804803f' 

Client = Client(accountSID, authToken)

TwilioNumber = '+15077107744'

mycellphone = '+18323169536' 

for row in coin_row[1:6]:
    td = row.findAll('td')

    name = td[2].text
    print('Name and Symbol:',name)

    price = td[4].text
    print('Current Price:',price)
    price = float(td[4].text.replace(',','').replace('$',''))
    
    change = td[5].text
    print('Percent Change in Price over the last 24 hours:',change)
    change = float(td[5].text.replace('','').replace('+','').replace('%',''))
    change = 1 + (change/100)
    #print(change)

    dchange = price/change
    #print(dchange)
    
    mon = float(price - dchange)

    poneg = 'increase'
    if mon > 0:
        poneg = 'increase'
    else:
        poneg = 'decrease'
    
    print('The Price 24 hours ago was:',"${:,.4f}". format(dchange))

    mon = "${:,.4f}". format(mon)

    print('Price Amount Change in last 24 hours:',mon, poneg)

    print('')
    
    if str(td[2].text) == 'Bitcoin BTC ':
        if price <  40000:
            textmessage = Client.messages.create(to=mycellphone, from_=TwilioNumber, body="BTC price is below $40,000!")

            #print(textmessage.status)

    if str(td[2].text) == 'Ethereum ETH ':
        if price < 3000:
            textmessage = Client.messages.create(to=mycellphone, from_=TwilioNumber, body="ETH price is below $3,000!")
            #print(textmessage.status)


#Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope process .\.venv\Scripts\activate
