#분해합

#문제
#어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
#어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 
#예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
#자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

#입력
#첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

#출력
#첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

import sys
sys.stdin = open('1_분해합.txt', 'r')

compare = int(input())

number = '1'
while number != '1000001': #분해합이 없는 경우까지만 계산
    total = int(number) #분해합에는 자기 자신도 포합되므로 total을 자기자신으로 초기화합니다.
    for i in range(len(number)):
        total += int(number[i]) #각 자리수를 total에 더해줍니다.
    if total == compare: #생산자와 분해합이 같으면
        break #무한 반복문을 탈출합니다.
    else:
        number = str(int(number) + 1) #그게 아니라면 생산자를 1 증가시켜줍니다.
if number == '1000001': #생산자가 없는 경우
    print('0') #'0' 출력
else: #생산자를 찾았다면
    print(number) #print


##or
#분해합을 계산하는 함수를 생성해준다.

def count_number(n): 
    #생산자에 대한 분해합을 계산해주는 함수
    total = int(n)
    for i in n:
        total += int(i)
    return total

result = int(input())
for i in range(1, result + 1):
    count = count_number(str(i))
    if str(count) == str(result):
        print(i)
        break
else:
    print('0')