class MixinCheckSalary:

    @staticmethod
    def _check_salary(salary):
        """Обработка значений если params['salary'] имеет значение None"""

        if salary['to'] is None:
            return salary['from'], 0, salary['currency']

        elif salary['from'] is None:
            return 0, salary['to'], salary['currency']

        else:
            return salary['from'], salary['to'], salary['currency']
