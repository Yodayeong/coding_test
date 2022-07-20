#더블더블

#1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

#주어질 숫자는 30을 넘지 않는다.

import sys
sys.stdin = open('problem_5.txt', 'r')

times = int(input())

init = 1
items = []
for i in range(times + 1):
    items.append(init)
    init *= 2

for item in items:
    print(item, end = ' ')