login = input('Введите логин ')#Вводим логин

for x in range(len(login)):#цакл работает столько раз, сколько символов в перременной login(len считает кол-во символов)
 if login[x] == '=' or login[x] == '?' or login[x] == '^' or login[x] == '$' or login[x] == '№' or login[x] == '@' or login[x] == '_':#Если перебираемый символ равен какой-то из введённых знаков, то они выведутся на консоли.(or = или)
  print(login[x])