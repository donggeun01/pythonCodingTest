# level 1 2016년 요일 구하기 (2016)

from datetime import datetime

def solution(a, b):

    day_of_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return day_of_week[datetime(2016, a, b).weekday()]

result = solution(5, 24)

print(result)