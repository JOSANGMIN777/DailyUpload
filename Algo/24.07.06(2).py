# 2164 카드2 실버4

import queue
Q = queue.Queue()

N = int(input())
for i in range(1,N+1):
    Q.put(i)

while Q.qsize() > 1:
    Q.get()
    card = Q.get()
    Q.put(card)

card = Q.get()
print(card)

# queue사용법과 while 조건문에 그냥 Q를 갖다 박으면 이미 import 해서 생성한 객체가 존재하기때문에 무한루프를 돈다는 사실 명심
# qsize(),isempty(),put(),get(),q.queue[0],q.queue[-1] 잊지말것