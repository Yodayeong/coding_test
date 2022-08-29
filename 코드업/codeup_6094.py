#이상한 출석 번호 부르기3

#번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
#n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

#출석을 부른 번호 중에 가장 빠른 번호를 출력한다.

n = int(input())
items = list(map(int, input().split()))  #map은 not subscriptable => list로 형 변환

min = items[0]
for i in range(n):
    if items[i] < min:
        min = items[i]
print(min)