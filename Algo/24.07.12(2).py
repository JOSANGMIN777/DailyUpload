# 1874 스택 수열 실버2

import sys
input = sys.stdin.readline



N = int(input())
stack = []
ans = []
cnt = 1
tmp = True

for _ in range(N):
    num = int(input())

    while cnt <= num:

        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    else:
        tmp = False
        break

if tmp == False:
    print('NO')

else:
    for i in ans:
        print(i)




