

import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def ort(self):
        t_matrix = np.array(self.matrix).T
        basis = []
        for i in range(len(t_matrix)):
            if i == 0:
                if np.linalg.norm(t_matrix[i]) != 0:
                    f0 = t_matrix[i] / np.linalg.norm(t_matrix[i])
                    basis.append(f0)
            else:
                vi = np.array(t_matrix[i], dtype=float)  
                for j in range(i):
                    proj = np.dot(vi, basis[j]) / np.dot(basis[j], basis[j]) * basis[j]
                    vi -= proj
                if np.linalg.norm(vi) != 0:
                    fi = vi / np.linalg.norm(vi)
                    basis.append(fi)
        return basis


matrix_data = [
    [1, 2, 1, 7],
    [1, 2, 1, 1],
    [0, 3, 3, 32],
    [3, 7, 9, 9]
]

matrix_obj = Matrix(matrix_data)
basis_vectors = matrix_obj.ort()

for i, vector in enumerate(basis_vectors):
    print(f'f{i+1} =', vector)

