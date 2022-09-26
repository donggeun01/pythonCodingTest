# level 1 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        count = 1
        for j in range(1, i):
            if i % j == 0:
                count += 1

        answer = answer + i if count % 2 == 0 else answer - i

    return answer

result = solution(13, 17)
# result = solution(24, 27)

print(result)