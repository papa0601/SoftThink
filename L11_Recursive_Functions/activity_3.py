import timecheck
from functools import lru_cache

'''
옮길 기둥이 홀수면 중간으로, 아니면 바로 결과로
'''

def hanoi_move(n: int, start: str, buffer: str, dest: str) -> None:
    if n == 1:
        print(f"{n}을 {start}에서 {dest}로 이동함!")
        return None
    
    hanoi_move(n-1, start, dest, buffer)
    print(f"{n}을 {start}에서 {dest}로 이동함!")
    hanoi_move(n-1, buffer, start, dest)

if __name__ == '__main__':
    with timecheck.check_time():
        hanoi_move(5, 'A', 'B', 'C')