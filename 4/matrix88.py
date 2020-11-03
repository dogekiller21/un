#Matrix88

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
class Matrix(object):
    def yielding(self, value):
        for i in range(1, value ** 2 + 1):
            yield i
    def make_matrix(self, value):
        a = self.yielding(value)
        return [[next(a) for i in range(value)] for i in range(value)]
    def ending(self, value=4):
        matrix = self.make_matrix(value)
        for j in range(len(matrix)):
            i = 0
            while i < j:
                matrix[j][i] = 0
                i += 1
        return matrix

matr = Matrix()
matrix = matr.ending()
[print(matrix[i]) for i in range(len(matrix))]
