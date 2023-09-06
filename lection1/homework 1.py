N = int(input('введите число:'))
def sum(k):
    return ((N//k)/2)*(k + (k * (N//k)))
result = sum(3) + sum(5) - sum(15)
print(result)