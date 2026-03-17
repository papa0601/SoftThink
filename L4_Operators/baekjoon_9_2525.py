import sys
input = sys.stdin.readline

ch, cm = map(int, input().split())
estm = int(input().rstrip())

endm = (ch * 60 + cm + estm) % (24 * 60)
print(endm // 60, endm % 60, sep=" ")
