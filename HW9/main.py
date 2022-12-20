import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.anekdot.ru/'

response = requests.get(url).text
txt = bs(response, 'html.parser')

txt = txt.find("div", "topicbox")
txt = txt.find("div", "text")

print(txt)

