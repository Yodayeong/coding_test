#자료구조는 정말 최고야

#문제
#찬우는 스택을 배운 뒤 자료구조 과목과 사랑에 빠지고 말았다.

#자료구조 과목만을 바라보기로 다짐한 찬우는 나머지 과목의 교과서 N권을 방 구석에 M개의 더미로 아무렇게나 쌓아 두었다. 
#하지만 중간고사가 다가오자 더 이상 자료구조만 공부할 수는 없었고, 결국 찬우는 팽개쳤던 나머지 과목의 교과서를 정리하고 번호순으로 나열하려 한다.

#N권의 교과서는 각각 1부터 N까지의 번호가 매겨져 있다. 
#찬우는 각 더미의 맨 위에 있는 교과서만 꺼낼 수 있으며, 반드시 교과서를 꺼낸 순서대로 나열해야 하기 때문에 번호순으로 나열하기 위해서는 1번, 2번, … N - 1번, N번 교과서 순으로 꺼내야 한다. 
#교과서를 올바르게 나열할 수 없다면 중간고사 공부를 때려치겠다는 찬우를 위해 번호순으로 나열할 수 있는지 여부를 알려주는 프로그램을 작성해 주자.

#입력
#첫째 줄에 교과서의 수 N, 교과서 더미의 수 M이 주어진다.
#둘째 줄부터 2 * M줄에 걸쳐 각 더미의 정보가 주어진다.
#i번째 더미를 나타내는 첫 번째 줄에는 더미에 쌓인 교과서의 수 k_{i} 가 주어지며, 두 번째 줄에는 k_{i} 개의 정수가 공백으로 구분되어 주어진다.
#각 정수는 교과서의 번호를 나타내며, 아래에 있는 교과서의 번호부터 주어진다.
#교과서의 번호는 1부터 N까지의 정수가 한 번씩만 등장한다.

#출력
#올바른 순서대로 교과서를 꺼낼 수 있다면 Yes를, 불가능하다면 No를 출력한다.

import sys
sys.stdin = open('1_자료구조는정말최고야.txt', 'r')

N, M = map(int, input().split())

stack = []
#전체 stack 더미와
num = int(input())
for i in range(M):
    books = list(map(int, input().split()))
    #각각의 stack 더미들을 입력
    stack.append(books)

find = 1
array = []
#하나씩 위에서부터 차례로 pop 했을 때, 정렬해 줄 array
while find < N:
    #맨 마지막 하나는 상관이 없으므로 pop 한 책의 길이가 N - 1일 때까지
    for j in stack:
        if j[-1] == find:
            #각 stack 더미의 젤 위의 책이 해당 순서에 맞는 책이라면,
            array.append(j.pop())
            #pop해서 array에 추가해 준다.
            find += 1
            break
    else:
        #모든 stack 더미를 돌았지만, 해당 순서에 맞는 책이 없다면
        break
        #break 해준다.

if len(array) == N - 1:
    #정렬한 책의 수, 즉 array의 길이가 전체 책의 권수와 같다면
    print('Yes')
    #Yes 출력
else:
    #아니면
    print('No')
    #No 출력



##더 효율적인 코드
#각 stack이 오름차순으로 잘 정렬되어 있는지만 확인해주면 된다.
N, M = map(int, input().split())

answer = 'Yes'
#초기에 answer를 Yes로 둔다.
for i in range(M):
    #각 더미들을 돌면서
    length = int(input())
    stack = list(map(int, input().split()))

    compare = stack.pop()
    #비교 대상이 될(가장 작은) 수를 stack에서 pop해준다.
    while len(stack) != 0:
        #stack의 끝에 도달할 때까지
        if stack[-1] > compare:
            #stack의 다음 수가 비교 대상보다 크면 => 오름차순으로 잘 정렬되어 있으면
            compare = stack.pop()
            #다음 비교대상을 pop 한다.
        else:
            #그게 아니면 answer를 No로 바꾸고 break 한다.
            answer = 'No'
            break
print(answer)