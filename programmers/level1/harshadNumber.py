# level 1 하샤드의 수 2022-09-16

def solution(x):
    harshad = True if x % sum(int(i) for i in str(x)) == 0 else False

    return harshad

result = solution(10)
# result = solution(12)
# result = solution(11)
# result = solution(13)

print(result)