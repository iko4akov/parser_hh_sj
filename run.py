from parser_hh_superjob.JSON_saver.json_saver import JSONSaver
from parser_hh_superjob.api_platforms.hh_api import HeadHunterAPI
from parser_hh_superjob.api_platforms.superjob_api import SuperJobAPI
from parser_hh_superjob.command_handler import CommandsHandler


def user_interaction():

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    filter_words = input("Введите ключевые слова для фильтрации вакансий,\nпример <Python develop Краснодар>: ")

    print('please wait....')

    hh_vacancies = hh_api.get_vacancies(filter_words)
    superjob_vacancies = superjob_api.get_vacancies(filter_words.split())

    vacancy = hh_vacancies + superjob_vacancies

    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)

    command_handler = CommandsHandler()

    top_n = command_handler.get_quantity_vacancies()

    key_exit_while = True

    while key_exit_while:

        salary_from, salary_to = command_handler.get_salary_range()
        key_exit_while = json_saver.get_vacancies_by_salary(top_n, salary_from, salary_to)


    id_vacancy = command_handler.get_id_vacancy()

    while id_vacancy != 'stop':
        json_saver.delete_vacancy(id_vacancy)
        id_vacancy = command_handler.get_id_vacancy()

if __name__ == "__main__":
    user_interaction()
