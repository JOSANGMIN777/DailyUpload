# 30802 웰컴 키트 브론즈3
import sys
input = sys.stdin.readline

N = int(input())
S,M,L,XL,XXL,XXXL = map(int,input().split())
T,P = map(int, input().split())
cnt = 0
T_List = [S,M,L,XL,XXL,XXXL]
for i in T_List:
    if i == 0:
        continue
    if i != 0 and i <= T:
        cnt += 1
    elif i > T:
        if i % T == 0:
            ans = i // T
            cnt += ans
        elif i % T != 0:
            ans = i // T
            cnt += (ans + 1)
print(cnt)
print(N // P, N % P)