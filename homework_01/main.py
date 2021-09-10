"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    req = []
    for num in args:
        req.append(num ** 2)
    return req


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    """
    функция определения простое-ли число
    :param num: число на проверку
    :return: True - число простое, False - иначе
    """
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False  # поделилось на что-то => не простое
        return True  # больше единицы и делится только на 1 и себя => простое
    return False  # 1 и меньше - не простые


def filter_numbers(input_list, tag):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if tag == ODD:
        return list(filter(lambda x: x % 2 == 1, input_list))
    elif tag == EVEN:
        return list(filter(lambda x: x % 2 == 0, input_list))
    elif tag == PRIME:
        return list(filter(is_prime, input_list))
