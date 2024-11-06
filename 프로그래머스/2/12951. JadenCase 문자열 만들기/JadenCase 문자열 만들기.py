def solution(s):
    string = s.split(' ')
    
    answer = ''
    for ch in range(len(string)):
        answer += string[ch].capitalize()
        if ch != (len(string)-1):
            answer += ' '
        
    
    return answer