#박스

#문제
#m행 n열로 이루어진 그리드가 주어진다. 일부 칸에는 박스가 들어 있다. 
#모든 박스가 더 이상 움직일 수 없을 때 까지 아래로 움직인다면, 박스는 쌓여진 상태가 된다.

#박스가 움직인 거리는 바닥에 쌓이기 전 까지 이동한 칸의 개수이다. 
#예를 들어, 맨 왼쪽 열에서 가장 위에 있는 박스가 움직인 거리는 2이다. 
#모든 박스가 이동한 거리 (각 박스가 이동한 거리의 합) 을 구하는 프로그램을 작성하시오.

#입력
#첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
#각 테스트 케이스의 첫째 줄에는 m과 n이 주어진다. (1 ≤ m, n ≤ 100) 
#다음 m개 줄에는 그리드의 각 행의 정보를 나타내는 n개의 정수가 주어진다. 
#그리드 첫 행부터 마지막 행까지 순서대로 주어진다. 박스가 들어있는 칸은 1로, 다른 칸은 0으로 주어진다. 
#각 정수 사이에는 공백이 하나 주어진다.

#출력
#각 테스트 케이스마다 입력으로 주어진 그리드에서 모든 박스가 이동한 거리를 출력한다.

import sys
sys.stdin = open('2_박스.txt', 'r')

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    matrix = [list(input().split()) for _ in range(n)]

    cnt = 0
    for i in range(m):
        j = n - 2
        print(j)
        while j >= 0:
            temp = i
            if matrix[j][i] == '1':
                print(matrix[j][i])
                temp = i
                while i < n:
                    if matrix[j][temp + 1] == '0':
                        cnt += 1
                        matrix[j][temp + 1] = '1'
                        matrix[j][temp] = '0'
                        temp += 1
            j -= 1
    print(cnt)
