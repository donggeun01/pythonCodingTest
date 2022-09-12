# level 1 나만의 카카오 성격유형검사 2022-08-18


def solution(survey, choices):
    score = {"R": 0, "T": 0, "F": 0, "C": 0, "M": 0, "J": 0, "A": 0, "N": 0}
    point = [3, 2, 1, 0, 1, 2, 3]
    characteristic = ["RT", "FC", "MJ", "AN"]
    answer = ""
    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] += point[choices[i] - 1]
        elif choices[i] > 4:
            score[survey[i][1]] += point[choices[i] - 1]

    for character in characteristic:
        if score[character[0]] > score[character[1]]:
            answer += str(character[0])
        elif score[character[0]] < score[character[1]]:
            answer += str(character[1])
        else:
            answer += chr(min(ord(character[0]), ord(character[1])))


    return answer


sur = ["AN", "CF", "MJ", "RT", "NA"]
chois = [5, 3, 2, 7, 5]

result = solution(sur, chois)

print(result)