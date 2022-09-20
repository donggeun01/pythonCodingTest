# level 1 두 정수 사이의 합

def solution(a, b):
    x = min(a, b)
    y = max(a, b)
    answer = 0
    for i in range(x, y + 1):
        answer += i

    return answer

# result = solution(3, 5)
# result = solution(3, 3)
result = solution(5, 3)

print(result)
