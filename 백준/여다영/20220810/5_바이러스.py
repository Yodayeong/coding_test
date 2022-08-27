#바이러스

#문제
#신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
#한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

#어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
#컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
#1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에는 컴퓨터의 수가 주어진다. 
#컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
#둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
#이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

#출력
#1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

#----
#무방향 adjacency list 활용
#dfs 탐색 활용

import sys
sys.stdin = open('5_바이러스.txt', 'r')

node = int(input())
edge = int(input())
adjacency_list = [[] for _ in range(node + 1)]

#undirected_adjecency_list 생성
for i in range(edge):
    u, v = map(int, input().split())

    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

#dfs 탐색
#1. stack에서 pop => 현재 노드
#2. 현재 노드의 adjacency_list 탐색
#3. 첫 방문 노드는 visited[True]와 stack에 append

visited = [False] * (node + 1) # visited도 adjacency_list와 마찬가지로 (node + 1) 개 만큼 만들어준다.

def dfs(start):
    cnt = 0

    stack = [start]
    visited[start] = True

    while stack: #stack에 아무 노드도 남아있지 않을 때까지
        now_node = stack.pop()
        for nodes in adjacency_list[now_node]:
            if visited[nodes] == False:
                visited[nodes] = True
                stack.append(nodes)
                cnt += 1

    return cnt

print(dfs(1))