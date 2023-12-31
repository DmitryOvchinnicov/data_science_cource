import numpy as np


def game_core_v3(number: int=1) -> int:
    """ Сначала устанавливаем любое random число, затем сужаем диапазон с обеих 
        сторон, в зависимости от сравнения переменных. Делим диапазон поиска до 
        тех пор, пока не угадаем число .
        Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101) # предполагаемое число
    left_border = 1
    right_border = 101

    
    while number!=predict: # создаю цикл по поиску числа
        count += 1
        predict = left_border + (right_border-left_border)//2 # сужаю диапазон

        if predict > number:
            right_border = predict
        elif predict < number:
            left_border = predict
        else:
            break        

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
    print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)