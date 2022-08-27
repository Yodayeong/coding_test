#가장 많은 글자

#문제
#영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.

#어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄부터 글의 문장이 주어진다. 글은 최대 50개의 줄로 이루어져 있고, 각 줄은 최대 50개의 글자로 이루어져 있다. 
#각 줄에는 공백과 알파벳 소문자만 있다. 문장에 알파벳은 적어도 하나 이상 있다.

#출력
#첫째 줄에 가장 많이 나온 문자를 출력한다. 여러 개일 경우에는 알파벳 순으로 앞서는 것부터 모두 공백없이 출력한다.

#파이썬에서의 eof 처리
#while True:
#    try:
#       [...]
#    except:
#        break

#딕셔너리 삭제
#del(dict['key'])

import sys
sys.stdin = open('3_가장많은글자.txt', 'r')

alphabets = dict()
while True:
    try:
    #try, except를 활용하여 파이썬에서의 eof 처리를 해준다.
        string = input()
        for i in string:
            #딕셔너리로 alphabet이 나온 횟수를 기록해 준다.
            if i in alphabets:
                alphabets[i] += 1
            else:
                alphabets[i] = 1
    except:
        break

if ' ' in alphabets:
    #딕셔너리에 빈칸이 있는 경우에는 빈칸의 횟수는 제외해준다.
    del(alphabets[' '])
max_alpha = max(alphabets.values()) #alphabet 딕셔너리에 있는 값들 중 최대로 나온 alphabet의 횟수

final = [] #최대 횟수로 나온 alphabet들을 저장
for j in alphabets:
    if alphabets[j] == max_alpha:
        final.append(j)

final.sort() #문자 순서대로 sort
for k in final:
    #final에 있는 문자들 출력
    print(k, end = '')