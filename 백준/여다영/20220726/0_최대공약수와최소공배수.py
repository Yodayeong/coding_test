#문제
#두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

#출력
#첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

#최대공약수란 두 수가 공통으로 가지는 약수들 중 가장 큰 수를 말하며,
#이는 두 수가 모두 다음의 수로 나뉘어진다는 것을 뜻한다.
import sys
sys.stdin = open('0_최대공약수와최소공배수.txt', 'r')

a, b = map(int, input().split())

temp = a #둘 중 아무 수를 temp에 두고 
while True:
    if a % temp == 0 and b % temp ==0: #두 수가 temp로 나눠질 때까지
        break
    temp -= 1 #temp 수를 하나씩 줄여나간다.
print(temp)

temp_2 = a
cnt = 1
while True:
    if temp_2 % a == 0 and temp_2 % b == 0: #temp_2가 두 수에 의해 나눠질 때까지
        break
    cnt += 1
    temp_2 = a #한번 할 때마다 초기화를 해주고
    temp_2 *= cnt #temp_2에 2.3.4...배를 해준다.
print(temp_2)