from abc import ABC


class BaseManager(ABC):
    def delete(self, pk):
        pass

    def create(self, **kwargs):
        pass


class DBManager(BaseManager):

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self, **kwargs):
        pass
