#문제
#길이가 같은 두개의 큐가 있다.
#작업 : 하나의 큐에서 pop해서 다른 큐에 insert 하는 한번의 과정
#각 큐의 합이 같을 때까지 이 작업을 한다고 할 때,
#필요한 작업의 최소 횟수는?
#단, 어떤 방법으로도 큐의 합이 같아지지 않으면, return -1
#오버플로우가 발생될 수 있으므로, long type 고려

#원리
#합이 더 큰 곳에서 작은 곳으로 옮겨나가자!

#후기
#처음에 그냥 queue로 두고 풀었는데 계속 시간초과가 떴다.
#dequeue의 popleft() 함수가 시간복잡도가 적다고 한다.

from collections import deque

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

def solution(queue1, queue2):
    queue_1 = deque(queue1)
    queue_2 = deque(queue2)

    sum1 = sum(queue_1)
    sum2 = sum(queue_2)
    
    cnt = 0
    while cnt <= (len(queue_1) + len(queue_2))*2:
        if sum1 == sum2:
            return cnt
        if sum1 < sum2:
            temp = queue_2.popleft()
            queue_1.append(temp)
            sum2 -= temp
            sum1 += temp
            cnt += 1
        if sum1 > sum2:
            temp = queue_1.popleft()
            queue_2.append(temp)
            sum1 -= temp
            sum2 += temp
            cnt += 1
    else:
        return -1

print(solution(queue1, queue2))