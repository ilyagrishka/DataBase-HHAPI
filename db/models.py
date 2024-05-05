class EmployerModel:

    def __init__(self, company_name, company_id, company_address, number_of_employees):
        # атрибуты для модели работодателей
        self.company_name = company_name
        self.company_id = company_id
        self.company_address = company_address
        self.number_of_employees = number_of_employees

    def __repr__(self):
        return (f'{self.company_name} \n'
                f'{self.company_id} - {self.company_address}\n'
                f'{self.number_of_employees}')

    @classmethod
    def serialize_all(cls, data):
        # Должен возвращать список сериализованных обектов
        return data.__dict__


class Vacancy:
    def __init__(self, name_vac, vac_id, salary):
        # атрибуты для модели вакансий
        self.name_vac = name_vac
        self.vac_id = vac_id
        self.salary = salary

    def __repr__(self):
        return (f"{self.name_vac} - {self.vac_id}\n"
                f"{self.salary}")
