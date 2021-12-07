from bs4 import BeautifulSoup
import requests

headers = {
    'authority': 'techshopbd.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'origin': 'https://techshopbd.com',
    'upgrade-insecure-requests': '1',
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://techshopbd.com/login',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_ga=GA1.2.3151448.1635788296; __tawkuuid=e::techshopbd.com::/YVeDj9FQVx4r2Y8P9C17KvYABNnuyOdX5+B8nph2BzDhhlIv+Vh4u+waIVPHk1P::2; recentlyViewedProducts=56#157#68#1534#3083#3434#1845#3451; _gid=GA1.2.1395063237.1637905597; JSESSIONID=1432C5732847C6F4B5374632868BF7C6; _gat_gtag_UA_40929689_5=1; TawkConnectionTime=0',
}

data = {
  
  '_csrf': 'new_csrf',
  'username': 'salehinrifat@hotmail.com',
  'password': 'qazwsxedcd',
  '_csrf': 'new_csrf'
  
}

with requests.session() as ss:
    url = 'https://techshopbd.com/login'
    r = ss.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')
    data['new_csrf'] = soup.find('input', attrs={'name': '_csrf'})['value']
    # abcd = soup.find('input', attrs={'name': '_csrf'})['value']
    # print(abcd)

    ss.post(url, headers=headers, data=data)
    
    r = ss.get('https://techshopbd.com/my-section/my-profile')
    print(r.content)









 