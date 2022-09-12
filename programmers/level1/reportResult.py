# level 1 신고 결과 받기 2022-01-23

from collections import defaultdict
def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report = set(report)

    reported_dic = defaultdict(set)
    count_dic = defaultdict(int)
    nameList = set()

    for i in report:
        user, reported = i.split(' ')
        reported_dic[reported].add(user)
        count_dic[reported] += 1

        if count_dic[reported] == k:
            nameList.add(reported)

    for name in nameList :
        for i in reported_dic[name] :
            answer[id_list.index(i)] += 1
    print(answer)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

k = 2

solution(id_list, report, k)