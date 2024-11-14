def solution(board):
    answer = 0
    
    dx = [-1, 0, 1,1,1,0,-1,-1]
    dy = [-1,-1,-1,0,1,1, 1, 0]
    for i in range(len(board)):
        for j in range(len(board[0])):
            for k in range(8):
                nx, ny = dx[k] + i, dy[k] + j
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[i][j] == 1 and board[nx][ny] != 1:
                        board[nx][ny] = 2
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                answer += 1
    
    return answer