from parser_hh_superjob.api_platforms.hh_api import HeadHunterAPI
from config.config import Config

class TestHHAPI:

    def setUp(self):
        self.api = HeadHunterAPI()

    def test_url_property(self):
        """testCase1: test getter and setter"""

        assert self.api.url == 'https://api.hh.ru/vacancies'

        self.api.url = 'https://google.com'

        assert self.api.url == 'https://google.com'






