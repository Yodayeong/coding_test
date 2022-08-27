#단어 공부

#문제
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

#입력
#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

#출력
#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = input()

word_list = dict()
for i in word:
    if i.upper() not in word_list and i.lower() not in word_list:
        #단어의 대소문자가 모두 word_list에 없는 경우에 dict에 추가해줌
        word_list[i.upper()] = 1
    else:
        #단어의 대문자가 dict에 있으면 수를 1 증가시켜줌
        word_list[i.upper()] += 1

max_num =  0
for i in word_list:
    #딕셔너리에 있는 문자들 중 가장 많은 횟수로 나온 문자를 찾는다.
    if word_list[i] > max_num:
        max_num = word_list[i]
#가장 많이 나온 문자를 찾는다.

check = 0
check_idx = 0
for i in word_list:
    if word_list[i] == max_num:
        #가장 많은 횟수와 일치하는 문자를 찾으면 check를 1 증가시키고 idx를 기록해준다.
        check += 1
        check_idx = i

if check == 1:
    #check가 1일 때만, idx를 출력
    print(check_idx)
else:
    print('?')