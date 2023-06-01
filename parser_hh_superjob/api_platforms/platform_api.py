from abc import ABC, abstractmethod


class PlatformAPI(ABC):

    @abstractmethod
    def _get_response(self):
        """Получение ответа от API"""
        pass

    @abstractmethod
    def _get_vacancies_per_page(self):
        """Наполнение списка вакансий self.vacancies_hh, вакансиями полученными с одной страницы"""
        pass

    @abstractmethod
    def get_vacancies(self, key_words: str) -> list:
        """Получение списка вакансий со всех страниц платформы"""
        pass
