def gen_prime(n):
    """
    Функция для генерации простых чисел в диапазон [2, N]
    используя решето Эратосфена.
    """
    # Создаем булев список длиной N.
    # True - значит число простое, False - составное.
    l = [True] * (n + 1)

    # Результирующий список простых чисел.
    result = []

    # Начальное значение
    p = 2

    # Начинаем перебирать все числа.
    while p <= n:

        if l[p]:
            # Добавляеем очередное простое число.
            result.append(p)

            # Проход вперед для отметки чисел кратных p.
            factor = 2  # Множитель
            p_mult = p * factor  # Число кратное p.

            # Проходим по всем кратным числам и отмечаем их как False.
            while p_mult <= n:  # Это условие в уроке показано с ошибкой, должно быть <= n
                l[p_mult] = False
                factor += 1
                p_mult = p * factor

        p += 1

    return result


print(gen_prime(129))
