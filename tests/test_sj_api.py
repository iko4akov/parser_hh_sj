from parser_hh_superjob.api_platforms.superjob_api import SuperJobAPI

class TestSjAPI:

    def test_url_getter(self):
        """testCase1: test getter and setter"""
        sj_test = SuperJobAPI()

        assert sj_test.url == 'https://api.superjob.ru/2.0/vacancies'

        sj_test.url = 'https://google.com'

        assert sj_test.url == 'https://google.com'
