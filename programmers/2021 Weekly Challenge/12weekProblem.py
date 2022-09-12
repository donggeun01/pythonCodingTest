from collections import deque;

def solution(k, dungeons):
    answer = 0;
    queue = deque()
    for i in range(len(dungeons)) :
        queue.append(i)
    while queue :
        hp = k;
        v = queue.popleft()
        count = 0;
        if hp - dungeons[v][1] >= 0 and hp >= dungeons[v][0] :
            hp = hp - dungeons[v][1];
            count += 1;
        for j in range(len(dungeons)) :
            if v == j :
                continue;
            if hp - dungeons[j][1] >= 0 and hp >= dungeons[j][0] :
                count += 1;
                hp = hp - dungeons[j][1];
        answer = count if answer < count else answer;

    return answer

k = 80;
# dungeons = [[80, 80], [210, 210], [200, 200], [100, 100], [60, 60], [30, 30], [299, 298], [10, 10]];
dungeons = [[80, 20], [50, 40], [30, 10]];

print(solution(k, dungeons))


