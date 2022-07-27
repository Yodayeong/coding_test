#연월일 달력

#연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
#해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
#”YYYY/MM/DD”형식으로 출력하고,
#날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

#연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
#일은 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
#※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

#입력]
#입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
#다음 줄부터 각 테스트 케이스가 주어진다.

#[출력]
#테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
#(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
sys.stdin = open('8_연월일달력.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    date = input()
    check = 0

    #문자열 슬라이싱
    month  = date[4:6]
    day = date[6:8]
    
    if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
        if int(day) >= 1 and int(day) <= 31:
            check = 1
    elif month == '02':
        if int(day) >= 1 and int(day) <= 28:
            check = 1
    elif month == '04' or month =='06' or month == '09' or month =='11':
        if int(day) >= 1 and int(day) <= 30:
            check = 1
    
    print(f'#{i}', end = ' ')
    if check == 1:
        #문자열 슬라이싱 적극 활용
        print(date[0:4], end = '/')
        print(date[4:6], end = '/')
        print(date[6:8])
    else:
        print('-1')