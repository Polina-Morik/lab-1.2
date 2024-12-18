# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Network:
    """
     Создание объекта "Социальные сеты"

        :param name: Название сети
        :param count_post: Общее количество постов
        :param count_likes: Количество лайков

        Пример:
        >>> network1 = Network("Вконтакте", 15, 500)
    """
    def __init__(self, name: str, count_post: int, count_likes: int):
        if not isinstance(name, str):
            raise TypeError("Не соответствует тип данных")
        self.name = name

        if not isinstance(count_post, int):
            raise TypeError("Не соответствует тип данных")
        if count_post <= 0:
            raise ValueError("Количество постов не может быть отрицательным")
        self.count_pages = count_post

        if not isinstance(count_likes, int):
            raise TypeError("Не соответствует тип данных")
        if count_likes < 0:
            raise ValueError("Количество лайков не может быть отрицательным")
        self.count_likes = count_likes

    def see_post(self, post: int) -> None:
        """
         Функция, которая добавляет количество просмотренных постов

        :param post: Количество просмотренных постов
        :raise TypeError: Если не соответствует тип данных, то вызывается ошибка
        :raise ValueError: Если количество постов отрицательное, то вызывается ошибка

        Пример:
        >>> network1 = Network("Вконтакте", 15, 500)
        >>> network1.see_post(150)
        """
        if not isinstance(post, int):
            raise TypeError("Не соответствует тип данных")
        if post < 0:
            raise ValueError("Количество постов не может быть отрицательным")
        ...

    def searching_name(self, search_name: str) -> bool:
        """
        Функция, проверяет социальную сеть по названию

        :param search_name: Название искомой социальной сети
        :return: Совпадает ли название социальной сети с искомым названием
        :raise TypeError: Если не соответствует тип данных, то вызывается ошибка

        Пример:
        >>> network1 = Network("Вконтакте", 15, 500)
        >>> network1.searching_name("Инстаграм")
        """
        if not isinstance(search_name, str):
            raise TypeError("Не соответствует тип данных")
        ...


class Bed:
    """
     Создание объекта "Кровать"

        :param width: Ширина кровати
        :param length: Длина кровати

        Пример:
        >>> bed1 = Bed(120, 70)
    """
    def __init__(self, width: int, length: int):
        if not isinstance(width, int):
            raise TypeError("Не соответствует тип данных")
        if width <= 0:
            raise ValueError("Ширина кровати не может быть отрицательным")
        self.width = width

        if not isinstance(length, int):
            raise TypeError("Не соответствует тип данных")
        if length <= 0:
            raise ValueError("Длина кровати не может быть отрицательным")
        self.length = length

    def area_of_bed(self) -> int:
        """
         Функция, которая считает площадь кровати

         :return: Площадь кровати

        Пример:
        >>> bed1 = Bed(120,70)
        >>> bed1.area_of_bed()
        """
        ...

    def perimeter_of_bed(self) -> int:
        """
        Функция, которая считает периметр кровати

        :return: Периметр кровати

        Пример:
        >>> bed1 = Bed(120, 70)
        >>> bed1.perimeter_of_bed()
        """
        ...


class UniversityGrade:
    """
     Создание объекта "Успеваемость в университете"

        :param subject: название предмета
        :param number_comp: Количество сданных работ
        :param number_uncomp: Количество несданных работ

        Пример:
        >>> grade = UniversityGrade("Физика", 5, 3)
    """

    def __init__(self, subject: str, number_comp: int, number_uncomp: int):
        if not isinstance(subject, str):
            raise TypeError("Не соответствует тип данных")
        self.subject = subject

        if not isinstance(number_comp, int):
            raise TypeError("Не соответствует тип данных")
        if number_comp < 0:
            raise ValueError("Количество работ не может быть отрицательным")
        self.number_comp = number_comp

        if not isinstance(number_comp, int):
            raise TypeError("Не соответствует тип данных")
        if number_comp < 0:
            raise ValueError("Количество работ не может быть отрицательным")
        self.number_comp = number_comp

    def add_comp(self, count: int) -> None:
        """
         Функция, которая увеличивает количество сданных работ

        :param count: Количество добавленных работ
        :raise TypeError: Если не соответствует тип данных, то вызывается ошибка
        :raise ValueError: Если количество работ отрицательное, то вызывается ошибка

        Пример:
        >>> grade = UniversityGrade("Физика", 5, 3)
        >>> grade.add_comp(2)
        """
        if not isinstance(count, int):
            raise TypeError("Не соответствует тип данных")
        if count < 0:
            raise ValueError("Количество работ не может быть отрицательным")
        ...

    def average_score(self) -> float:
        """
        Функция, которая считает средний колисчество работ

        :return: Средний балл

        Пример:
        >>> grade = UniversityGrade("Физика", 5, 3)
        >>> grade.average_score()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
