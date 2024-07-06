# 10816 숫자 카드 2 실버4

import sys
input = sys.stdin.readline

N = int(input())
N_List = [*map(int, input().split())]
M = int(input())
M_List = [*map(int, input().split())]

N_dict = {}

for i in N_List:
    if i in N_dict:
        N_dict[i] += 1
    else:
        N_dict[i] = 1

res = [0] * len(M_List)
for i,j in enumerate(M_List):
    if j in N_dict.keys():
        res[i] = N_dict[j]

print(*res)

# 이진탐색하다가 시간초과의 늪에 빠져 허우적거렸다.
# 이후 딕셔너리 쓰기를 시도하다가 딕셔너리는 키 값 조회가 안되면 무조건 에러가 나는 것을 확인해서
# 어떻게든 고쳐서 써보려했으나 시행착오들을 겪게되었다.
# enumerate와 dictionary에 대한 이해도가 높아졌음.