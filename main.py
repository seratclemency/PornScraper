import requests
import wget
from bs4 import BeautifulSoup


choice = int(input('С какого сайта вы хотите скачать фото (erogif, hentaicity, eroticaxxx - 1, paheal - 2): '))
  
def bar_progress(current, total, width=80):
    print("Скачивание: %d%% [%d / %d] битов" % (current / total * 100, current, total))

def parse():
    directory = input('Введите путь до папки: ')
    cleared_directory = directory.replace('"', '')
    query = input('Введите ссылку на пост: ')
    responce = requests.get(query)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    num_of_images = 1
    for image in images:
        image = image.get('src')
        try:
            print('Файл номер {} скачивается'.format(num_of_images))
            num_of_images += 1
            wget.download(image, cleared_directory, bar=bar_progress)
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
    num_of_images = 1
    for image in images:
        image = image.get('href')
        try:
            if 'https://lotus.paheal.net/_images/' in image and '.mp4' not in image:
                print('Файл номер {} скачивается'.format(num_of_images))
                num_of_images += 1
                wget.download(image, cleared_directory, bar=bar_progress)
            elif 'https://tulip.paheal.net/_images/' in image and '.mp4' not in image:
                print('Файл номер {} скачивается'.format(num_of_images))
                num_of_images += 1
                wget.download(image, cleared_directory, bar=bar_progress)
        except Exception:
            pass

if choice == 1:
    parse()
elif choice == 2:
    parse_rule34_paheal()