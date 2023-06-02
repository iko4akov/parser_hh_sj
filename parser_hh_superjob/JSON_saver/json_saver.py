import json

from config.config import Config
from parser_hh_superjob.mixin_working_data import MixinWorkingData


class JSONSaver(MixinWorkingData):

    def __init__(self):
        self.file_name = Config.file_name

    def add_vacancy(self, vacancies: list) -> None:
        """Принимает список с обьектами вакансий,
        сохраняет отсортированный список в file_name, в формате JSON"""

        with open(self.file_name, 'w', encoding='utf-8') as file:
            sorted_vacancies = self.sorting_list(vacancies)
            file.write(json.dumps(sorted_vacancies, ensure_ascii=False))

    @property
    def read_file(self) -> list:
        """Возвращает данные из файла file_name"""

        with open(Config.file_name, encoding='utf-8') as file:
            return json.loads(file.read())

    def get_vacancies_by_salary(self, quantity: int, salary_from: int, salary_to: int) -> None:
        """Выводит пользователю отфильтрованные вакансии"""

        filtered_vacancy = self.__find_request(quantity, salary_from, salary_to)
        self.show_filtered_vacancy(filtered_vacancy)

    def __find_request(self, quantity: int, salary_from: int, salary_to: int) -> list:
        """Возвращает отфильтрованный список вакансий"""

        data = self.read_file

        filtered_list = self.get_filtered_list(quantity, salary_from, salary_to, data)

        return filtered_list

    def delete_vacancy(self, id_vacancy: int):
        """Удаляет вакансии из файла по ID"""

        data = self.read_file

        new_data = self.compare_lists(data, id_vacancy)

        if new_data:
            with open(Config.file_name, mode='w', encoding='utf-8') as file:
                file.write(json.dumps(new_data, ensure_ascii=False))
                print(f'vacancy by id: {id_vacancy} successful deleted')

