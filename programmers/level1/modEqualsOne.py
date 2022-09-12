# level 1 나머지가 1이 되는 수 2022-09-12

def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break

    return answer
