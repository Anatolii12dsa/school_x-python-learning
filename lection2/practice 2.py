numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
for n in numbers:
    
    if n % 3 == 0:
        print(f'Число - {n} кратно трём')
        print(n)
    if n % 3 != 0:
        print(f'Число - {n} not кратно трём')
        print(n)
for n in numbers:
    if n % 3 == 0 and n % 5 ==0:
        print(f'число - {n} универсальное')
        print(n)
    elif n % 3 == 0:
        print(f'число - {n} делится  на 3')
        print(n)
    elif n % 5 == 0:
        print(f'число - {n} делится на 5')
        print(n)
    else:
        print(f'число - {n} никакое')
        print(n)


# word: str = input('введите слово:')
# vowel: str = 'aeiouy'

# vowel_count: int = 0

# for ch in word:
#     if ch in vowel:
#         vowel_count += 1

# print(vowel_count)

# n: int = int(input('N:'))
 
# while n > 0:
#     print(n)
#     n = n + 1