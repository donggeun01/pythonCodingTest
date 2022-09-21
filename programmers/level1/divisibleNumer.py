# level 1 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    answer.sort()

    return answer if len(answer) else [-1]

result = solution([5, 9, 7, 10], 5)
# result = solution([2, 36, 1, 3], 1)
# result = solution([3,2,6], 10)

print(result)