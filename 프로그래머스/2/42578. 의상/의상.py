

def solution(clothes):

    closet = {}
    
    for key,val in clothes:
        if val in closet.keys():   
            closet[val] += [key]
        else:
            closet[val] = [key]
    answer = 1
    for val in closet.values():
        answer *= len(val)+1
        print(val)
    
    

    return answer-1