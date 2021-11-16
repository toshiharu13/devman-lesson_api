import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, url, long_url):
    body = {"long_url": long_url}
    headers = {'Authorization': token}
    check_for_correct_link = requests.get(long_url)
    check_for_correct_link.raise_for_status()
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    if 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    return response.json()['link']


def count_clicks(token, entered_link, url_to_bitly):
    headers = {'Authorization': token}
    cleared_link = clear_link(entered_link)
    prepared_link = f'{url_to_bitly}/{cleared_link}/clicks/summary'
    response = requests.get(prepared_link, headers=headers)
    response.raise_for_status()
    if 'error' in response:
        raise requests.exceptions.HTTPError(response['error'])
    return response.json()['total_clicks']


def check_for_bitly_link(token, entered_link, url_to_bitly):
    headers = {'Authorization': token}
    cleared_link = clear_link(entered_link)
    prepared_link = f'{url_to_bitly}/{cleared_link}'
    response = requests.get(prepared_link, headers=headers)
    return response.ok


def clear_link(entered_link):
    link_parse = urlparse(entered_link)
    return link_parse.netloc + link_parse.path


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
    try:
        if check_for_bitly_link(key, entered_link, url_to_bitly):
            print(
                f'Количество переходов по ссылке битли: '
                f'{count_clicks(key, entered_link, url_to_bitly)}'
            )
        else:
            response = shorten_link(key, url_to_bitly, entered_link)
            print(f'Битлинк: {response}')
    except (requests.exceptions.MissingSchema,
            requests.exceptions.ConnectionError):
        print("Вы ввели неправильную ссылку.")
