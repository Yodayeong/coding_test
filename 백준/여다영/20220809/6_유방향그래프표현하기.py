#유방향 그래프 표현하기

#그래프 입력이 주어질 때 유방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.

#첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  
#둘째 줄부터 M개의 줄에 간선의 시작점 u와 끝점 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 

#인접 행렬을 출력하고, 인접 리스트를 출력하세요.

#유방향 인접행렬은 들어오는 간선만 1로 체크

import sys
from pprint import pprint

sys.stdin = open('6_유방향그래프표현하기.txt', 'r')

##-----
#Adjacency Matrix
N, M = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    #edge들을 모두 체크
    u, v = map(int, input().split())

    #유방향이기 때문에 (노드u -> 노드v)인 간선만 체크해주면 됨.
    matrix[u][v] = 1
pprint(matrix)

##-----
#Adjacency List
N, M = map(int, input().split())
list = [[] for _ in range(N + 1)]

for i in range(M):
    #edge들을 모두 체크
    u, v = map(int, input().split())

    #유방향이기 때문에 (노드u -> 노드v)인 간선만 체크해주면 됨.
    list[u].append(v)
print(list)