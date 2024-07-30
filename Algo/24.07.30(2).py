# 백준 1697 숨바꼭질 실버1

import sys
from collections import deque
input = sys.stdin.readline

def bfs(visited):
    queue = deque()
    queue.append(N)
    while queue:
        curr = queue.popleft()
        if curr == K:
            return visited[curr]
        for i in (curr-1, curr+1, curr*2):
            if 0 <= i <= Max and not visited[i]:
                visited[i] = visited[curr] + 1
                queue.append(i)

N, K = map(int, input().split())
Max = 10 ** 5
visited = [0] * (Max+1)
print(bfs(visited))

# 진짜 씨발 visited배열에 0이 아니라 false넣었다고 틀렸다고 하는데 이유가 뭘까
# 0이 False고 False가 0아니었나? 암튼 7번 틀림 그거때문에
# 여기서 중요한건 우선 visited배열을 최대 입력만큼 생성해 놔야한다는것
# 그래서 백만개 생성함 ㅋㅋ
# 그리고 bfs 처음 해봤는데 생각보다 난이도가 있는거 같아 바리에이션이 많아서
# 신박한 코드인 for i in (curr -1, curr+1, curr*2)를 처음 발견함
# 이거대로 하면 저 세개의 범위에 해당하는 각 노드를 방문 할 수 있음
# 그렇게 방문하다가 curr에 해당하는 visited 값에 1을 더하고 그 값을 세개의 범위 노드들에 할당해줌
# 하위 노드들에 방문했냐 안했냐로 따지기 때문에 visited[curr]에는 다음 자식 노드로 갈 때마다 1이 추가됨
# 그러면 visited[i] 에는 계속해서 1이 늘어나고 있는 visited[curr]이 추가되는 것임
# 그렇게 계속하다가 target 노드에 다다르면 이제까지의 visited[curr]을 리턴해주면 몇번째만에 찾았는지 기록의 결과를 받을 수 있는것
#  