import bisect

def solution(citations):
    answer = 0
    citations.sort()

    # 이진탐색을 이용한 h-index 찾기
    cLen = len(citations)
    start = 1 #  h인덱스의 최소값
    end = citations[-1] # 최대값


    while start<= end:
        middle = (start + end) // 2
        pos = bisect.bisect_left(citations, middle)

        if cLen - pos >= middle and pos <= middle:
            answer = middle
            start = middle +1
        else:
            end = middle - 1


    return answer