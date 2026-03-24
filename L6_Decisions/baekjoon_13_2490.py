import sys
input = sys.stdin.readline

yut_stat = {
    0: "D",
    1: "C",
    2: "B",
    3: "A",
    4: "E",
}

for _ in range(3):
    print(yut_stat[sum(list(map(int, input().split())))])