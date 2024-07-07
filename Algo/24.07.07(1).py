# 11723 집합 실버5

import sys
input = sys.stdin.readline


M = int(input())
S = set()
for i in range(M):
    List = list(input().split())
    C = List[0]
    if C == 'add':
        S.add(int(List[1]))
    elif C == 'remove':
        if int(List[1]) in S:
            S.remove(int(List[1]))
    elif C == 'check':
        if (int(List[1])) in S:
            print(1)
        else:
            print(0)
    elif C == 'all':
        S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif C == 'toggle':
        if int(List[1]) in S:
            S.remove(int(List[1]))
        else:
            S.add(int(List[1]))
    else:
        S = set()

# list는 연산의 수가 3,000,000까지만 가능해서 계속 메모리초과가 났다.
# 원래는 list를 받아서 다시 돌면서 했으나 받으면서 바로바로 조건을 수행하도록 바꾸었다.