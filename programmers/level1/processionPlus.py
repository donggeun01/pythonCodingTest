# level 1 행렬 더하기

def solution(arr1, arr2):
    answer = []
    for row in range(len(arr1)):
        item = []
        for col in range(len(arr1[row])):
            item.append(arr1[row][col] + arr2[row][col])

        if len(item):
            answer.append(item)

    return answer


# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]

arr1 = [[1],[2]]
arr2 = [[3],[4]]

result = solution(arr1, arr2)

print(result)
