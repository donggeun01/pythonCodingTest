# level 1 시저 암호

def solution(s, n):
    text = list(s)
    answer = ''

    for char in text:
        ASCII = ord(char)
        if ASCII == 32:
            answer += chr(ASCII)
            continue;
        caeasar = ASCII + n
        if char.isupper():
            answer += chr(caeasar) if caeasar <= 90 else chr(caeasar - 26)
        else:
            answer += chr(caeasar) if caeasar <= 122 else chr(caeasar - 26)

    return answer

result = solution("a B z", 4)

print(result)
