def print_matrix(matrix):
    for line in matrix:
        for element in line:
            print(f'{element:5d}', end='')
        print()

# 테스트 데이터
test_matrix = [
    [1, 23, 456],
    [7890, 1, 2],
    [10, 20, 30]
]

print_matrix(test_matrix)
