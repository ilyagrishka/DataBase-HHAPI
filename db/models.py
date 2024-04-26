from abc import ABC


class EmployerModel:

    def __init__(self):
        # атрибуты для модели работодателей
        pass

    def __repr__(self):
        pass

    @classmethod
    def serialize_all(cls):
        # Должен возвращать список сериализованных обектов
        pass


class Vacancy:
    def __init__(self):
        # атрибуты для модели вакансий
        pass

    def __repr__(self):
        pass
