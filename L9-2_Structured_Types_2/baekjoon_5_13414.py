import sys
input = sys.stdin.readline

capacity, btn_clicked = map(int, input().split())
sugang = dict()

for i in range(btn_clicked):
    sugang[input().rstrip()] = i

sugang_final = sorted(sugang.items(), key=lambda x: x[1])[:capacity]
print(*[val[0] for val in sugang_final], sep='\n')