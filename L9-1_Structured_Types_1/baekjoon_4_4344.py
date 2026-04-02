import sys
input = sys.stdin.readline

test_case_num = int(input().rstrip())
for _ in range(test_case_num):
    scores = map(int, input().split())
    student_num = next(scores)
    scores = list(scores)
    avg = sum(scores) / student_num
    over_avg = (score > avg for score in scores)
    print(f"{(sum(over_avg) / student_num * 100, 3):.3f}%")
