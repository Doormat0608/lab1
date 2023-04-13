import requests
from bs4 import BeautifulSoup


def parse(url):
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    faculties = []
    for button in soup.find_all('a', class_='sidebar-menu__link'):
        faculties.append(button.text)
    return faculties


def wtf(data, filename):
    with open(filename, 'w') as f:
        for item in data:
            f.write("%s\n" % item)
