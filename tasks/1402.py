# baekjoon 1402

import sys
from collections import defaultdict
from itertools import product
input = sys.stdin.readline

테스트횟수 = int(input().rstrip())

def 소인수분해(숫자: int) -> dict:
    계산한계 = int(pow(숫자, 0.5)) + 1
    인수들 = defaultdict(int)
    for 정수 in range(2, 계산한계):
        while 숫자 % 정수 == 0:
            인수들[정수] += 1
            숫자 = 숫자 // 정수
    if 숫자 > 1:
        인수들[숫자] += 1

    return 인수들

for _ in range(테스트횟수):
    주어진수, 타겟 = map(int, input().split())
    소인수분해결과 = 소인수분해(주어진수)
    print(소인수분해결과)    
    소인수 = list(소인수분해결과.keys())
    횟수 = list(소인수분해결과.values())

    for 경우 in product(*[range(1, 수+1) for 수 in 횟수]):
        
        if sum(경우) == 주어진수:
            print('yes')
            break
    
    else:
        print('no')
    
