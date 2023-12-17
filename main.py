# Испортируем нужные библиотеки
import customtkinter
from bs4 import BeautifulSoup
import tkinter
import wget
import requests
import threading
import os
import time

'''
Функция для показа прогресса скачивания в реальном времени
'''
def bar_progress(current, total, width=80):
    text_box.insert('0.0', '\nСкачивание: %d%% [%d / %d] битов\n' % (current / total * 100, current, total))

'''
Функция для скачивания фоток с erogif.ru
'''
def parse_erogif():
    if not os.path.exists(r'C:\out'): # Если дириктории не существует, то создаём её
        os.mkdir(r'C:\out')
    user_input = textfield.get() # Получаем ввод пользователя
    responce = requests.get(user_input) # Отправляем запрос на ту сссылку которую дал пользователь
    html = responce.text # Преобразовываем в текст полученную страницу
    soup = BeautifulSoup(html, 'html.parser') # Объявляем объект BeautifulSoup4
    images = soup.find_all('img') # Ищем тег
    list_of_images = [] # Пустой лист
    for image in images:
        image = image.get('src') # Получаем ссылки
        list_of_images.append(image) # Добавляем ссылки в массив
    num_of_images.configure(text='Насчитано ' + str(len(list_of_images)) + ' фотографий по заданной ссылке.') # Считаем сколько ссылок в листе и выводим сообщение с цифрой
    time.sleep(1) # Спать 1 секунду
    textfield.delete(0, 500) # Удаляем все символы из textfield
    textfield.insert(0, 'Скачивание началось. Посмотрите папку out.') # Добавляем новую надпись
    num_of_image = 1
    for image in images:
        image = image.get('src') # Получаем ссылки и скачиваем их
        try:
            text_box.insert('0.0', '\nФАЙЛ НОМЕР {} СКАЧИВАЕТСЯ\n'.format(num_of_image))
            num_of_image += 1
            wget.download(image, r'C:\out', bar=bar_progress)
        except Exception:
            pass
    text_box.insert('0.0', '\nСКАЧИВАНИЕ ЗАВЕРШЕНО.\n')


'''
Функция для скачивания фоток с pahel
'''
def parse_rule34_paheal():
    if not os.path.exists(r'C:\out'):
        os.mkdir(r'C:\out')
    user_input = paheal_textfield.get()
    responce = requests.get(user_input)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('a')
    list_of_images = []
    for image in images:
        image = image.get('href')
        try:
            if 'https://lotus.paheal.net/_images/' in image and '.mp4' not in image:
                list_of_images.append(image)
            elif 'https://tulip.paheal.net/_images/' in image and '.mp4' not in image:
                list_of_images.append(image)
        except Exception:
            pass
    num_of_images.configure(text='Насчитано ' + str(len(list_of_images)) + ' фотографий по заданной ссылке.')
    time.sleep(1)
    paheal_textfield.delete(0, 500)
    paheal_textfield.insert(0, 'Скачивание началось. Посмотрите папку out.')
    num_of_image = 1
    for image in images:
        image = image.get('href')
        try:
            if 'https://lotus.paheal.net/_images/' in image and '.mp4' not in image:
                text_box.insert('0.0', '\nФАЙЛ НОМЕР {} СКАЧИВАЕТСЯ\n'.format(num_of_image))
                num_of_image += 1
                wget.download(image, r'C:\out', bar=bar_progress)
            elif 'https://tulip.paheal.net/_images/' in image and '.mp4' not in image:
                text_box.insert('0.0', '\nФАЙЛ НОМЕР {} СКАЧИВАЕТСЯ\n'.format(num_of_image))
                num_of_image += 1
                wget.download(image, r'C:\out', bar=bar_progress)
        except Exception:
            pass
    text_box.insert('0.0', '\nСКАЧИВАНИЕ ЗАВЕРШЕНО.\n')

