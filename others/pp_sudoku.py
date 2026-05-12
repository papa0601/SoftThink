def _is_valid_row(row, num: str):
    return num not in row

def _is_valid_col(board, col, num: str):
    for row in board:
        if row[col] == num:
            return False
    return True

def _is_valid_block(board, block: tuple[int, int], num: str):
    '''
    block 변수는
    3*3으로 묶은 추상적인 단위
    즉,
    0 1 2
    0 1 2
    0 1 2
    '''
    for i in range(block[0]*3, block[0]*3+3):
        for j in range(block[1]*3, block[1]*3+3):
            if board[i][j] == num:
                return False
    return True

    

def _is_valid(board, axis: tuple[int, int], num: str) -> bool:
    '''
    board: 스도쿠 보드
    axis: (행, 열) tuple임
    num: 들어갈 숫자 근데 타입이 str
    '''

    get_block = lambda row, col: (row // 3, col // 3)
    block = get_block(axis[0], axis[1])

    return all([_is_valid_row(board[axis[0]], num), _is_valid_col(board, axis[1], num), _is_valid_block(board, block, num)])

def find_holes(board) -> list[tuple[int, int]]:
    holes = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == '0':
                holes.append((i, j))
    
    return holes

def solve_sudoku(depth: int, board, holes):
    if depth == len(holes):
        return True
    
    for i in range(1, 10):
        num = str(i)
        if _is_valid(sudoku_with_holes_str, holes[depth], num):
            sudoku_with_holes_str[holes[depth][0]][holes[depth][1]] = num
            if solve_sudoku(depth+1, board, holes):
                return True
            sudoku_with_holes_str[holes[depth][0]][holes[depth][1]] = '0'
    
    return False

def print_board(board):
    for line in board:
        print(' '.join(line))


if __name__ == '__main__':
    new_board = [['0'] * 9 for _ in range(9)]
    
    '''
    sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    '''
    
    sudoku_with_holes_str = [
        ["5", "0", "4", "6", "0", "8", "9", "1", "0"],
        ["6", "7", "0", "1", "9", "0", "3", "0", "8"],
        ["0", "9", "8", "0", "4", "2", "5", "6", "0"],
        ["8", "5", "0", "7", "6", "1", "0", "2", "3"],
        ["4", "0", "6", "8", "0", "3", "7", "0", "1"],
        ["7", "1", "3", "0", "2", "0", "8", "5", "6"],
        ["0", "6", "1", "5", "3", "0", "2", "8", "0"],
        ["2", "0", "7", "4", "1", "9", "0", "3", "5"],
        ["0", "4", "5", "0", "8", "6", "1", "0", "9"]
    ]

    holes = find_holes(sudoku_with_holes_str)
    if not solve_sudoku(0, sudoku_with_holes_str, holes):
        raise Exception
    print_board(sudoku_with_holes_str)