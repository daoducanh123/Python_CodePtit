class Matrix:
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.a = list()
        for _ in range(n):
            row = list(map(int,input().split()))
            self.a.append(row)
    def Trans(self):
        matran_trans = list()
        for i in range(self.m):
            row = list()
            for j in range(self.n):
                row.append(self.a[j][i])
            matran_trans.append(row)
        return matran_trans
    
    def Nhan(self, other):
        matran_res = list()
        for i in range (self.n): # lay so hang
            row = list()
            for j in range(len(other[0])): # lay so cot cua list other
                s = 0
                for k in range (self.m):
                    s+= self.a[i][k] * other[k][j]
                row.append(s)
            matran_res.append(row)
        return matran_res

t= int(input())
for _ in range(t):
    n,m = map(int,input().split())
    matrix  = Matrix(n,m)
    matrix_trans = matrix.Trans()
    matrix_res = matrix.Nhan(matrix_trans)
    
    for i in range(len(matrix_res)):
        for j in range(len(matrix_res[i])):
            print(matrix_res[i][j], end=" ")
        print()
    