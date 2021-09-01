def solution(scores):
    answer = ""
    num = len(scores)
    avgs = []
    scores = [list(x) for x in zip(*scores)] # 행렬길이가 똑같은 리스트에대해 transpose
    
    for i in range(num):
        s = scores[i]
                
        if (max(s) == s[i] or min(s) == s[i]) and s.count(s[i]) == 1: 
            avgs.append((sum(s) - s[i]) / (num - 1))
        else:
             avgs.append(sum(s) / num)
    
    for i in avgs:  answer += "A" if i >= 90 else "B" if i>= 80 else "C" if i >= 70 else "D" if i >= 50 else "F" 
    return answer