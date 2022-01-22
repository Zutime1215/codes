from bs4 import BeautifulSoup
import requests
import json

with open("apis.txt", "r") as apis:
  for lines in apis:
    var = lines

    html_text = requests.get(f'https://api.redx.com.bd/parcel-track/2111A4THAFO{var}').text
    soup = BeautifulSoup(html_text, 'lxml')
    name = soup.find('p').text
    
    print(name)
