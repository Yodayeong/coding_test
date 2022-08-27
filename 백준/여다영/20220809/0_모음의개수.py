#모음의 개수

#문제
#영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 
#모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

#입력
#입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장이 주어진다. 
#각 줄은 최대 255글자로 이루어져 있다.

#입력의 끝에는 한 줄에 '#' 한 글자만이 주어진다.

#출력
#각 줄마다 모음의 개수를 세서 출력한다.

import sys
sys.stdin = open('0_모음의개수.txt', 'r')

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    cnt = 0
    string = input()

    if string == '#':
        break

    for vowel in vowels:
        cnt += string.count(vowel)
    print(cnt)