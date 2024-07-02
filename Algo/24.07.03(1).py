# 2609 최대공약수와 최소공배수 브론즈1

def gcd(a,b):
    while b > 0:
        a,b = b, a % b
    return a

def lcm(a,b):
    ans = a*b
    return ans

A,B = map(int, input().split())
print(gcd(A,B))
print(lcm(A,B)//gcd(A,B))

# 유클리드 호제법 잊지말자 