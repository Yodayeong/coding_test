#유니크

#문제
#상근이와 친구들은 MT에 가서 아래 설명과 같이 재미있는 게임을 할 것이다.
#각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.
#상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.

#입력
#첫째 줄에 참가자의 수 N이 주어진다. (2 ≤ N ≤ 200) 둘째 줄부터 N개 줄에는 각 플레이어가 1번째, 2번째, 3번째 게임에서 쓴 수가 공백으로 구분되어 주어진다.

#출력
#각 플레이어가 3번의 게임에서 얻은 총 점수를 입력으로 주어진 순서대로 출력한다.

import sys
sys.stdin = open('1_유니크.txt', 'r')

num = int(input())
players = [list(input().split()) for _ in range(num)]
print(players)

points = [0] * num

play_1 = []
for j in range(num):
    play_1.append(players[j][0])

for k in range(num):
    if play_1[k] in play_1:
        points[k] += int(play_1[k])

play_2 = []
for j in range(num):
    play_2.append(players[j][1])

for k in range(num):
    if play_2[k] not in play_2:
        points[k] += int(play_2[k])

play_3 = []
for j in range(num):
    play_3.append(players[j][2])

for k in range(num):
    if play_3[k] not in play_3:
        points[k] += int(play_3[k])

print(points)