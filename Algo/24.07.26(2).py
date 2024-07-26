# 11074 동전 0 실버4

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coins = []
for i in range(N):
    coin = input().strip()
    coin = int(coin)
    if coin <= K:
        coins.append(coin)
cnt = 0


while K != 0:

    if coins:
        if coins[-1] <= K:
            cnt += K // coins[-1]
            K %= coins[-1]
        else:
            coins.pop()

print(cnt)

# while 부분에서 cnt를 더하고 K의 값을 뺄 때 나누기를 사용해야한다. 
# 그냥 단순하게 빼기로만 생각했더니 시간초과가 발생했다. 개같은...
# 여기서 중요했던 점은 coins배열이 비어있지 않은 경우를 전제로 if문을 작성해야 index out of range 에러가 발생하지 않는다는 점이다.
# 파이썬이 만약에 비어있으면요? 그러면 어떡해요? 이러는거기 때문에 칭얼거리지 않게 미리 손을 써줘야 한다.