import pytest


from parser_hh_superjob.api_platforms.models.hh_model import ModelHeadHunter
from parser_hh_superjob.api_platforms.models.superjob_model import ModelSuperJob
from parser_hh_superjob.mixin_working_data import MixinWorkingData as mx

@pytest.fixture()
def list_with_object() -> list:
    hh_model1 = ModelHeadHunter({
        'salary': {'from': 50000, 'currency': 'currency1', 'to': 50000},
        'id': 1,
        'name': 1,
        'area': {'name': 'area1'},
        'apply_alternate_url': 'url1',
        'employer': {'name': 'employer1'},
        'experience': 'experience1'
    })
    hh_model2 = ModelHeadHunter({
        'salary': {'from': 60000, 'currency': 'currency1', 'to': 60000},
        'id': 2,
        'name': 2,
        'area': {'name': 'area2'},
        'apply_alternate_url': 'url2',
        'employer': {'name': 'employer2'},
        'experience': 'experience2'
    })
    sj_model = ModelSuperJob({
        'payment_from': 40000,
        'payment_to': 40000,
        'currency': 'currency3',
        'id': 3,
        'profession': 3,
        'town': {'title': 'area1'},
        'link': 'url1',
        'firm_name': 'employer3',
        'experience': {'title': 'experience'}
    })
    return [hh_model1, hh_model2, sj_model]


class TestMixinWorkingData:

    def test_sotring_list(self, list_with_object):
        """TestCase1"""
        result = mx.sorting_list(list_with_object)
        assert result[0]['ID Вакансии'] == 2
        assert result[1]['ID Вакансии'] == 1
        assert result[2]['ID Вакансии'] == 3

    def test_show_filtered_vacancy(self):
        """TestCase2 len list != 0"""
        test_list = [0, {}, 10]

        assert mx.show_filtered_vacancy(test_list) == print(i for i in test_list)

    def test_show_filtered_vacancy_zero(self):
        """TestCase3 len = 0"""

        test_list = []

        assert mx.show_filtered_vacancy(test_list) == print("Нет вакансий, соответствующих заданным критериям.")

    def test_get_filtered_list(self):
        filter_list = [
            {'ЗП от': 1500},
            {'ЗП от': 1000},
            {'ЗП от': 2000},
        ]

        filtred_list = mx.get_filtered_list(3, 1000, 2000, filter_list)

        assert filtred_list[0]['ЗП от'] == 1500

