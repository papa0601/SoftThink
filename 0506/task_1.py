from random import randrange
import sys

def gen_random_matrix(N: int) -> list[list[int]]:
    return [[randrange(1, 10*N*N) for x in range(N)] for i in range(N)]

def print_matrix(matrix: list[list[int]]) -> None:
    for line in matrix:
        for element in line:
            print(f'{element:8d}', end='')
        print()

def dot(mat_A: list[list[int]], mat_B:list[list[int]]) -> list[list[int]]:
    N = len(mat_A)
    result = [[0 for x in range(N)] for i in range(N)]
    for i in range(N):
        for x in range(N):
            for k in range(N):
                result[i][x] += mat_A[i][k] * mat_B[k][x]

    return result

def madd(mat_A: list[list[int]], mat_B:list[list[int]]) -> list[list[int]]:
    N = len(mat_A)
    return [[(mat_A[i][x] + mat_B[i][x]) for x in range(N)] for i in range(N)]
            

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    print(N)

    A = gen_random_matrix(N)
    print('A')
    print_matrix(A)
    B = gen_random_matrix(N)
    print('B')
    print_matrix(B)
    C = gen_random_matrix(N)
    print('C')
    print_matrix(C)

    print('result')
    print_matrix(madd(dot(A, B), C))



