# level 1 신고 결과 받기 2022-08-18


def solution(sizes):
    maxLength = 0  # 가장 큰 길이
    length = 0  # 반대쪽 길이

    for size in sizes:
        minLength = min(size)
        if maxLength < max(size):
            maxLength = max(size)
        if minLength > length:
            length = minLength


    answer = maxLength * length

    return answer

a = [[60, 50], [30, 70], [60, 30], [80, 40]]

b = solution(a)

print(b)