# level 1 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        row = ''
        map1 = format(arr1[i], 'b').zfill(n)
        map2 = format(arr2[i], 'b').zfill(n)
        for j in range(n):
            if map1[j] == '1' or map2[j] == '1':
                row += '#'
            else:
                row += ' '
        answer.append(row)

    return answer


result = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
# result = solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])

print(result)
