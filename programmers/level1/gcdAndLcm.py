# level 1 최대공약수 와 최소공배수

def gcd(x ,y):
    if y == 0:
        return y

    if x > y:
        if x % y != 0:
            return gcd(y, x % y)
        else:
            return y

    return gcd(y, x) if y > x else y

def solution(n, m):

    GCD = gcd(n, m)
    LCM = n * m // gcd(n, m)

    answer = [gcd(n, m), LCM]
    return answer

result = solution(2, 5)
print(result)

