from collections import defaultdict
import sys
input = sys.stdin.readline

book_sold = int(input().rstrip())
sell_log = defaultdict(int)

for _ in range(book_sold): sell_log[input().rstrip()] += 1
sell_refined = sorted(sell_log.items(), key=lambda x: x[0])
sell_refined.sort(key=lambda x: x[1], reverse=True)
print(sell_refined[0][0])
