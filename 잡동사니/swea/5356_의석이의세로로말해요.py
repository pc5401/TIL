import sys
sys.stdin = open('의석이의세로로말해요.txt', 'r')

########################################
'''
파이썬의 try, except을 사용하면 손쉽게 풀 수 있지만,
그냥 연습한다는 생각으로 이것저것 시도해본 문제다.
+ 전치 행렬 : lst = list(zip(*arr))
+ 함수 만들어 보기
+ 공백이 포함된 경우 indexerror 안 나게 슬라이싱하기 등
'''
########################################


# 함수 만들기 my_max, my_len
def my_len(lst):
    cnt = 0
    for i in lst:
        cnt += 1
    return cnt

def str_longest(lst):
    maxi = 0
    for i in range(my_len(lst)):
        cnt = 0
        for j in range(my_len(lst[i])):
            cnt += 1
        if cnt >= maxi:
            maxi = cnt
    return maxi


T = int(input())

for tc in range(1,T+1):
    str_lst = [input() for i in range(5)]
    lenth = str_longest(str_lst)

    arr = [ [ '' for j in range(lenth) ] for i in range(5)]
    
    for i in range(5):
        for j in range(lenth):
            if j >= my_len(str_lst[i]):
                arr[i][j] = ''
            else:
                arr[i][j] = str_lst[i][j]
    
    lst = list(zip(*arr))

    print(f'#{tc}',end=" ")
    for i in range(my_len(lst)):
        for j in range(5):
            print(lst[i][j], end="")
    print()

