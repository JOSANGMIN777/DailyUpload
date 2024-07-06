# 1920 수 찾기 실버4

def binary(arr, target):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(input())
N_List = list(map(int,input().split()))
M = int(input())
M_List = list(map(int,input().split()))
ans = [0] * len(M_List)
N_List.sort()

for i, value in enumerate(M_List):
    if binary(N_List, value):
        ans[i] = 1
for i in ans:
    print(i)

# 이진탐색을 활용해야 하는 문제