# level 1 K번째 수

def solution(array, commands):
    answer = []
    for command in commands:
        numbers = [array[i] for i in range(command[0] - 1, command[1])]
        numbers.sort()
        answer.append(numbers[command[2] - 1])

    return answer


numList = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

result = solution(numList, commands)

print(result)
