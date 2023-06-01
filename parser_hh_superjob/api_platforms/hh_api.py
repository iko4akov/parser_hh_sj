import requests

from parser_hh_superjob.api_platforms.models.hh_model import ModelHeadHunter
from parser_hh_superjob.api_platforms.platform_api import PlatformAPI
from parser_hh_superjob.api_platforms.mixin_api import ObjectVacancyMixin
from config.config import Config


class HeadHunterAPI(PlatformAPI, ObjectVacancyMixin):

    def __init__(self):
        self.__url = Config.url_headhunter
        self.params = {'area': 113, 'per_page': 100, 'only_with_salary': True}
        self.vacancies_hh = []

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    @property
    def _get_response(self) -> dict:
        """Получение ответа от API"""

        return requests.get(self.url, self.params).json()

    def _get_vacancies_per_page(self) -> None:
        """Наполнение списка вакансий self.vacancies_hh, вакансиями полученными с одной страницы"""

        data = self._get_response['items']

        for vacancy in data:
            hh_vacancy = self.get_object_vacancy(vacancy, ModelHeadHunter)

            self.vacancies_hh.append(hh_vacancy)

    def get_vacancies(self, key_words: str) -> list:
        """Получение списка вакансий со всех страниц платформы"""
        self.params['text'] = key_words
        try:
            all_pages = int(self._get_response['pages'])

            for i in range(all_pages):
                self.params['page'] = i
                self._get_vacancies_per_page()

            return self.vacancies_hh

        except KeyError:
            print("Нет вакансий, соответствующих заданным критериям. HH")
