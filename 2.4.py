import numpy as np


class Decsnra:
    def __init__(self, matrix, first):
        self.A = np.array(matrix)
        x, y = np.shape(self.A)
        if x == y:
            self.n = x
        zeroes = list(np.diagonal(self.A))
        if zeroes == [np.int32(0) for _ in range(x)]:
            self.algorithm(first)
        else:
            print('Неправильно введены данные')

    def algorithm(self, first):
        flag, ways = [False for _ in range(self.n)], [1000000 for _ in range(self.n)]
        ways[first - 1] = 0
        print(*[f'путь {first}{i + 1} = {self.A[first - 1][i]}' for i in range(self.n)], sep='\n')
        for i in range(self.n):
            min_const = 1000001
            for j in range(self.n):
                if not flag[j] and ways[j] < min_const:
                    min_const = ways[j]
                    i = j
            for k in range(self.n):
                way = ways[i] + self.A[i][k]
                if way < ways[k]:
                    print(f'путь {first}{k + 1} : {first}{k} + {k}{k + 1} = {ways[i]} + {self.A[i][k]} = {way}')
                    ways[k] = way
            print(f'кратчайшее расстояние {first}{i + 1} : {ways[i]}', f'точка {i + 1} посещена', sep='\n')
            flag[i] = True
        print(f'все точки посещены, алгоритм завершается')
        print(f'минимальные пути от точки {first} : {ways}')


d = Decsnra([[0, 2, 2, 4],
             [2, 0, 4, 3],
             [2, 4, 0, 1],
             [4, 3, 1, 0]], 1)
