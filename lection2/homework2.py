

num: list = [1, 2, 3, 4]
ind: list = []
for i in range(len(num) - 1):
    if num[i + 1] - num[i] > 1:
        ind.append(i+1)
    

if len(ind) == 0:
    print('не найдено')
elif len(ind) == 1:
    print(ind[0])
else:
    print(ind)
