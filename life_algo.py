from itertools import product
from typing import MutableSet

def get_neighbours(n_rows, n_cols):
    neighbours = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_cols):
            r_nei = [i-1, i, i+1]
            c_nei = [j-1, j, j+1]
            if i-1 < 0:
                r_nei.remove(i-1)
            if i+1 >= n_rows:
                r_nei.remove(i+1)
            if j-1 < 0:
                c_nei.remove(j-1)
            if j+1 >= n_cols:
                c_nei.remove(j+1)
            nei = list(product(r_nei, c_nei))
            nei.remove((i,j))
            neighbours[i][j] = nei
    return neighbours


def conway_iter(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    neighbours = get_neighbours(n_rows, n_cols)
    next_gen = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            nei_alive = 0
            cur_cell = matrix[row][col]
            for nei_row, nei_col in neighbours[row][col]:
                if matrix[nei_row][nei_col] == 1:
                    nei_alive += 1
            if cur_cell == 1 and nei_alive < 2:
                next_gen[row][col] = 0
                continue
            if cur_cell == 1 and nei_alive in (2,3):
                next_gen[row][col] = 1
                continue
            if cur_cell == 1 and nei_alive > 3:
                next_gen[row][col] = 0
                continue
            if cur_cell == 0 and nei_alive == 3:
                next_gen[row][col] = 1
                continue
    return next_gen

if __name__ == "__main__":
    matrix = [[0 for _ in range(3)] for _ in range(3)]
    matrix[0][1] = 1
    matrix[1][1] = 1
    matrix[2][1] = 1
    for _ in range(4):
        for line in matrix:
            print(line)
        print()
        matrix = conway_iter(matrix)
