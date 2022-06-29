import random
import prompt


"""
Необходимо реализовать игру "Проверка на чётность". 
Суть игры в следующем: пользователю показывается случайное число. 
И ему нужно ответить yes, если число чётное, или no — если нечётное:
"""


def guess_number():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1

    while count <= 3:
        random_number = random.randint(1, 20)
        print(f"Question: {random_number}")
        answer = prompt.string("You answer: ")

        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
            count += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break

    if count == 4:
        print(f"Congratulations, {name}!")
