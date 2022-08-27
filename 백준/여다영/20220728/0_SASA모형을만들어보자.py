#SASA 모형을 만들어보자

#문제
#당신은 SASA 연못에서 알파벳 S 모양의 블록 N개와 알파벳 A 모양의 블록 M개를 건졌다. 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.
#SASA 모형 1개를 만들기 위해서는, 알파벳 S 모양의 블록 2개와 알파벳 A 모양의 블록 2개가 필요하다. 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.

#입력
#첫째 줄에 알파벳 S 모양의 블록의 개수 N과 알파벳 A 모양의 블록의 개수 M이 공백으로 구분되어 주어진다.

#출력
#태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 출력한다.

#제한
#1 <= N, M <= 10의 9제곱

import sys
sys.stdin = open('0_SASA모형을만들어보자.txt', 'r')

##첫번째 풀이(시간초과)
S, A = map(int, input().split())

cnt = 1
while True:
    if (S - (2 * cnt)) <= 0 and (A - (2 * cnt) <= 0):
        break
    cnt += 1
print(cnt - 1)

##두번째 풀이(시간초과)
S, A = map(int, input().split())

cnt = 0
while S > 0 and A > 0:
    S -= 2
    A -= 2
    cnt += 1
print(cnt)

##마지막 풀이
#둘 중 더 작은 것을 찾아내고, 그 수를 2로 나눴을 때의 몫을 출력하면 된다.
S, A = map(int, input().split())

print(min(S, A) // 2)