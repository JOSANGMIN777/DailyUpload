import math
def solution(n, words):
    answer = []
    spoken = []
    spoken.append(words[0])
    for i in range(1, len(words)):
        if words[i] in spoken or words[i-1][-1] != words[i][0] or len(words[i]) == 1:
            if (i+1)%n != 0:
                answer.append((i+1)%n)
            else:
                answer.append(n)
            answer.append(math.ceil((i+1)/n))
            break
        else:    
            spoken.append(words[i])
    if not answer:
        answer.extend([0,0])
    return answer