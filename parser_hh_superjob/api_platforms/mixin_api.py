from parser_hh_superjob.api_platforms.models import all_models


class ObjectVacancyMixin:

    @staticmethod
    def get_object_vacancy(vacancy: dict, model_vacancy: all_models) -> object:
        """Получение объекта вакансии"""

        object_vacancy = model_vacancy(vacancy)
        return object_vacancy
