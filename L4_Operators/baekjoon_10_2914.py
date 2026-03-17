import sys
input = sys.stdin.readline

song_count, expectation = map(int, input().split())

print(song_count * (expectation - 1) + 1)