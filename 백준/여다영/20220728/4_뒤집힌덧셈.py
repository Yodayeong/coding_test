#뒤집힌 덧셈

#문제
#어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.
#두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

#입력
#첫째 줄에 수 X와 Y가 주어진다. X와 Y는 1,000보다 작거나 같은 자연수이다.

#출력
#첫째 줄에 문제의 정답을 출력한다.

import sys
sys.stdin = open('4_뒤집힌덧셈.txt', 'r')

def REV(k):
    #reverse해주는 함수를 생성합니다.
    return k[::-1]

x, y = input().split()
#reverse는 string에서만 가능하기 때문에 string으로 값을 받아서 변환하고
#합할때는 다시 int로
#함수를 쓸 때는 다시 str으로
#출력해줄 때는 int로 해줍니다.
print(int(REV(str(int(REV(x)) + int(REV(y))))))