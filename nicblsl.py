import bs4
import requests
from bs4 import BeautifulSoup


re = requests.get('http://nepalstock.com.np/marketdepthofcompany/2887')
soup = bs4.BeautifulSoup(re.text, "lxml")
Position=soup.find('label',{"class":"livePrice"}).text.strip()
print(Position)

if Position == '759.00':
    print("not changed")
