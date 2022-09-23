# level 1 제일 작은 수 제거하기

def solution(arr):
    answer = []
    if len(arr) > 1:
        arr.remove(min(arr))
        answer = arr
    else:
        answer.append(-1)
    return answer

result = solution([4, 3, 2, 1])
# result = solution([10])

print(result)
