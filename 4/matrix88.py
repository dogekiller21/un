#Matrix88

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

def make_matrix(m):
    def yieldin(m):
        for i in range(1, m**2 + 1):
            yield i
    a = yieldin(m)
    return [[next(a) for i in range(m)] for i in range(m)]

matrix = make_matrix(int(input('m=')))

for j in range(len(matrix)):
    i = 0
    while i < j:
        matrix[j][i] = 0
        i += 1

[print(matrix[i]) for i in range(len(matrix))]
