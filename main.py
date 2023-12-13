import customtkinter
from bs4 import BeautifulSoup
import tkinter
import wget
import requests
import threading
import os

def parse():
    if not os.path.exists(r'C:\out'):
        os.mkdir(r'C:\out')
    user_input = textfield.get()
    textfield.delete(0, 50)
    textfield.insert(0, 'Скачивание началось. Посмотрите папку out.')
    responce = requests.get(user_input)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        image = image.get('src')
        try:
            wget.download(image, r'C:\out')
        except Exception:
            pass

def parse_rule34_paheal():
    if not os.path.exists(r'C:\out'):
        os.mkdir(r'C:\out')
    user_input = paheal_textfield.get()
    paheal_textfield.delete(0, 50)
    paheal_textfield.insert(0, 'Скачивание началось. Посмотрите папку out.')
    responce = requests.get(user_input)
    html = responce.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('a')
    for image in images:
        image = image.get('href')
        try:
            if 'https://lotus.paheal.net/_images/' in image and '.mp4' not in image:
                wget.download(image, r'C:\out')
            elif 'https://tulip.paheal.net/_images/' in image and '.mp4' not in image:
                wget.download(image, r'C:\out')
        except Exception:
            pass

def start_parse():
    threading.Thread(target=parse, daemon=True).start()

def start_parse_paheal():
    threading.Thread(target=parse_rule34_paheal, daemon=True).start()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

window = customtkinter.CTk()
window.geometry('800x800')
window.title('PornScraper')

pornscraper_label = customtkinter.CTkLabel(master=window, text='PornScraper by serat', font=('Time 30', 20))
non_paheal_label = customtkinter.CTkLabel(master=window, text='Введите ссылку ниже и нажмите на кнопку:', font=('Time 30', 15))
paheal_label = customtkinter.CTkLabel(master=window, text='Введите paheal ссылку ниже и нажмите на кнопку:', font=('Time 30', 15))
parse_button = customtkinter.CTkButton(master=window, text='Парсить', command=start_parse)
parse_paheal_button = customtkinter.CTkButton(master=window, text='Парсить', command=start_parse_paheal)
textfield = customtkinter.CTkEntry(master=window, width=300)
paheal_textfield = customtkinter.CTkEntry(master=window, width=300)

pornscraper_label.pack(pady=50)
non_paheal_label.pack()
textfield.pack(pady=20)
parse_button.pack(pady=50)
paheal_label.pack()
paheal_textfield.pack(pady=20)
parse_paheal_button.pack(pady=50)

window.mainloop()