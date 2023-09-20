def convert_ab_to_int(a: str, b: str) -> (int, int):
    a, b = int(a), int(b)
    return a, b
def divide_ab(a: int | float, b: int | float) -> float:
    return a / b

while True:
    a, b = input('введите 2 числа для их суммы:').split()
    try:
        a, b = convert_ab_to_int(a, b)
        division_scope = divide_ab(a, b)
    except ValueError as e:
        print(f'ошибка: {e}')
        print('ошибка')
        print()
        continue
    except ZeroDivisionError as e:
        print(f'ошибка: {e}')
        print('ошибка')
        print()
        continue
    except AttributeError as ex:
        print(f'ошибка: {e}')
        print('ошибка')
        print()
        break
    ab_sum = a + b
    print(f'Сумма {a} + {b} = {ab_sum}')
    print(f'{a} / {b} = {division_scope}')
    print()