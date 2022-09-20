# level 1 서울에서 김서방 찾기

def solution(seoul):
    location = seoul.index("Kim")

    return f'김서방은 {location}에 있다'


result = solution(['Jane', 'Kim'])

print(result)
