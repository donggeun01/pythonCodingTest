# level 1 수박수박수박수박수박수?

def solution(n):
    answer = ''
    if n % 2 == 1:
        answer = '수박' * (n // 2) + '수'
    else:
        answer = '수박' * (n // 2)

    return answer

result = solution(4)

print(result)
