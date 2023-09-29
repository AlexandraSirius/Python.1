game = input()
if game == 'game':
    print('Игра "Угадай число"')
    for i in range(3):
        namber = input('Введите число ')
        if namber == '5':
            print('Вы выиграли билет на концерт!')
            break
        elif namber == 'off':
            break
        else:
            print('Неверный ответ')
    print('Игра завершена')