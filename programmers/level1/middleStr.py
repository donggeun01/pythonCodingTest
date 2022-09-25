# level 1 가운데 글자 가져오기

def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        index = len(s) // 2 - 1
        answer = s[index] + s[index + 1]
    else:
        answer = s[len(s) // 2]

    return answer


result = solution('abcde')
# result = solution('qwer')

print(result)
