# BUG 백준에서 Python3로 실행시 시간초과, 이에 PyPy3로 통과함 
# O(n^2)
import sys
from itertools import combinations
input = sys.stdin.readline

num_dots = int(input().rstrip())
print(sum(abs(x[0] - x[1]) for x in combinations(map(int, input().split()), 2))*2)


'''
다음은 AI가 제안한 풀이, O(n log n) (정렬), 순회는 O(n)
import sys
input = sys.stdin.readline

# 점의 개수 입력 (아래 계산에서는 직접 쓰지 않아도 무방)
num_dots = int(input().rstrip())
# 좌표를 정렬해서 읽음: 정렬하면 왼쪽 값들은 항상 현재 값 이하
points = sorted(map(int, input().split()))

# 현재 인덱스 i보다 왼쪽 원소들의 합
prefix_sum = 0
# i < j 인 쌍들에 대한 거리 합 누적
pair_distance_sum = 0

for i, value in enumerate(points):
	# (value - points[0]) + ... + (value - points[i-1])
	# = value * i - (points[0] + ... + points[i-1])
	pair_distance_sum += value * i - prefix_sum
	# 다음 인덱스를 위해 현재 값을 누적합에 반영
	prefix_sum += value

# 위에서 i < j만 셌으므로, 모든 i, j 합으로 만들기 위해 2배
print(pair_distance_sum * 2)
'''
