# level 1 문자열 다루기 기본

def solution(s):
    strLen = len(s)
    if strLen == 4 or strLen == 6:
        return s.isdigit()

    return False

result = solution("1234")

print(result)

