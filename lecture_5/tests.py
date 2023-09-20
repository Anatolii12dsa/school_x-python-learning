a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]

def mask_list(array: list[int], mask: list[int]) -> list[int]:
    return [val * mask[i] * .5 for i, val in enumerate(array)]

def test_masl_list():
    print('проверяем тест маск лист')
    assert test_masl_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0]

answer = [val*b[i] for i, val in enumerate(a)]

print(answer)


