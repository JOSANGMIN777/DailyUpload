# 백준 16953 A -> B 실버2

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1
flag = True

while B != A:
    if B < A:
        flag = False
        break
    elif B % 2 == 0:
        B = B // 2
    elif str(B)[-1] == '1':
        B = int(str(B)[:-1])
    else:
        flag = False
        break
    cnt += 1

if flag:
    print(cnt)
else:
    print(-1)

# 조건문에서 조건의 순서가 중요하다는 것을 깨달았다.
# 자꾸 무한루프 돌길래 빡쳤었는데 gpt가 문제를 한번에 알려줌...
# 탈출조건을 앞에다가 쓰도록 하자 그래야 뻘짓하면서 탈출조건 전에 단계에서 무한루프 안돈다.