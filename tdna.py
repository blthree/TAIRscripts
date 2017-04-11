import requests
from bs4 import BeautifulSoup
stock_num = 'SALK_105078'
base_url = 'http://www.arabidopsis.org/servlets/StockSearcher?action=detail&stock_number='

r = requests.get(base_url + stock_num)
soup = BeautifulSoup(r.text, 'html.parser')
all_links = soup.find_all('a')
for tag in all_links:
    link_url = tag.get('href')
    if link_url is not None and 'polyallele' in link_url and 'TairObject' in link_url:
        poly_link = link_url
        poly_name = tag.text
print(poly_link, poly_name)
