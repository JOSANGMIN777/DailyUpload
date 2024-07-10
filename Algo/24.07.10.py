# 11399 ATM 실버4

import sys
input = sys.stdin.readline

def min_sum(p):
    curr_sum = 0
    total_sum = 0

    for val in range(len(p)):
        curr_sum += p[val]
        total_sum += curr_sum

    return total_sum

N = int(input())
Line = list(map(int, input().split()))
Line.sort()

print(min_sum(Line))

# 생각보다 간단하게 풀었어야했다. 괜히 순열 만들어서 풀었다가 시간초과만 4번...
# 그냥 오름차순 정렬하는게 가장 시간이 짧게 소요된다는 것을 알고 풀면됨
# total_sum += curr_sum 이건 가히 혁명이었다. 사고가 경직된 나에게 충격을 선사한... 2중 for문이나 while문으로 했었음... ㅠ