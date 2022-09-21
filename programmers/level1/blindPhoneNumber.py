# level 1 핸드폰 번호 가리기

def solution(phone_number):
    blindSize = len(phone_number) - 4

    return ('*' * blindSize) + phone_number[-4:]


# result = solution("01033334444")
result = solution("027778888")

print(result)
