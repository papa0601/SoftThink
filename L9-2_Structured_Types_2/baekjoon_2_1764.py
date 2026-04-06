import sys
input = sys.stdin.readline

num_unseen, num_unheard = map(int, input().split())
unseen = {input().rstrip() for _ in range(num_unseen)}
unheard = {input().rstrip() for _ in range(num_unheard)}
unseen_unheard = list(unseen.intersection(unheard))
unseen_unheard.sort()
print(len(unseen_unheard), *unseen_unheard, sep='\n')