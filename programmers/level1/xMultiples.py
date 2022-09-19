# level 1 x간격의 n개의 숫자 2022-09-19

def solution(x, n):
    multiples = x
    answer = []
    for i in range(n):
        answer.append(multiples)
        multiples += x

    return answer


# result = solution(2, 5)
# result = solution(4, 3)
result = solution(-4, 2)

print(result)