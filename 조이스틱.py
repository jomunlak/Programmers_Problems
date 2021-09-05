def solution(name):
    answer = 0
    nLen = len(name)
    for i in range(nLen):
        answer += min((ord(name[i]) - ord('A')), 26 - (ord(name[i])-ord('A')))
    
    n = len(name)
    left_or_right = n-1
    
    for i in range(n): # 모든 문자에대해 조사.
        _next = i + 1 
        while _next < n and name[_next] == 'A':
            _next += 1 
            # 현재 문자의 오른쪽에서 'A'가 아닌 가장 가까운 문자를 찾는 코드
        
        # i : 왼쪽 끝에서부터 탐색한 문자의 개수
        # n - _next : 오른쪽 끝에서부터 _next의 위치 탐색한 문자 개수
        left_or_right = min(left_or_right, i + n - _next + min(i, n-_next)) 
        #조이스틱 위치가 갔다가 돌아오기때문에 min(i, n - _next)를 더해준다.
    answer += left_or_right
    return answer