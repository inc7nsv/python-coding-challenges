"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5,
то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""


def find_sum_of_multiples(multiple_1: int, multiple_2: int, limit: int) -> int:
    """
    Функция возвращает сумму чисел меньше заданного предела,
    кратных одному из двух заданных делителей
    """
    result = 0

    for number in range(1, limit):
        if number % multiple_1 == 0 or number % multiple_2 == 0:
            result += number

    return result


if __name__ == "__main__":
    print(find_sum_of_multiples(3, 5, 1000))