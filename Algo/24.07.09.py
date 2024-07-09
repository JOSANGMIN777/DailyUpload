# 엘리스 코딩경진대회 2회차 정리정돈을 좋아하는 k씨

def slice(List, i, j, k):
    k_list = List[(i-1):j]
    k_list.sort()
    return k_list[k-1]


N, M = map(int,input().split())
List = list(map(int,input().split()))
for _ in range(M):
    i,j,k = map(int,input().split())
    print(slice(List, i, j, k))

# 나도 내일부터는 10시 땡치면 시작할거다 이놈들아
# 유클리드 호제법을 굳이 사용해야하는 부분인지 잘 모르겠슈...