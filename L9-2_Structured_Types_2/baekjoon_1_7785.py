import sys
input = sys.stdin.readline

log_length = int(input().rstrip())
company_status = set()

for _ in range(log_length):
    log = input().split()

    if log[1] == 'enter':
        company_status.add(log[0])
    
    else:
        company_status.remove(log[0])

print(*sorted(list(company_status), reverse=True), sep='\n')
