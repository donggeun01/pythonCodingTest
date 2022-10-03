# level 1 문자열 내 마음대로 정렬

def solution(strings, n):

    strings.sort()
    return sorted(strings, key=lambda string: string[n])


# result = solution(["sun", "bed", "car"], 1)
result = solution(["abce", "abcd", "cdx"], 2)

print(result)