s = int(input('Стоимость без учёта скидки '))
skidka = int(input('Скидка '))
r = ((s / 100) * skidka)# вычисляет сколько р будет скидка
os = s - ((s / 100) * skidka)#стоимость со скидкой
while os>=0:#работает пока стоимость со скидкой не равна 0
 print(os)
 os = s - ((s / 100) * skidka)
 s -= r

    #
