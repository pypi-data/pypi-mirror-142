import requests
import json
import re
from datetime import datetime
from janda.utils import parser, just_number

BASE_URL = 'https://nhentai.sinxdr.workers.dev'
BASE_IMG = 'https://i.nhentai.net/galleries'

class Nhentai(object):

    @staticmethod
    def preg_match_tags(tags):
        """Parses the tags and returns a list of tags.

        Parameters
        ----------
        tags : str
            The tags to be parsed.
        
        Returns
        -------
        list
        """

        tags_name = []
        for tag in tags:
            tags_name.append(tag['name'])
        return tags_name

    @staticmethod
    def get_language_in_tags(tags):
        """Parses language value

        Parameters
        ----------
        tags : list
            The tags to be parsed.

        Returns
        -------
        str
        """

        for tag in tags:
            if tag['type'] == 'language':
                return tag['name']
    


    def __init__(self, api_key: str = ''):
        """Initializes the client.

        Parameters
        ----------
        api_key : str
            scathach.dev API key (optional)
        
        Returns
        -------
        None
        """
        if api_key is '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}

    async def get_book(self, book: int, safe_search: bool = None):
        """Get doujin API from Id

        Parameters
        ----------
        book : int
            Nmber id of the book

        safe_search : bool
            If True, janda will throw you error whenever contains minor content, such as loli or shota. Default is False

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
        """

        try:
            if isinstance(book, int):
                book = str(book)

            self.book = str(just_number(book))

        except ValueError:
            raise ValueError('Book must be an int')

        data = requests.get(F'{BASE_URL}/api/gallery/{self.book}')
        if data.status_code == 404:
            raise ValueError('Book not found')

        if data.status_code != 200:
            raise ValueError('Request failed')

        return parser(data.json())

    async def search(self, tags: str, page: int = 1, popular: str = 'today'):
        """Search doujin by tags / artis / character / parody or group

        Parameters
        ----------
        tags : str
            Tags to search for.

        page : int
            Page number. Default is 1.

        popular : str
            Popularity type. Default is today.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
        """

        if popular not in ['today', 'all', 'week']:
            raise ValueError('popular must be today, all, or week')

        self.specs['query'] = tags
        self.specs['page'] = page
        self.specs['popular'] = popular

        data = requests.get(
            f'{BASE_URL}/api/galleries/search', params=self.specs)

        if data.status_code != 200:
            raise ValueError('Request failed')

        if data.status_code != 200:
            raise ValueError('Request failed')

        self.raw_object = json.loads(Nhentai.better_object(data.json()))
        self.results = self.raw_object['result']

        self.results_object = []
        for result in self.results:
            self.results_object.append({
                'id': result['id'],
                'title': result['title'],
                'link': f'https://nhentai.net/g/{result["id"]}',
                'upload_date': Nhentai.readable_timestamp(result['upload_date']),
                'num_pages': result['num_pages'],
                'num_favorites': result['num_favorites'],
                'language': Nhentai.get_language_in_tags(result['tags']),
                'tags': Nhentai.preg_match_tags(result['tags'])
            })

        return Nhentai.better_object(self.results_object)

    async def get_related(self, book: int):
        """Get realated book API from book ID or book link

        Parameters
        ----------
        book : int
            Nmber id of the book

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
        """

        try:
            self.book = str(Nhentai.just_number(book))

        except ValueError:
            raise ValueError('Book must be an int')

        data = requests.get(F'{BASE_URL}/api/gallery/{self.book}/related')

        if data.status_code != 200:
            raise ValueError('Request failed')

        if data.status_code != 200:
            raise ValueError('Request failed')

        self.raw_object = json.loads(Nhentai.better_object(data.json()))
        self.results = self.raw_object['result']

        self.results_object = []
        for result in self.results:
            self.results_object.append({
                'id': result['id'],
                'title': result['title'],
                'link': f'https://nhentai.net/g/{result["id"]}',
                'upload_date': Nhentai.readable_timestamp(result['upload_date']),
                'num_pages': result['num_pages'],
                'num_favorites': result['num_favorites'],
                'language': Nhentai.get_language_in_tags(result['tags']),
                'tags': Nhentai.preg_match_tags(result['tags'])
            })

        return Nhentai.better_object(self.results_object)

    async def random(self):
        """Get random doujin
        
        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
        """
        random = requests.get(F'{BASE_URL}/random')

        try:
            self.book = str(Nhentai.just_number(random.url))

        except ValueError:
            raise ValueError('Uh oh something wrong here')

        data = requests.get(F'{BASE_URL}/api/gallery/{self.book}')
        if data.status_code == 404:
            raise ValueError('Error')

        if data.status_code != 200:
            raise ValueError('Request failed')

        return Nhentai.parser(data.json())
