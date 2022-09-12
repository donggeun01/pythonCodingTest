"""
소수 찾기 프로그래머스 고득점 Kit 완전탐색
작성일 : 2021-10-31
"""
import math


def solution(numbers) :
    length = 1;
    numList = list(numbers)



def primary_number(cnt, val, answer) :
    if cnt == len(numbers) : return 0;
    for idx, value in enumerate(numbers) :
        ret = val
        if used[idx] == True :
            continue;
        ret += value
        used[idx] = True;
        if is_prime_number(int(ret)) == True :
            answer += 1;
        answer += primary_number(cnt= cnt+1, val=ret, answer=0)
    return answer;

def is_prime_number(x) :
    for i in range(2, int(math.sqrt(x))+1) :
        if x % i == 0 :
            return False;
    return True;

paper = "21035";
numbers = list(paper);
check = [False] * len(numbers)
answer = 0;

answer = primary_number(cnt= 0, check=check, val="", answer=0)

print(answer);

