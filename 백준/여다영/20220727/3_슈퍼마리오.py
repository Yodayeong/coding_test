#슈퍼 마리오

#문제
#슈퍼 마리오 앞에 10개의 버섯이 일렬로 놓여져 있다. 이 버섯을 먹으면 점수를 받는다.
#슈퍼 마리오는 버섯을 처음부터 나온 순서대로 집으려고 한다. 하지만, 모든 버섯을 집을 필요는 없고 중간에 중단할 수 있다. 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다. 따라서 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없다.
#마리오는 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.
#버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램을 작성하시오.

#입력
#총 10개의 줄에 각각의 버섯의 점수가 주어진다. 이 값은 100보다 작거나 같은 양의 정수이다. 버섯이 나온 순서대로 점수가 주어진다.

#출력
#첫째 줄에 마리오가 받는 점수를 출력한다. 만약 100에 가까운 수가 2개라면 (예: 98, 102) 마리오는 큰 값을 선택한다.

import sys
sys.stdin = open('3_슈퍼마리오.txt', 'r')

points = []
#버섯 point 입력받기
for i in range(10):
    points.append(int(input()))

score = []
#하나의 버섯을 먹을 때마다 현재의 score을 저장한다.
now_score = 0
now = 0
for i in points:
    #버섯들을 하나씩 먹으면서
    if now_score >= 100:
        #100이나 100이상의 수가 저장되면 멈춘다.
        break
    now_score += points[now]
    #현재 score는 이때까지 먹은 버섯 point의 총합
    score.append(now_score)
    now += 1

now_score = score[now - 1]
prior_score = score[now - 2]
if now_score == 100:
    #score가 100인 경우
    print(100)
elif (now_score - 100) > (100 - prior_score):
    #100과 가장 가까운 수가 socre 리스트에서 한 칸 앞일 때
    print(prior_score)
else:
    #score 리스트에서 가장 큰 수가 100과 가장 가깝거나, 100과 가장 가까운 수가 2개 일때
    print(now_score)