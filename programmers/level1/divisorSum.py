# level 1 약수의 합 2022-09-13

def solution(n):
    answer = 0
    divisor = [n]
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisor.append(i)

    answer = sum(divisor)

    return answer

result = solution(12)
# result = solution(5)

print(result)
