import sys
input = sys.stdin.readline

test_case_num = int(input().rstrip())

for _ in range(test_case_num):
    score = 0
    O_strik = 0
    line = input().rstrip()
    for char in line:
        if char == 'O':
            O_strik += 1
            score += O_strik
        
        else:
            O_strik = 0
    
    print(score)
