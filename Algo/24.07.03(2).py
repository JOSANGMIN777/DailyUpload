# 11866 요세푸스 문제 0 실버5

import queue

N,K = map(int, input().split())
Q = queue.Queue() # 큐 사용법
for i in range(1,N+1):
    Q.put(i) # 1부터 N까지이므로 해당 범위 내에서 요소들을 Q에 put 한다.

result = []
while not Q.empty(): # 큐가 비게되면 탈출
    for _ in range(K-1): # k-1을 해야 0부터 헤아렸을때 정확한 인덱스를 가리킴
        Q.put(Q.get()) # k-1 범위내에서 get을 하면 처음 요소를 뽑고 그걸 put하면 마지막 요소로 이동 해당 반복이 끝나면 for문 탈출
    result.append(str(Q.get())) # 이걸 반복해서 K번째 요소를 result배열에 담을 수 있음


print('<', ', '.join(result),'>', sep='') # 출력을 쓸데없이 복잡하게 만든 문제