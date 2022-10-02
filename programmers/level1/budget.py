# level 1 예산

def solution(d, budget):
    d.sort(reverse=True)
    answer = 0
    if budget >= sum(d):
        return len(d)

    while budget > 0:
        price = d.pop()
        budget -= price
        if budget >= 0:
            answer += 1
        else:
            break

    return answer

result = solution([1,3,2,5,4], 9)
# result = solution([2,2,3,3], 10)

print(result)
