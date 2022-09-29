# level 1 직사각형 별찍기

a, b = map(int, input().strip().split(' '))

for row in range(b):
    print('*' * a)