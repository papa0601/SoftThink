import sys
input = sys.stdin.readline

peak = 0
cur = 0

for _ in range(4):
    off, on = map(int, input().split())
    cur -= off
    cur += on
    peak = cur if cur > peak else peak

print(peak)
