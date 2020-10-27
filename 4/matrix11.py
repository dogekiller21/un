#Matrix11

def make_matrix(n, m):
    def yieldin(n, m):
        for i in range(1, n * m + 1):
            yield i
    a = yieldin(n, m)
    return [[next(a) for i in range(n)] for i in range(m)]

[print(list(reversed(row))) if i % 2 != 0 else print(row) for i, row in enumerate(make_matrix(int(input('n=')), int(input('m='))))]

