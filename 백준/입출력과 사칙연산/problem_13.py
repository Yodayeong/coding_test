#곱셈

#문제
#(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

#   472 -- (1)
#  *385 -- (2)
#------
#  2360 -- (3)
# 3776 --(4)
#1416 --(5)
#------
#181720 --(6)

#입력
#첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

#출력
#첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

input_1 = int(input())
input_2 = input()

print(input_1 * int(input_2[2]))
print(input_1 * int(input_2[1]))
print(input_1 * int(input_2[0]))
print(input_1 * int(input_2))