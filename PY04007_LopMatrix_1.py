
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.a = list()

        for i in range(n):
            row = list(map(int, input().split()))
            self.a.append(row)

    def Trans(self):
        matrix_trans = list()

        for i in range(self.m):
            column = list()

            for j in range(self.n):
                column.append(self.a[j][i])

            matrix_trans.append(column)

        return matrix_trans

    def Nhan(self, other):
        c = list()

        # self (n,m) * other (m,n) = c (n,n)
        for i in range(self.n):
            row = list()

            for j in range(len(other[0])):
                s = 0

                for k in range(self.m):
                    s += self.a[i][k] * other[k][j]

                row.append(s)

            c.append(row)

        return c


# main
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    matrix = Matrix(n, m)

    matrix_trans = matrix.Trans()
    c = matrix.Nhan(matrix_trans)

    for row in c:
        print(*row)
