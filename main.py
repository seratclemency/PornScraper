import requests
import wget
from bs4 import BeautifulSoup


choice = int(input('С какого сайта вы хотите скачать фото (erogif, hentaicity, eroticaxxx - 1, paheal - 2): '))

def parse():
    directory = input('Введите путь до папки: ')
    cleared_directory = directory.replace('"', '')
    query = input('Введите ссылку на пост: ')
    responce = requests.get(query)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        image = image.get('src')
        try:
            wget.download(image, cleared_directory)
        except Exception:
            pass

def parse_rule34_paheal():
    directory = input('Введите путь до папки: ')
    cleared_directory = directory.replace('"', '')
    query = input('Введите ссылку на страницу paheal: ')
    responce = requests.get(query)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('a')
    for image in images:
        image = image.get('href')
        try:
            if 'https://lotus.paheal.net/_images/' in image and '.mp4' not in image:
                wget.download(image, cleared_directory)
            elif 'https://tulip.paheal.net/_images/' in image and '.mp4' not in image:
                wget.download(image, cleared_directory)
        except Exception:
            pass

if choice == 1:
    parse()
elif choice == 2:
    parse_rule34_paheal()