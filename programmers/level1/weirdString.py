# level 1 이상한 문자열 만들기

def solution(s):
    answer = []

    words = s.split(' ')
    for word in words:
        character = list(word)
        for index in range(len(character)):
            if index % 2 == 0:
                character[index] = character[index].upper()
            else:
                character[index] = character[index].lower()

        answer.append(''.join(character))

    return ' '.join(answer)

result = solution("try hello world")

print(result)