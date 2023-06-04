from parser_hh_superjob.exceptions.my_exceptions import InvalidLen


class CommandsHandler:

    @staticmethod
    def get_quantity_vacancies():
        while True:
            try:
                quantity = int(input("Введите количество вакансий для вывода в топ N: "))
                return quantity
            except ValueError:
                print('Введено не число')

    @staticmethod
    def get_salary_range():
        while True:
            try:
                user_input = input("Введите диапазон зарплат в формате '1000 150000' :").split()
                if len(user_input) == 2:
                    salary_from = int(user_input[0])
                    salary_to = int(user_input[1])
                    return salary_from, salary_to

                else:
                    raise InvalidLen

            except ValueError:
                print('Введено не число')

            except InvalidLen as e:
                print(e.message)

    @staticmethod
    def get_id_vacancy():
        while True:
            try:
                id_vacancy = int(input("Введите ID вакансии для удаления ее из файла: "))
                return id_vacancy

            except ValueError:
                print('Введите целое число')
