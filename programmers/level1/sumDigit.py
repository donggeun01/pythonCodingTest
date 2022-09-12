# level 1 자릿수 더하기 2022-09-12

def solution(n):
    sum = 0
    number = str(n)
    for i in range(len(number)):
        sum += int(number[i])
    return sum

answer = solution(123)

print(answer)
