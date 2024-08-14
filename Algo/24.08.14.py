# 백준 1158 요세푸스 실버4

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
ans = []
queue = deque()
for i in range(1,N+1):
    queue.append(i)

while queue:
    queue.rotate(-(K))
    ans.append(str(queue.pop()))

print('<'+', '.join(ans)+'>')

# 위에서 rotate를 쓰니 시간이 1/33 으로 줄어들었다.
# rotate는 디폴트 방향이 앞쪽 인덱스를 뒤쪽에 이어붙히는게 아니라 뒤쪽인덱스를 앞으로 이어붙히는것이기때문에
# -를 써서 방향을 바꿔줘야한다.

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
ans = []
queue = deque()
for i in range(1,N+1):
    queue.append(i)

while queue:
    for i in range(K):
        queue.append(queue.popleft())
    ans.append(str(queue.pop()))

print('<'+', '.join(ans)+'>')

# 처음에 그대로 Queue로 하다가 시간초과나서 deque로 했다.
# 기존 요세푸스 코드를 조금 변형한 정도이지만 이것 또한 맞긴하다. 물론 rotate를 쓸때와 안쓸때 차이가 매우 크지만 말이다.
# rotate를 알게되어 매우 뿌듯하다.