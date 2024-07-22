# 11724 연결 요소의 갯수 실버2

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(start, visited):

    visited[start] = 1
    for node in nodes[start]:
        if visited[node] == 0:
            dfs(node, visited)
    return

N,M = map(int, input().split())
nodes = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1
for i in range(M):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i, visited)
        cnt += 1

# dfs(1, visited)
# if visited.count(0) != 1:
#     for i in range(2, N+1):
#         for j in nodes[i]:
#             if visited[j] != 1:
#                 dfs(j,visited)
#                 cnt += 1

print(cnt)


# 주석처리 해놓은게 내 코드인데... 솔직히 극혐이긴 하다.
# 아니 근데 똑같이 동작하는거같은데 왜 내껀 안되는건데에 도대체
# 질문등록해놨으니 궁금증은 이후에 해결하자
# 기존 bfs에서 살짝 변형한건데 꽤 오래걸렸다. 아직 외워서 코드 치나? 생각도 들고
# 나는 취직할 수 있을까 싶고 생각이 많아지는데 코드도 40%에서 틀려서 상당히 스트레스 받는 하루였다.