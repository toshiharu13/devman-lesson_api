import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, url, link_to_bitly):
    body = {"long_url": link_to_bitly}
    headers = {'Authorization': token}
    check_for_correct_link = requests.get(link_to_bitly)
    check_for_correct_link.raise_for_status()
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    if 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    return response.json()['link']


def count_clicks(token, url):
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    if 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    return response.json()['total_clicks']


def check_for_bitly_link(link_to_check):
    return 'bit.ly' in link_to_check


if __name__ == "__main__":
    load_dotenv()
    url_to_bitly = 'https://api-ssl.bitly.com/v4/bitlinks'
    key = os.getenv('KEY_TO_BITLY')

    parser = argparse.ArgumentParser(
        description='Программа формирует короткие ссылки'
    )
    parser.add_argument(
        'address', help='Введите полный адрес интересующего сайта'
    )
    args = parser.parse_args()
    entered_link = args.address
    link_parse = urlparse(entered_link)
    bitly_link = link_parse.netloc + link_parse.path
    print(type(link_parse.netloc))
    try:
        if check_for_bitly_link(bitly_link):

            url_count_clicks = (
                f'{url_to_bitly}/{bitly_link}/clicks/summary'
            )
            print(
                f'Количество переходов по ссылке битли: '
                f'{count_clicks(key, url_count_clicks)}'
            )
        else:
            response = shorten_link(key, url_to_bitly, entered_link)
            print(f'Битлинк: {response}')
    except (requests.exceptions.MissingSchema,
            requests.exceptions.ConnectionError):
        print("Вы ввели неправильную ссылку.")