'''
Функция для скачивания фоток с hentaicity
'''
def parse_hentaicity():
    if not os.path.exists(r'C:\out'):
        os.mkdir(r'C:\out')
    user_input = hentaicity_textfield.get()
    responce = requests.get(user_input)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    list_of_images = []
    for image in images:
        image = image.get('src')
        cleared_image = image.replace('-t', '')
        list_of_images.append(cleared_image)
    num_of_images.configure(text='Насчитано ' + str(len(list_of_images)) + ' фотографий по заданной ссылке.')
    time.sleep(1)
    hentaicity_textfield.delete(0, 500)
    hentaicity_textfield.insert(0, 'Скачивание началось. Посмотрите папку out.')
    num_of_image = 1
    for image in images:
        image = image.get('src')
        cleared_image = image.replace('-t', '')
        text_box.insert('0.0', '\nФАЙЛ НОМЕР {} СКАЧИВАЕТСЯ\n'.format(num_of_image))
        num_of_image += 1
        wget.download(cleared_image, r'C:\out', bar=bar_progress)
    text_box.insert('0.0', '\nСКАЧИВАНИЕ ЗАВЕРШЕНО.\n')

'''
Запуск функций в новом потоке дабы интерфейс не лагал
'''
def start_parse():
    threading.Thread(target=parse_erogif, daemon=True).start()

def start_parse_paheal():
    threading.Thread(target=parse_rule34_paheal, daemon=True).start()

def start_parse_hentaicity():
    threading.Thread(target=parse_hentaicity, daemon=True).start()

'''
Здесь написан код отвечающий за окно, кнопки, надписи, расположения кнопок и надписей
'''
customtkinter.set_appearance_mode('dark') # Тема приложения
customtkinter.set_default_color_theme('green') # Цветовой акцент приложения

window = customtkinter.CTk() # Создание окна приложения, является самым главным объектом
window.geometry('1500x1500') # Установка размеров окна
window.title('PornScraper') # Установка названия окна

text_box = customtkinter.CTkTextbox(window, width=500, height=500) # Textbox
num_of_images = customtkinter.CTkLabel(master=window, text='', font=('Time 30', 20)) # Пустая надпись для обновления в реальном времени
pornscraper_label = customtkinter.CTkLabel(master=window, text='PornScraper by serat', font=('Time 30', 20)) # Надпись PornScraper
erogif_label = customtkinter.CTkLabel(master=window, text='Введите erogif ссылку ниже и нажмите на кнопку:', font=('Time 30', 15)) # Надпись erogif
hentaicity_label = customtkinter.CTkLabel(master=window, text='Введите hentaicity ссылку ниже и нажмите на кнопку:', font=('Time 30', 15)) # Надпись hentaicity
paheal_label = customtkinter.CTkLabel(master=window, text='Введите paheal ссылку ниже и нажмите на кнопку:', font=('Time 30', 15)) # Надпись paheal
parse_button = customtkinter.CTkButton(master=window, text='Парсить', command=start_parse) # Кнопка для начала парсинга erogif
parse_paheal_button = customtkinter.CTkButton(master=window, text='Парсить', command=start_parse_paheal) # Кнопка для начала парсинга paheal
parse_hentaicity_button = customtkinter.CTkButton(master=window, text='Парсить', command=start_parse_hentaicity) # Кнопка для начала парсинга hentaicity
textfield = customtkinter.CTkEntry(master=window, width=300) # Поле ввода для erogif
paheal_textfield = customtkinter.CTkEntry(master=window, width=300) # Поле ввода для paheal
hentaicity_textfield = customtkinter.CTkEntry(master=window, width=300) # Поле ввода для hentaicity

'''
Добавление кнопок/надписей на макет с фиксированными позициями
'''
num_of_images.place(x=10, y=10)
pornscraper_label.place(x=900, y=10)
erogif_label.place(x=900, y=60)
textfield.place(x=900, y=110)
parse_button.place(x=900, y=190)
paheal_label.place(x=900, y=250)
paheal_textfield.place(x=900, y=300)
parse_paheal_button.place(x=900, y=380)
hentaicity_label.place(x=900, y=440)
hentaicity_textfield.place(x=900, y=490)
parse_hentaicity_button.place(x=900, y=570)
text_box.place(x=10, y=100)

window.mainloop() # Запуск приложения