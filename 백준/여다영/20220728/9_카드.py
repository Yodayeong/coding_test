#문제
#준규는 숫자 카드 N장을 가지고 있다. 
#숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

#준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 
#만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

#입력
#첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
#둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

#출력
#첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.

import sys
sys.stdin = open('9_카드.txt', 'r')

n = int(input())

cards = dict()
for i in range(n):
    temp = int(input())
    if temp in cards:
        cards[temp] += 1
    else:
        cards[temp] = 1

most = max(cards.values())
final = []
for key in cards:
    if cards[key] == most:
        final.append(key)

final.sort()
print(final[0])