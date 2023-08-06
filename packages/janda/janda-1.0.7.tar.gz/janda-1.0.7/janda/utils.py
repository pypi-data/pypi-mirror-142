import requests
import json
import re
from datetime import datetime

BASE_URL = 'https://nhentai.sinxdr.workers.dev'
BASE_IMG = 'https://i.nhentai.net/galleries'

def auto_space(string):
    """Automatically adds spaces for GET requests

    Parameters
    ----------
    string : str
        The string to be formatted.

    Returns
    -------
    str

    """
    return string.replace(' ', '+')


def just_number(string):
    """Remove the non-numeric characters from a string.

    Parameters
    ----------
    string : str
        The desired string.

    Returns
    -------
    str
    """
    return re.sub(r'\D', '', string)

def better_object(parser):
    """Converts the json object to a more readable object.

    Parameters
    ----------
    parser : dict
        
    Returns
    -------
    dict

    """
    return json.dumps(parser, sort_keys=True, indent=4, ensure_ascii=False)


def readable_timestamp(timestamp):
    """Converts a timestamp to a datetime object.

    Parameters
    ----------
    timestamp : int
        The timestamp to be converted.

    Returns
    -------
    str
    """
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

def parser(obj: dict):
        raw_object = json.loads(better_object(obj))
        media = raw_object['media_id']

        book_object = {
            'details': {
                'id': raw_object['id'],
                'title': raw_object['title'],
                'link': f'https://nhentai.net/g/{raw_object["id"]}',
                'upload_date': readable_timestamp(raw_object['upload_date'])
            },
            'scanlator': raw_object['scanlator'],
            'num_pages': raw_object['num_pages'],
            'num_favorites': raw_object['num_favorites']}

        tags = []
        for tag in raw_object['tags']:
            tags.append(tag['name'])
        book_object['tags'] = tags

        for tag in raw_object['tags']:
            if tag['type'] == 'language':
                book_object['language'] = tag['name']
                break

        image_urls = []
        for image in raw_object['images']['pages']:

            if image['t'] == 'p':
                image_urls.append(
                    f'{BASE_IMG}/{media}/{len(image_urls) + 1}.png')

            elif image['t'] == 'j':
                image_urls.append(
                    f'{BASE_IMG}/{media}/{len(image_urls) + 1}.jpg')

            elif image['t'] == 'g':
                image_urls.append(
                    f'{BASE_IMG}/{media}/{len(image_urls) + 1}.gif')

        book_object['image_urls'] = image_urls

        thumbnail_urls = []
        for image in raw_object['images']['pages']:
            if image['t'] == 'p':
                thumbnail_urls.append(
                    f'{BASE_IMG}/{media}/{len(thumbnail_urls) + 1}t.png')

            elif image['t'] == 'j':
                thumbnail_urls.append(
                    f'{BASE_IMG}/{media}/{len(thumbnail_urls) + 1}t.jpg')

            elif image['t'] == 'g':
                thumbnail_urls.append(
                    f'{BASE_IMG}/{media}/{len(thumbnail_urls) + 1}t.gif')

        book_object['thumbnail_urls'] = thumbnail_urls
        return better_object(book_object)