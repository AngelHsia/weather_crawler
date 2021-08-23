import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

hour = int(datetime.now().strftime('%H')) # current time (hour only)

# (not very important) these data provide web server with our device information. (though some website may check this part)
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'

CRAWL_URL = 'https://www.cwb.gov.tw/V8/C/W/Town/MOD/3hr/6800500_3hr_PC.html'

session = requests.Session()
session.headers = {'user-agent' : USER_AGENT}

req = session.get(CRAWL_URL)
soup = BeautifulSoup(req.text, 'html.parser')
temps = soup.find_all("span", class_="tem-C is-active")
temperature = temps[17].text # data type: string
#print(temperature)

url = "http://api.thingspeak.com/update?api_key=2BG7NSL1HYBXHD1K&field1=%s" % temperature
req = urlopen(url)