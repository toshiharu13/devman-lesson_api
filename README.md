# Счетчик кликов

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

## Техническое описание
ПО предназанчено для конвертирования ссылок в короткие, а если предоставлена короткая ссылка, отражает количество кликов по ней.
Ссылку необходимо вводить полную.

## Системные требования
- [Python 3](https://www.python.org/)

##  Установка
### Для установки дастаточно:

 - Cклонировать проект


        $ https://github.com/toshiharu13/django-orm-watching-storage.git
    

 - Установить requirements.txt


        $ pip install -r requirements.txt
      

 - Сгенерировать токен на bitly.com
 - Создать в проекте файл .env и записать туда такую строчку


       KEY_TO_BITLY=ХХХХХХХХХХХХХХХХХХХХХХХХХХ

где "ХХХХХХХХХХХХХХХХХХХХХХХХХХ" - это ваш токен, полученый на bitly.com

## Запуск 

  Введение данных, в качестве примера ya.ru:

    python3 bitlink_create_link.py http://ya.ru

  Программа присваевает короткую ссылку:

    Битлинк: https://bit.ly/3pTSEll

  Введение короткой ссылки:

    python3 bitlink_create_link.py https://bit.ly/3pTSEll

  Программа отдаёт количество переходов по короткой ссылке:

    Количество переходов по ссылке битли: 0




