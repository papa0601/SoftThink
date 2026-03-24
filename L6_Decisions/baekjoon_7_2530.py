import sys
input = sys.stdin.readline

ch, cm, cs = map(int, input().split())
ests = int(input().rstrip())
ctts = ch * 60 * 60 + cm * 60 + cs
fts = (ctts + ests) % 86400
fh = fts // (60**2)
fm = (fts % (60**2)) // 60
fs = fts % 60
print(fh, fm, fs, sep=' ')