# level 1 자연수 뒤집어 배열로 만들기 2022-09-14

def solution(n):
    answer = []
    number = str(n)
    for i in range(1, len(number) + 1):
        answer.append(int(number[i * -1]))

    return answer


result = solution(123)

print(result)
