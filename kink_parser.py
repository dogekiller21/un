import requests
from bs4 import BeautifulSoup
import csv

CSV = 'kink.csv'
# HOST = 'https://kinkstore.ru/'
URL = 'https://kinkstore.ru/search/?module=search'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

def content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='shop-item')
    mass = []
    for item in items:
        mass.append(
            {
                'title':item.find('h5', class_='catalogCardTitle').find('a', class_='shop-item-title').get_text(strip=True),
                'price':item.find('div', class_='price').find('span').get_text(strip=True),
                'link':item.find('h5', class_='catalogCardTitle').find('a').get('href')
            }
        )
    return mass

def save(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название товара', 'Цена товара', 'Ссылка на товар'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['link']])

def parser():
    search = str(input('Укажите запрос: ').strip())
    html = get_html(URL)
    if html.status_code == 200:
        mass = []
        print(f'Парсим ваш запрос {search}...')
        html = get_html(URL, params={'searchword': search})
        mass.extend(content(html.text))
        l = len(mass)
        print(f'Парсинг закончился, получено {l} результатов')
        save(mass, CSV)
    else:
        print('Error')

parser()