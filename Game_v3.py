import numpy as np
import random
#random.seed(1)
rand_num = random.randint(1, 101)
def game_core_v3(num:int=1) -> int:
    """Guessing predicted number
 Args:
 num (int, optional): predicted number. Defaults to 1.
 Returns:
 int: Amount of guessing attempts
    """
    count = 0
    start = 1
    finish = 100
    while True:
        count += 1
        predict_num = (start + finish) // 2
        if predict_num == rand_num:
            print(f'The number {predict_num} was guessed in {count} attempts!')
            break
        elif predict_num > rand_num:
            finish = predict_num
        else:
            start = predict_num
        if count > 20:
            break
    return count
def count_attempts(game_core_v3) -> int:
    """Average amount of attempts to guess the number
    Args:
        game_core_v3 (_type_): guessing function
        
    Returns:
        int: average number of attempts
    """
    attempts = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1)) # загадали список чисел

    for num in random_array:
        attempts.append(game_core_v3(num))

    score = int(np.mean(attempts)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    count_attempts(game_core_v3)