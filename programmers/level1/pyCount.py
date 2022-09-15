# level 1 문자열 내 p와 y의 개수 2022-09-15

def solution(s):
    pCount = s.count('p') + s.count('P')
    yCount = s.count('y') + s.count('Y')

    return True if pCount == yCount else False

result = solution('pPoooyY')
# result = solution('Pyy')

print(result)
