def solution(s):
    num_list = []
    ans_list = []
    answer = ''
    s = s.split(' ')
    for ch in range(len(s)):
        num_list.append(s[ch])
    for n in num_list:
        ans_list.append(int(n))
        
    answer = str(min(ans_list)) + ' ' + str(max(ans_list))

    
    return answer