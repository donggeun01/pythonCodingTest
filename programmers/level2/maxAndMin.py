# level 2 최댓값과 최솟값

def solution(s):
    numberList = list(map(int, s.split(' ')))
    maxStr = str(max(numberList))
    minStr = str(min(numberList))

    return f"{minStr} {maxStr}"


result = solution('1 2 3 4')
# result = solution('-1 -2 -3 -4')
# result = solution('-1 -1')

print(result)
