# level 1 정수 제곱근 판별 2022-09-13
import math

def solution(n):
    answer = 0
    square = math.sqrt(n)
    if float(square).is_integer():
        answer = math.pow(int(square) + 1, 2)
    else:
        answer = -1

    return answer

result = solution(144)
# result = solution(3)

print(result)