from collections import deque

def solution(maps):
    answer = bfs(0,0,maps)
    return -1 if answer == 1 else answer

def bfs(x,y,maps):
    que = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que.append((x, y))
    answer = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    que.append((nx,ny))
    return maps[len(maps)-1][len(maps[0])-1]