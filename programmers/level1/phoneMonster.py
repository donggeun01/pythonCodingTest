# level 1 폰켓몬

def solution(nums):
    max_count = len(nums) // 2
    monster = len(set(nums))
    answer = monster if monster <= max_count else max_count

    return answer

# result = solution([3,1,2,3])
# result = solution([3,3,3,2,2,4])
result = solution([3,3,3,2,2,2])

print(result)
