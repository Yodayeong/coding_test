#문제
#김형택은 탑문고의 직원이다. 
#김형택은 계산대에서 계산을 하는 직원이다. 
#김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

#오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 
#이 값은 1,000보다 작거나 같은 자연수이다. 
#둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 
#책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

#출력
#첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 
#만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.

import sys
sys.stdin = open('7_베스트셀러.txt', 'r')

n = int(input())

books = dict()
for i in range(n):
    temp = input()
    if temp in books:
        books[temp] += 1
    else:
        books[temp] = 1

most = max(books.values())
final = []
for key in books:
    if books[key] == most:
        final.append(key)

final.sort()
print(final[0])