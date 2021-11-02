import requests
import os
from dotenv import load_dotenv
load_dotenv()

def shorten_link(token, url, link_to_bitly):
    body = {"long_url": link_to_bitly}
    headers = {'Authorization': token}
    check_for_correct_link = requests.get(link_to_bitly)
    check_for_correct_link.raise_for_status()
    response = requests.post(url, headers=headers, json=body)
    return response.json()['link']


def count_clicks(token, url):
    headers = {'Authorization': token}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def check_for_bitly_link(link_to_check):
    return 'bit.ly/' in link_to_check


if __name__ == "__main__":
    url_to_bitly = 'https://api-ssl.bitly.com/v4/bitlinks'
    key = os.getenv('KEY')

    link_to_bitly = input('Веедите адрес для битлинка: ')
    if check_for_bitly_link(link_to_bitly):
        url_count_clicks = f'https://api-ssl.bitly.com/v4/bitlinks/{link_to_bitly[7:]}/clicks/summary'
        print(f'количество кликов по ссылке: {count_clicks(key, url_count_clicks)}')
    else:
        response = shorten_link(key, url_to_bitly, link_to_bitly)
        print(f'Битлинк: {response}')
