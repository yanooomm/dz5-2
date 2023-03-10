'''
1. Усовершенствовать игру «Камень, ножницы, бумага».
Пользователь играет с компьютером и делает ход:
1 – Камень, 2 – Ножницы, 3 – Бумага. Компьютер делает
ответный ход и объявляет победителя. Камень бьет ножницы,
ножницы режут бумагу, бумага кроет камень. Основная
программа должна состоять только из вызова одной
единственной функции – mainMenu(). Функция mainMenu()
должна выводить на экран меню пользователя и запрашивать
число от 1 до 3. Внутри этой функции должна вызваться
функция для проверки правильности ввода числа и функция,
которая реализует сам алгоритм игры и определяет
победителя (либо объявляет ничью). Таким образом,
в программе должно быть 3 функции.
'''

import random
    
def CheckPlayer(x):
    if x not in {1, 2, 3}:
        return False
    else:
        return True
    
def game():
    player = int(input())
    while not CheckPlayer(player) :
        print('Число введено неверно')
        print('Введите число, в соответствии с правилами!')
        player = int(input())
    if player == 1:
        print('Ваш ход: Камень')
    if player == 2:
        print('Ваш ход: Ножницы')
    if player == 3:
        print('Ваш ход: Бумага')
    computer = random.randint(1, 3)
    if computer == 1:
        print('Ход компьютера: ', 'Камень')
    if computer == 2:
        print('Ход компьютера: ', 'Ножницы')
    if computer == 3:
        print('Ход компьютера: ', 'Бумага')
    if (player == 1 and computer == 2) or (player == 2 and computer == 1):
        print('Камень разбивает ножницы')
        if player == 1:
            print('Вы победили!')
        else:
            print('Победил компьютер!')
    elif (player ==  1 and computer == 3) or (player ==  3 and computer == 1):
        print('Бумага заворачивает камень')
        if player == 3:
            print('Вы победили!')
        else:
            print('Победил компьютер!')
    elif (player == 2 and computer == 3) or (player == 3 and computer == 2):
        print('Ножницы режут бумагу')
        if player == 2:
            print('Вы победили!')
        else:
            print('Победил компьютер!')
    else:
        print('Ничья!')


def mainMenu():
    print('Добро пожаловать в игру "Камень, ножницы, бумага"')
    print('Вы ходите первым! Введите число в соответствии со значением:')
    print('1 - Камень, 2 - Ножницы, 3 - Бумага')
    game()
    print('Игра окончена! Хотите сыграть еще раз ?')
    print('1 - да, 2 - нет')
    OneMoreTime = int(input())
    while OneMoreTime == 1:
        print('Введите число:')
        game()
        print('Игра окончена! Хотите сыграть еще раз ?')
        print('1 - да, 2 - нет')
        OneMoreTime = int(input())
    print('Спасибо за игру!')
    
    
mainMenu()




'''Добро пожаловать в игру "Камень, ножницы, бумага"
Вы ходите первым! Введите число в соответствии со значением:
1 - Камень, 2 - Ножницы, 3 - Бумага
1
Ваш ход: Камень
Ход компьютера:  Ножницы
Камень разбивает ножницы
Вы победили!
Игра окончена! Хотите сыграть еще раз ?
1 - да, 2 - нет
1
Введите число:
2
Ваш ход: Ножницы
Ход компьютера:  Камень
Камень разбивает ножницы
Победил компьютер!
Игра окончена! Хотите сыграть еще раз ?
1 - да, 2 - нет
1
Введите число:
3
Ваш ход: Бумага
Ход компьютера:  Камень
Бумага заворачивает камень
Вы победили!
Игра окончена! Хотите сыграть еще раз ?
1 - да, 2 - нет
1
Введите число:
4
Число введено неверно
Введите число, в соответствии с правилами!
2
Ваш ход: Ножницы
Ход компьютера:  Камень
Камень разбивает ножницы
Победил компьютер!
Игра окончена! Хотите сыграть еще раз ?
1 - да, 2 - нет
2
Спасибо за игру!
'''
    
