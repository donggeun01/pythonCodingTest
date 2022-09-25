# level 1 문자열 내림차순

def solution(s):
    strList = list(s)
    strList.sort(reverse=True)

    return ''.join(strList)

result = solution('Zbcdefg')

print(result)
