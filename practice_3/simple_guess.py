#ввод любое натурльное число
#вывод: корень этого числа, если он целый
#если его нет - трудно, не могу
#def guess(num: int) -> int:


#81
#9

N = int(input('N:'))

def guess(N: int) -> int | str:
    res = 0
    for i in range(1, N+1):
        if i * i == N:
            return i
    return 'no'
    
print(guess(N))
# result = guess(N)
# if result != 0:
#      print(result)
# else:
#      print('трудно, не могу')





