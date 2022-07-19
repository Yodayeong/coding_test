#거꾸로 출력해 보아요

#주어진 숫자부터 0까지 순서대로 찍어보세요

import sys
sys.stdin = open('problem_2.txt', 'r')

item = int(input())
while item != -1:
    print(item, end = ' ')
    item -= 1