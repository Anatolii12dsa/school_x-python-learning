# numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
# for n in numbers:
    
#     if n % 3 == 0:
#         print(f'Число - {n} кратно трём')
#     if n % 3 != 0:
#         print(f'Число - {n} not кратно трём')
# for n in numbers:
#     if n % 3 == 0 and n % 5 ==0:
#         print(f'число - {n} универсальное')
#     elif n % 3 == 0:
#         print(f'число - {n} делится  на 3')
#     elif n % 5 == 0:
#         print(f'число - {n} делится на 5')
#     else:
#         print(f'число - {n} никакое')


# word: str = input('введите слово:')
# vowel: str = 'aeiouy'

# vowel_count: int = 0

# for ch in word:
#     if ch in vowel:
#         vowel_count += 1

# print(vowel_count)

n: int = int(input('N:'))
 
while n > 0:
    print(n)
    n = n + 1