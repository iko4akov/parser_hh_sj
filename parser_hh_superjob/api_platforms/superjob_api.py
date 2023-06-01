import requests

from parser_hh_superjob.api_platforms.mixin_api import ObjectVacancyMixin
from parser_hh_superjob.api_platforms.platform_api import PlatformAPI
from parser_hh_superjob.api_platforms.models.superjob_model import ModelSuperJob
from config.config import Config


class SuperJobAPI(PlatformAPI, ObjectVacancyMixin):

    def __init__(self):
        self.__url = Config.url_superjob
        self.headers = {'X-Api-App-Id': Config.secret}
        self.params = {'count': 100}
        self.vacancies_sj = []

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    @property
    def _get_response(self) -> dict:
        """Получение ответа от API"""

        return requests.get(self.url, headers=self.headers, params=self.params).json()

    def _get_vacancies_per_page(self) -> None:
        """Наполнение списка вакансий self.vacancies_hh, вакансиями полученными с одной страницы"""

        data = self._get_response['objects']
        for vacancy in data:
            sj_model = ModelSuperJob(vacancy)

            self.vacancies_sj.append(sj_model)

    def get_vacancies(self, key_words: list) -> list:
        """Получение списка вакансий со всех страниц платформы"""

        self.params['keywords'] = key_words
        try:

            all_pages = 5

            for i in range(all_pages):
                self.params['page'] = i
                self._get_vacancies_per_page()

            return self.vacancies_sj

        except KeyError:
            print("Нет вакансий, соответствующих заданным критериям.")
