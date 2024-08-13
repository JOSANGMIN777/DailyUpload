# 백준 1629 곱셈 실버1

import sys
input = sys.stdin.readline

def sol(A,B,C):
    if B == 1:
        return (A%C)

    else:
        K = sol(A,B//2,C)
        if B % 2 == 0:
            return (K*K)%C
        else:
            return(K*K*A)%C


A, B, C = map(int, input().split())
print(sol(A,B,C))

# 지수법칙을 활용한 문제
# 그냥 B가 짝수일 때 2로 나눈걸 두번 곱하고 
# 홀수일 때 2로 나누고 A를 곱한걸 C로 나누기만하면 되는 문제였지만
# while문으로 최소 지수 2에서 2로 나눈 몫과 그렇지 않을 때의 나머지를 따로 받아서 쓰다가 계속 틀렸다.
# 수학적인 사고방식이 부족한듯하다... ㅠ 