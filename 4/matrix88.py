#Matrix88

matr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def make_some_job(matrix):
    for j in range(len(matrix)):
        i = 0
        while i < j:
            matrix[j][i] = 0
            i += 1
    return matrix

matrix = make_some_job(matr)
[print(matrix[i]) for i in range(len(matrix))]
