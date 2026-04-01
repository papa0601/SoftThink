'''
[달별 마지막 날짜]
    31일: 1월, 3월, 5월, 7월, 8월, 10월, 12월
    30일: 4월, 6월, 9월, 11월
    28일: 2월 

1월 1일이 목요일 가정
'''

month_end_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['목', '금', '토', '일', '월', '화', '수']
given_month = int(input())
start_date = date[sum(month_end_date[:given_month-1]) % 7] # 7로 나눠서 요일 구함
index = 0 # 칸 수 맞추기 (이놈이 7의 배수먄 줄바꿈)
print('  ', end='')
# 일 월 화 수 목 금 토 출력하기
for i in range(7):
    print(f"{date[(i+3) % 7]:2}", end='') # [] <- 내부 수식 재밌다!
print()

# 1일 전에 몇 칸 띄워야하는지
start_margin = (sum(month_end_date[:given_month-1]) + 4) % 7

#계산한 만큼 띄운다
for i in range(start_margin):
    print(f"   ", end='')

index += start_margin
for i in range(1, month_end_date[given_month-1] + 1):
    print(f"{i:3}", end='')
    index += 1
    if index % 7 == 0: print() # 칸 수 맞추기 (이놈이 7의 배수먄 줄바꿈)
