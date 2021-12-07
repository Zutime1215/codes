from bs4 import BeautifulSoup
import requests

def get_link(soup):
   link3 = ''

   for link in soup.find_all('a'):
      link1 = link.get('href')

      if isinstance(link1, str):
         link2 = link1

         if "/lsp/download_file.php?" in link2:
            link3 = link2

   return link3   

def download(var, link3):
   finalink = "https://lmms.io" + link3
   name1 = finalink.replace(f"https://lmms.io/lsp/download_file.php?file={var}&name=", "")
   name2 = name1.replace("+", " ")

   if name2.endswith(".wav"):
      filess = requests.get(finalink)
      print("downloading--> " + name2)
      with open(f'samples/{name2}', 'wb') as f:
          f.write(filess.content)

   elif name2.endswith(".ogg"):
      filess = requests.get(finalink)
      print("downloading--> " + name2)
      with open(f'samples/{name2}', 'wb') as f:
          f.write(filess.content)

   elif name2.endswith(".mmpz"):
      filess = requests.get(finalink)
      print("downloading--> " + name2)
      with open(f'projects/{name2}', 'wb') as f:
          f.write(filess.content)

   elif name2.endswith(".mmp"):
      filess = requests.get(finalink)
      print("downloading--> " + name2)
      with open(f'projects/{name2}', 'wb') as f:
          f.write(filess.content)

   elif name2.endswith(".xpf"):
      filess = requests.get(finalink)
      print("downloading--> " + name2)
      with open(f'presets/{name2}', 'wb') as f:
          f.write(filess.content) 

   else:
      filess = requests.get(finalink)
      print("downloading--> " + name2)
      with open(f'others/{name2}', 'wb') as f:
          f.write(filess.content)                               


def main():
   for var in range(20001, 23001):
      html_text = requests.get(f'https://lmms.io/lsp/?action=show&file={var}').text
      soup = BeautifulSoup(html_text, 'lxml')
      # print(soup)

      link3 = get_link(soup)
      print(f'{var} : ')

      if link3 != '':
         download(var, link3)


main()