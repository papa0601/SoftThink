month_end_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

string = ''

index = 4
string += '   ' * 4

for month in range(12):
    for date in range(1, month_end_date[month] + 1):
        string += f"{date:3}"

        index += 1

        if index % 7 == 0:
            string += '\n'
    
string_list = string.split('\n')
month_check = 0
given_month = int(input())
last_printed = False
line_count = 0

date = ['목', '금', '토', '일', '월', '화', '수']
print('  ', end='')
for i in range(7):
    print(f"{date[(i+3) % 7]:2}", end='')
print()

for line in string_list:
    if line.find('  1') != -1:
        month_check += 1
    
    if month_check == given_month:
        line_count += 1
        last_printed = True
        if line_count == 1:
            for _ in range(20, 31):
                s = str(_)
                line = line.replace(s, '  ')
        print(line)
    
    elif last_printed:
        for _ in range(1, 7):
            s = str(_)
            line = line.replace("  " + s, ' ')
        print(line)
        last_printed = False