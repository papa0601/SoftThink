from collections import defaultdict
import sys
input = sys.stdin.readline

card_count = defaultdict(int)

card_num = int(input().rstrip())
cards = map(int, input().split())

for n in cards: card_count[n] += 1

check_num = int(input().rstrip())
checks = map(int, input().split())
print(' '.join(str(card_count[n]) for n in checks))
