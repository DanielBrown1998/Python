import numpy as np
#sudoku codewars
class Sudoku(object):
    def __init__(self, data) -> None:
        self.data: list[list[int]] = data
    
    def is_valid(self)->bool:
        if len(self.data) == 1 and self.data[0][0] != 1 or isinstance(self.data[0][0], bool):
            return False
        if len(self.data) <= 0 or not isinstance(int((len(self.data))**1/2), int):
            return False
        divisors = np.array([2, 3, 5, 7, 11, 13, 17, 21])
        for x, row in enumerate(self.data):
            if len(row) != len(self.data):
                return False
            for element in row:
                if row.count(element) != 1 or not isinstance(element, int):
                    return False
            list_prov = []
            for y in range(len(self.data)):
                list_prov.append(self.data[y][x])
            if list_prov.count(element) != 1:
                return False
            del list_prov
        num = 1
        for divisor in divisors:
            if divisor > len(self.data)//2:
                break
            if len(self.data)%divisor == 0:
                num = divisor
        vetor = np.array(self.data)
        e = 1
        for i in range(0, len(self.data), num):
            c = 1
            for j in range(0, len(self.data),num):
                vetor_parcial = list(vetor[i:num*e, j:num*c].copy())
                if len(np.unique(vetor_parcial)) != len(self.data):
                    return False 
                c += 1
            e += 1
        return True
        

if __name__ == '__main__':
    table= [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 1, 5, 6, 4, 8, 9, 7],
    [3, 1, 2, 6, 4, 5, 9, 7, 8],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 4, 8, 9, 7, 2, 3, 1],
    [6, 4, 5, 9, 7, 8, 3, 1, 2],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 7, 2, 3, 1, 5, 6, 4],
    [9, 7, 8, 3, 1, 2, 6, 4, 5]
]

    sudoku = Sudoku(table)
    print(sudoku.is_valid())
