import pytest

from unittest.mock import patch
from parser_hh_superjob.command_handler import CommandsHandler

class TestCommandsHandler():

    @patch('builtins.input', side_effect=['5', '15', 'asf', '156'])
    def test_get_quantity_vacancies(self, mock_input):
        """TestCase1: type valid input"""

        assert CommandsHandler.get_quantity_vacancies() == 5
        assert CommandsHandler.get_quantity_vacancies() == 15
        assert CommandsHandler.get_quantity_vacancies() == 156

    @patch('builtins.input', side_effect=[{}])
    def test_get_quantity_vacancies_invalid(self, mock_input):
        """Testcase2: Type invalid input"""

        with pytest.raises(TypeError):
            CommandsHandler.get_quantity_vacancies()

    @patch('builtins.input', side_effect=['1 15', 'sad', '15', '10 13'])
    def test_get_salary_range_valid(self, mock_input):
        """TestCase3: type valid input"""

        assert CommandsHandler.get_salary_range() == (1, 15)
        assert CommandsHandler.get_salary_range() == (10, 13)

    @patch('builtins.input', side_effect=['15', '156 123', 'sdfsdg', '123'])
    def test_get_id_vacancy(self, mock_input):

        assert CommandsHandler.get_id_vacancy() == 15
        assert CommandsHandler.get_id_vacancy() == 123
