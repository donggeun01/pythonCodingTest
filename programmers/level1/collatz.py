# level 1 콜라츠 추측 2022-09-19

def solution(num):
    number = num
    answer = 0
    while True:
        if number == 1:
            break
        elif answer == 500:
            answer = -1
            break

        answer += 1
        if number % 2 == 0:
            number = number // 2
        elif number % 2 != 0:
            number = number * 3 + 1

    return answer

result = solution(626331)

print(result)