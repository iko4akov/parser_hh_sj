from parser_hh_superjob.api_platforms.models.platform_model import PlatformModel
from parser_hh_superjob.api_platforms.models.mixin_check_salary import MixinCheckSalary


class ModelHeadHunter(PlatformModel, MixinCheckSalary):

    def __init__(self, vacancy: dict):
        self.id = vacancy['id']
        self.name = vacancy['name']
        self.area = vacancy['area']['name']
        self.apply_alternate_url = vacancy.get('apply_alternate_url')
        self.employer = vacancy.get('employer')['name']
        self.experience = vacancy.get('experience')
        self.salary_from, self.salary_to, self.currency = self._check_salary(vacancy['salary'])

    def __str__(self) -> dict:
        """Возвращает словарь"""

        return {
            'ID Вакансии': self.id,
            'Название': self.name,
            'Город': self.area,
            'ЗП от': self.salary_from,
            'Зп до': self.salary_to,
            'URL': self.apply_alternate_url,
            'Работодатель': self.employer,
            'Опыт': self.experience
        }

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from
