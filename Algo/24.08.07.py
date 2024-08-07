# 백준 11725 트리의 부모 찾기 실버2

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
queue = deque()
queue.append(1)

while queue:
    current = queue.popleft()
    for v in graph[current]:
        if visited[v] == 0:
            visited[v] = current
            queue.append(v)

print('\n'.join(map(str, visited[2:])))

# 우선 문제 이해를 잘못해서 아니 왜 1이랑 6의 부모의 출력을 4라고 하지?? 1이 부모노드면 1이랑 연결된 노드들의 부모는 당연히 다 1 아니야? 
# 이러고 있었음 근데 사실은 그게 아니라 1번 노드를 제외한 2번 노드부터의 부모를 나타낸거기에 그런 출력값이 나온거였다...
# 현재 노드를 변수에 할당하고 해당 노드 인덱스의 링크드 리스트를 순회하면서
# 배열 안의 수에 해당하는 graph 인덱스에 현재 노드의 값을 추가하고 이후 배열안의 수를 차례로 큐에 넣는다.
# visited[1] = 1이라고 해야 나중에 6번 노드가서 graph[1]이 6으로 안바뀐다. 1번 노드의 부모는 없다는 것을 명시하려고 0으로 두면 나중에 헷갈릴수도있음
# 걍 1번의 부모는 자기자신이라고 하는게 오히려 이해하기 쉬울듯