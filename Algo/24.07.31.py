# 백준 14940 쉬운 최단거리 실버1

import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_x, start_y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 0
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if Map[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif Map[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

    return -1

N,M = map(int,input().split())
Map = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if Map[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()

# 이제 슬슬 어려워지는듯... 코드가 40줄이 넘어가기 시작했다.
# 당연히 못풀었고 이걸 완벽히 이해해야할듯하다. 정답으로 프린트 찍는거조차 쉽지 않다.


#우선 



# 우선 bfs에 원래 도달할 수 없는 위치거나 도착 위치인 경우 두 가지 일때 해당 좌표를 시작점으로 넣는다.
# 그러면 bfs에서 해당 시작점을 visited배열에 -1이라고 넣고 deque을 불러와서 시작좌표를 큐에 넣고 시작한다.
# 그리고 델타순회를 하면서 만약 범위안에 있고 visited가 -1일 경우 4방향에 대한 탐색을 한다.
# 그리고 0인 경우에는 0을 visited에 기록하고 1인 경우 이전 visited좌표에서 델타탐색하는 좌표에 1을 더하고 탐색한다.
# 여기서 탐색이라고 하는 것은 queue에 append하는 것을 말함 그래야 큐에 넣었다 뺌으로써 또 델타탐색할 수 있기 때문에
# 그리고 0인경우와 아닌 경우를 나눠서 print 해준다.