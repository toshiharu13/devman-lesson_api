# Счетчик кликов

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

## Техническое описание
ПО предназанчено для конвертирования ссылок в короткие, а если предоставлена короткая ссылка, отражает количество кликов по ней.
Ссылку необходимо вводить полную.

## Системные требования
- [Python 3](https://www.python.org/)
- Linux OS

##  Установка
Для установки дастоточно:

Cклонировать проект

    $ https://github.com/toshiharu13/django-orm-watching-storage.git

Установить requirements.txt

      $ pip install -r requirements.txt

 - Сгенерировать токен на bitly.com
 - Создать в проекте файл .env и записать туда такую строчку


     KEY_TO_BITLY=ХХХХХХХХХХХХХХХХХХХХХХХХХХ

где "ХХХХХХХХХХХХХХХХХХХХХХХХХХ" - это ваш токен, полученый на bitly.com

## Запуск 
    $ python3 bitlink_create_link.py 
    Введите адрес для битлинка:
  Введение данных в качестве примера ya.ru

    Введите адрес для битлинка: http://ya.ru
  Присваевание короткой ссылки:

    Битлинк: https://bit.ly/3pTSEll



