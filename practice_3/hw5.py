
N = int(input("введите число секунд: "))
minut = round(N / 60)
hour = minut // 60
minut2 = minut % 60
print(N, '-->', f'{hour} час(а/ов) и {minut2} минут(а/ы)')



