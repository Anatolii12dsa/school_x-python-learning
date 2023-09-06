# На вход вы получаете число N.

# Вывести: массив числе от -N до N включительно возведённых в квадрат.

# Пример:

# Ввод: 4
# Вывод: [16, 9, 4, 1, 0, 1, 4, 9, 16]

N = int(input('N:'))
n1 = N
n2 = 0
i: list = []
if N > 0:
    while n1 > 0:
        i.append(n1**2)
        n1 -= 1
    while n2 <= N:
        i.append(n2**2)
        n2 += 1
    print(i)
if N < 0:
    while n1 < 0:
        i.append(n1**2)
        n1 += 1
    while n2 >= N:
        i.append(n2**2)
        n2 -= 1
    print(i)
else:
    print('[0]')



