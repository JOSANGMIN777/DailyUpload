from collections import deque  # 덱을 임포트 해온다.

def solution(maps):
    answer = bfs(0,0,maps) # bfs 사용을 위해 따로 bfs라는 함수를 만들고 여기에 인자로 시작점(0,0)과 배열 maps를 전달
    return -1 if answer == 1 else answer # 축약한 if문 표현이다 answer이 최종적으로 1이라면 -1을 반환하고 아닐 경우 bfs 결과값을 반환.

def bfs(x,y,maps):
    que = deque() # deque를 초기화 해준다.
    dx = [-1,1,0,0] # 동서남북 탐색을 위한 델타X
    dy = [0,0,-1,1] # 델타Y
    que.append((x, y)) # que에 x,y를 한 세트로 넣어준다. 튜플로 감싸야 변경이 불가하기에 무결성을 위해 튜플을 쓴다.
    while que: # que가 모두 빌때까지 
        x,y = que.popleft() # deque의 가장 왼쪽이라는 말은 가장 먼저 들어있었다는 말
        for i in range(4): # 델타 탐색은 동서남북 4방향을 탐색하기에 range는 4
            nx = x + dx[i] # 기존 x에 dx의 4방향 즉 동서남북을 탐색한 방향을 더해 nx라는 새로운 변수에 추가
            ny = y + dy[i] # 이하동문
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]): # index out of range에러가 나지 않게 0 이상 마지막 인덱스 미만(for문 range설정할 때와 마찬가지)
                if maps[nx][ny] == 1: # 만약 델타로 탐색한 범위중 1이 있다면 길이므로 갈 수 있다
                    maps[nx][ny] = maps[x][y] + 1 # 갈 수 있는 길로 이동해나가며 1을 누적해서 더해간다. DP느낌
                    que.append((nx,ny)) # 위 조건들을 통과한 nx, ny를 또 다시 que에 넣으면 이동한 위치에서 또 다시 델타탐색을 하게 되고 끝에 다다르거나 더 이상 이동할 수 없을 때까지 탐색을 계속할 수 있다. 
    return maps[len(maps)-1][len(maps[0])-1] # 우측 하단에 상대방 진영이 있다고 했으므로 우측 하단의 좌표에 기록된 값을 리턴하면 누적되어있는 값이 리턴될 것이다. 
