from parser_hh_superjob.api_platforms.models.platform_model import PlatformModel


class ModelSuperJob(PlatformModel):

    def __init__(self, vacancy: dict):
        self.id = vacancy['id']
        self.name = vacancy['profession']
        self.area = vacancy['town']['title']
        self.apply_alternate_url = vacancy.get('link')
        self.employer = vacancy.get('firm_name')
        self.experience = vacancy.get('experience')['title']
        self.salary_from = int(vacancy.get('payment_from'))
        self.salary_to = int(vacancy.get('payment_to'))
        self.currency = vacancy.get('currency')

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
