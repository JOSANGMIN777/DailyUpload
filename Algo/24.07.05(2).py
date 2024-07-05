import sys
input = sys.stdin.readline

def binary(List, Max, N):
    start = 1
    end = Max
    result = 0
    while start <= end:
        mid = (start+end) // 2
        if not check(List, mid, N):
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


def check(List, target, N):
    res = 0
    for j in range(len(List)):
        res += List[j] // target
    if res >= N:
        return True
    else:
        return False

K, N = map(int, input().split())
List = []

for i in range(K):
    List.append(int(input()))

Max = max(List)
List.sort()

print(binary(List, Max, N))

# while문의 동작 순서를 잘 이해해야하며 while문 탈출 조건을 충족하기 전에 이미 정답값인 mid값이 나올 수 있다는 것을 알고 mid값 자체를 리턴하면 안된다. 어디다 저장해놨다가 리턴해야함