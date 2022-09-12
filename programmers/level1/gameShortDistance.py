# level 1 게임내 최단거리 2022-08-17

from collections import deque


def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    goal = False
    queue = deque()

    queue.append((0, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 범위를 벗어났을 때
                continue
            if maps[nx][ny] == 0:  # 벽을 만났을 떄
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                if n - 1 == nx and m - 1 == ny:
                    goal = True

    if goal:
        answer = maps[n - 1][m - 1]

    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

result = solution(maps)

print(result)
