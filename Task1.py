"""1)
a = 16
c = 16
while a <= 23:
    a+=1
    c+=a
print(c)"""
"""2)
N1 = int(input('Введите число'))
N2 = int(input('Введите второе число'))
print(N1+N2)"""

"""#3)
alb = 255
n = int(input('Введите число'))
if n <= alb :
    print(alb - n)"""

"""4)
n1, n2, n3 = int(input('Введите первое число')),  int(input('Введите первое число')), int(input('Введите первое число'))
print(n1+n2+n3, max(n1, n2, n3), min(n1, n2, n3))"""

"""#5)
n1 = abs(int(input('Введите число')))
n2 = abs(int(input('Введите число')))
print(max((n1, n2)) - min((n1, n2)))
"""
"""#6)
d = 96.51
e = 103.53
question = int(input('Введите 1, если вы хотите узнать про евро и 2, если вам интересно'))
n = int(input('Введите число долларов или евро'))
if question == 1:
    print(round (n*d, 2), 'столько стоит', n, 'долларов в рублях')
else:
    print(round (n*e, 2), 'Столько стоит', n, 'евро в рублях')"""

"""#7)
print(1572//int(input('Введите стоимость ')))"""

"""#8
n = int(input())
n1 = n%10
n10 = (n%100)//10
n100 = n//100
print(n100 + n10 + n1)"""

'''#9
n = int(input())
n1 = n%10
n10 = (n%100)//10
n100 = n//100
print(n1, n10, n100)'''

"""#10
print(1970 + int(input('Введите количество секунд ')) // 31536000)"""

"""#11
print(round((int(input('Масса ')) / ((int(input('Рост ')))/100)**2), 2))"""

#12
width = int(input('Ширина в метрах '))
h = int(input('Высота в метрах '))
need_paint = int(input("Расход краски, кв/л"))
V = int(input('Объём банки в литрах '))
p = int(input('Процент запаса '))
