from random import randrange
import sys

def gen_random_matrix(N: int) -> list[list[int]]:
    return [[randrange(1, 10*N*N) for x in range(N)] for i in range(N)]

def print_matrix(matrix: list[list[int]]) -> None:
    for line in matrix:
        for element in line:
            print(f'{element:8d}', end='')
        print()

def transpose(matrix: list[list[int]]) -> list[list[int]]:
    N = len(matrix)
    return [[matrix[x][i] for x in range(N)] for i in range(N)]

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    matrix = gen_random_matrix(N)
    print_matrix(matrix)

    print('\n'*2)
    print_matrix(transpose(matrix))

