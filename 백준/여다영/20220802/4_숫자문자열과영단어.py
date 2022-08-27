#숫자 문자열과 영단어

#네오와 프로도가 숫자놀이를 하고 있습니다. 
#네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

#다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

#1478 → "one4seveneight"
#234567 → "23four5six7"
#10203 → "1zerotwozero3"
#이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
#s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

#참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

import sys
sys.stdin = open('4_숫자문자열과영단어.txt', 'r')

s = input()

def solution(s):
    #replace 함수는 문자열만 취급하므로, 숫자들도 문자로 저장을 해준다.
    match = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    
    for i in match:
        if match[i] in s:
            #함수 이므로, 결과값을 꼬옥 s에 담아주자 !!!!!!!
            #절대 저절로 안바뀐다 !!!!!!!!!
            s = s.replace(match[i], i)
    return int(s)

print(solution(s))