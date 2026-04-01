import sys
input = sys.stdin.readline

test_case_num = int(input().rstrip())

for _ in range(test_case_num):
    base, degree = map(int, input().split())
    res = pow(base % 10, degree, 10)
    print(10 if res == 0 else res)
