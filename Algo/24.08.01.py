# 백준 5430 AC 골드5

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    P = input()
    N = int(input())
    X = input().strip()
    tmp = []
    string = ''
    for i in X:
        if i.isdigit():
            string += i
        elif i == ',':
            tmp.append(int(string))
            string=''
        elif i == ']':
            if string:
                tmp.append(int(string))

    queue = deque(tmp)
    reverse = False
    error = False
    for ch in P:
        if ch == 'R':
            reverse = not reverse
        elif ch == 'D':
           if queue:
               if reverse:
                   queue.pop()
               else:
                   queue.popleft()

           else:
               error = True
               print('error')
               break

    if not error:
        if reverse:
            queue.reverse()
        result = '['+ ','.join(map(str,queue))+']'
        print(result)

# 입출력이 매우 더러웠던 문제다 다신 보지말자
# 처음에 시간초과나 났는데 그 이유는 reverse를 중간중간 계속 해줬기 때문이다.
# pop과 popleft를 쓰면서 지우다가 마지막에 reverse를 쓰면 된다.
# 그래서 flag로 reverse 상태를 추적해 주어야했다.
# 그리고 error를 출력할 때 바로 break를 걸어줘야 오류 발생 후 루프가 계속되지 않는다.
# 그리고 error flag를 이용해서 최종 출력을 결정지어야지 if queue이걸로 하면 반례가 생겨서 에러가 난다.
# 정확한 이유는 아직 탐색중 마지막 출력부근과 시간초과 원인에서 gpt도움을 받았는데 gpt는 진짜 신인가