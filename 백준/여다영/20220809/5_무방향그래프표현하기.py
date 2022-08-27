#무방향 그래프 표현하기

#그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.

#첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  
#둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 

#인접 행렬을 출력하고, 인접 리스트를 출력하세요.

#인접행렬
#간선들이 연결되어 있으면 1, 연결되어 있지 않으면 0
#각 간선들의 연결 여부를 양쪽으로 표현해 줘야 하므로, matrix는 (노드 수) * (노드 수)의 배열이다.

#인접리스트
#각 노드별 인접 간선들을 모두 체크

import sys
from pprint import pprint

sys.stdin = open('5_무방향그래프표현하기.txt', 'r')

##-----
#Adjacency Matrix
N, M = map(int, input().split())
#행렬을 모두 0으로 초기화
#왼쪽과 위쪽 테두리를 0으로 둘러줌.
matrix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    #edge들을 모두 체크
    u, v = map(int, input().split())

    #무방향이기 때문에 양방향 모두 체크
    matrix[u][v] = 1
    matrix[v][u] = 1
pprint(matrix)

##-----
#Adjacency List
N, M = map(int, input().split())
#노드 수 만큼 리스트 생성
#맨 앞에 빈 리스트도 하나 둠.
list = [[] for _ in range(N + 1)]

for i in range(M):
    #edge들을 모두 체크
    u, v = map(int, input().split())

    #무방향이기 때문에 양방향 모두 체크
    list[u].append(v)
    list[v].append(u)
print(list)