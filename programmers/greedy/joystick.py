# 탐욕법 조이스틱 2022-01-09
# 테스트 케이스 추가로 인한 수정 2022-01-23

def solution(name) :
    answer = 0
    Lenght = len(name)
    min_move = Lenght - 1
    for index, value in enumerate(name) :
        if value != 'A' :
            if ord(value) - ord('A') <= 13 :
                answer += ord(value) - ord('A')
            else :
                answer += 26 - (ord(value) - ord('A'))

    for i in range(Lenght) :   # i = 왼쪽에서 오른쪽으로 갔을때 도착하는 거리
        idx = i + 1
        while idx < Lenght and name[idx] == 'A' :
            idx += 1       # idx = A의 마지막 index, len(name) - idx = 뒤로 갔을떄 거리
        distance = min(i, len(name) - idx)
        min_move = min(min_move, i + len(name) - idx + distance)
    answer += min_move
    return answer
# move = n - 1
#     for idx in range(n):
#         next_idx = idx + 1
#         while (next_idx < n) and (name[next_idx] == 'A'):
#             next_idx += 1
#         distance = min(idx, n - next_idx)
#         move = min(move, idx + n - next_idx + distance)

name = 'AAABAAAAAA'
# print(solution(name))
# print(abs(ord('Z') - ord('A')))
# print(solution(name))

k = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = set(k)
k = list(k)
test = [0 for i in range(len(k))]

print(k)

