def solution(brown, yellow):
    answer = []
    carpet = brown+yellow
    for height in range(1, carpet+1):
        if carpet % height == 0:
            width = carpet // height
            
            if (width-2) * (height-2) == yellow:
        
                return [width, height]