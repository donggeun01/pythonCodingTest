# level 1 실패율

def solution(N, stages):
    answer = []
    failure = {i : 0 for i in range(1, N + 1)}
    for i in range(1, N + 1):
        failer = stages.count(i)
        successful = len(stages)
        if failer != 0:
            failure[i] = failer / successful
            stages = [k for k in stages if k != i]
            # for j in range(failer):
            #     stages.remove(i)

    sort_dict = sorted(failure.items(), key= lambda item: item[1], reverse=True)

    answer = [stage[0] for stage in sort_dict]

    return answer


result = solution(5, [4, 4, 4, 4])

print(result)
