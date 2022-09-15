# level 1 정수 내림차순 배치 2022-09-15

def solution(n):
    numList = list(str(n))
    # numList.sort()
    # numList.reverse()
    numList.sort(reverse=True)

    answer = int(''.join(numList))

    return answer

result = solution(118372)

print(result)