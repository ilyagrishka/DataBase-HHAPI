from abc import ABC
import psycopg2


class BaseManager(ABC):
    def delete(self, pk):
        pass

    def create(self, **kwargs):
        pass


class DBManager(BaseManager):
    def delete(self, pk):
        pass

    def create(self, **kwargs):
        pass

    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        self.cur.execute("SELECT company_name, COUNT(*) FROM company GROUP BY company_name")
        return self.cur.fetchall()

    def get_all_vacancies(self):
        self.cur.execute("SELECT company_name, vacancy_name, salary  FROM company and vacancies")  ####????
        return self.cur.fetchall()


def get_avg_salary(self):
    self.cur.execute("SELECT AVG(salary) FROM vacancies")
    return self.cur.fetchall()


def get_vacancies_with_higher_salary(self):
    avg_salary = self.get_avg_salary()
    self.cur.execute("SELECT company_name, vacancy_name, salary FROM vacancies WHERE salary > %s",
                     (avg_salary,))
    return self.cur.fetchall()

# def get_vacancies_with_keyword(self):
#     self.cur.execute(
#         "SELECT company_name, vacancy_name, salary FROM vacancies WHERE vacancy_name LIKE %s",
#
#     return self.cur.fetchall()
