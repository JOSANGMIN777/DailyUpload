def solution(n):
    answer = 0
    end = 0
    interval = 0
    arr = []
    for num in range(1, n+1):
        arr.append(num)
    
    for start in range(n):
        while interval < n and end < n:
            interval += arr[end]
            end += 1
        if interval == n:
            answer += 1
        interval -= arr[start]
    return answer