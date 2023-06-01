class MixinWorkingData:

    @staticmethod
    def sorting_list(vacancies: list) -> list:
        """Принимает список с объектами вакансий,
        сортирует и возвращает упрощенный(__str__) отсортированный список"""

        sorted_vacancies = []

        sorted_objects = sorted(vacancies, reverse=True)

        for object_vacancy in sorted_objects:
            sorted_vacancies.append(object_vacancy.__str__())
        return sorted_vacancies

    @staticmethod
    def show_filtered_vacancy(filtered_vacancy: list) -> print:
        """Проверяет полученный список на полноту, показывает его содержимое"""

        if len(filtered_vacancy) == 0:
            print("Нет вакансий, соответствующих заданным критериям.")

        else:
            for vacancy in filtered_vacancy:
                print(vacancy)

    @staticmethod
    def get_filtered_list(quantity: int, salary_from: int, salary_to: int, data: list) -> list:
        """Возвращает отфильтрованный список data между параметрами salary_from и salary_to
        в количестве quantity"""

        filtered_list = []
        count = 0
        for vacancy in data:
            if salary_from < vacancy['ЗП от'] < salary_to:
                filtered_list.append(vacancy)
                count += 1
                if count == quantity:
                    break
        return filtered_list

    @staticmethod
    def compare_lists(data: list, id_vacancy: int) -> bool:
        """Получает список и удаляет из него объект с id_vacancy,
        если такой объект был, возвращает bool значение"""

        new_data = []
        for vacancy in data:
            if int(vacancy['ID Вакансии']) != id_vacancy:
                new_data.append(vacancy)

        return len(data) > len(new_data)
