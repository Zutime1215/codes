from bs4 import BeautifulSoup
import requests
import json

with open("apis.txt", "r") as apis:
  for lines in apis:
    var = lines

    html_text = requests.get(f'https://api.redx.com.bd/parcel-track/2111A4THAFO{var}').text
    soup = BeautifulSoup(html_text, 'lxml')
    name = soup.find('p').text
 
    data = json.loads(name)

    info = data["parcel"]

    purify_info = json.dumps(info, indent=2, sort_keys=True) + '\n\n'

    with open("results.txt", "a") as result:
      result.write(purify_info)

print("Writing is complete")