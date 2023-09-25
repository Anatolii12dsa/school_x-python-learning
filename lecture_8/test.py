

def find_inverse_matrix(matrix):
    n = len(matrix)
    
    # Создаем расширенную матрицу, где справа от вертикальной черты будет единичная матрица
    augmented_matrix = [row + [0] * n for row in matrix]
    for i in range(n):
        augmented_matrix[i][n + i] = 1
    
    
    # Приводим матрицу к диагональному виду
    for i in range(n):
        # Находим максимальный элемент в столбце и переставляем строки
        max_row = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[max_row][i]):
                max_row = j
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]
        
        # Делаем элемент в текущей строке и столбце равным 1
        pivot = augmented_matrix[i][i]
        for j in range(i, n * 2):
            augmented_matrix[i][j] /= pivot
        
        # Обнуляем остальные элементы в столбце
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                for k in range(i, n * 2):
                    augmented_matrix[j][k] -= factor * augmented_matrix[i][k]
    
    # Извлекаем обратную матрицу из расширенной матрицы
    inverse_matrix = [row[n:] for row in augmented_matrix]
    
    return inverse_matrix

# Пример использования
matrix = [
    [2, 1, 4],
    [5, 3, 2],
    [7, 3, 1]
]

inverse = find_inverse_matrix(matrix)
for row in inverse:
    print(row)
