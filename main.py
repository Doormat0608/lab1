import requests
from bs4 import BeautifulSoup

url = 'https://omgtu.ru/general_information/faculties/'

page = requests.get(url).content

soup = BeautifulSoup(page, 'html.parser')

with open('faculties.txt', 'w') as f:
    for button in soup.find_all('a', class_='sidebar-menu__link'):
        f.write(button.text + '\n')
        print(button.text)
