from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.delfi.lt/news/daily/world/karas-ukrainoje-rusu-ziniasklaida-ukrainoje-suciuptiems-britams-ir-marokieciui-mirties-bausme.d?id=90439595').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('p')
blokai = blokai[1:8]

for blokas in blokai:
    print(blokas.text.strip())

# print(blokas[:8])