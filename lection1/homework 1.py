# n = int(input())
# a = 0
# for i in range(1, n+1):
#     if i % 3 == 0 or i % 5 == 0:
#         a = a + i
# print(a)
#---------------------

N = int(input('введите число:'))
def sum(k):
    return ((N//k)/2)*(k + (k * (N//k)))
result = sum(3) + sum(5) - sum(15)
print(result)