board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    stack = []

    cnt = 0
    for move in moves:
        i = 0
        while i != len(board):
            if board[i][move - 1] != 0:
                stack.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
            else:
                i += 1

        if len(stack) < 2:
            continue
        else:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                cnt += 2

    return cnt

print(solution(board, moves))
