from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """Возвращает экземпляр класса Connector """
        pass


class HH(Engine):
    def get_request(self):
        pass

class Superjob(Engine):
    def get_request(self):
        pass

class Vacancy:
    # __slots__ = ...

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        pass

# class CountMixin:
#
#     @property
#     def get_count_of_vacancy(self):
#                 """
#         Вернуть количество вакансий от текущего сервиса.
#         Получать количество необходимо динамически из файла.
#         """
#         pass

# class HHVacancy(Vacancy):  # add counter mixin
#     """ HeadHunter Vacancy """
#
#     def __str__(self):
#         return f'HH: {self.comany_name}, зарплата: {self.salary} руб/мес'

# class SJVacancy(Vacancy):  # add counter mixin
#     """ SuperJob Vacancy """
#
#     def __str__(self):
#         return f'SJ: {self.comany_name}, зарплата: {self.salary} руб/мес'
#
#     def sorting(vacancies):
#         """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
#         pass
#
#     def get_top(vacancies, top_count):
#         """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
#         pass


# class Connector:
#     """
#     Класс коннектор к файлу, обязательно файл должен быть в json формате
#     не забывать проверять целостность данных, что файл с данными не подвергся
#     внешнего деградации
#     """
#     __data_file = None
#
#     @property
#     def data_file(self):
#         pass
#
#     @data_file.setter
#     def data_file(self, value):
#         # тут должен быть код для установки файла
#         self.__connect()
#
#     def __connect(self):
#         """
#         Проверка на существование файла с данными и
#         создание его при необходимости
#         Также проверить на деградацию и возбудить исключение
#         если файл потерял актуальность в структуре данных
#         """
#         pass
#
#     def insert(self, data):
#         """
#         Запись данных в файл с сохранением структуры и исходных данных
#         """
#         pass
#
#     def select(self, query):
#         """
#         Выбор данных из файла с применением фильтрации
#         query содержит словарь, в котором ключ это поле для
#         фильтрации, а значение это искомое значение, например:
#         {'price': 1000}, должно отфильтровать данные по полю price
#         и вернуть все строки, в которых цена 1000
#         """
#         pass
#
#     def delete(self, query):
#         """
#         Удаление записей из файла, которые соответствуют запрос,
#         как в методе select. Если в query передан пустой словарь, то
#         функция удаления не сработает
#         """
#         pass
#
# if __name__ == '__main__':
#     df = Connector('df.json')
#
#     data_for_file = {'id': 1, 'title': 'tet'}
#
#     df.insert(data_for_file)
#     data_from_file = df.select(dict())
#     assert data_from_file == [data_for_file]
#
#     df.delete({'id': 1})
#     data_from_file = df.select(dict())
#     assert data_from_file == []