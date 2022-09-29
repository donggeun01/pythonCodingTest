# level 1 부족한 금액 계산하기

def solution(price, money, count):
    total = sum(p * price for p in range(1, count + 1))

    answer = total - money if total > money else 0

    return answer

result = solution(3, 20, 4)

print(result)
