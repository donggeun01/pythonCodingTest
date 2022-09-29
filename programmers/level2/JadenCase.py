# level 2 JadenCase 문자열 만들기

def solution(s):

    answer = [i.capitalize() for i in s.split(' ')]

    return ' '.join(answer)

result = solution('3people unFollowed me')

print(result)
