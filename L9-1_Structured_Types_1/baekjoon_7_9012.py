import sys
input = sys.stdin.readline

'''
재귀로 풀어야 하는 느낌이 존나게 나고 있다;;;
'''

test_scase_num = int(input().rstrip())

for _ in range(test_scase_num):
    given_string = input().rstrip()
    if not all(char in ('(', ')') for char in given_string):
        print("NO")
        continue

    elif given_string.count("(") != given_string.count(")"):
        print("NO")
        continue

    elif given_string[0] == ")" or given_string[-1] == "(":
        print("NO")
        continue

    string_old = ""
    while given_string != string_old:
        string_old = given_string
        given_string = given_string.replace("()", "")
    if given_string:
        print("NO")
        continue

    print("YES") 