a = input() #Дорогие друзья, для связи со мной лучше использовать почту mailmar@siple.com на моем личном сервере
s = a.split(' ')

print(s)

for i in range(len(s)):
    if s[i].find('@') != -1:
        print(s[i])