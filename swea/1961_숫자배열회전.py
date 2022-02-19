import sys
from unittest import result
sys.stdin = open('숫자배열회전.txt')

T = int(input())
########################################
'''
인덱스 감을 완전히 잡았다고 할 수 는 없지만, 많이 배웠다.
특히 N-i-1 에서 '-1'이 필요하다는 것을 잊지말자.
그리고 머리로 이해가 안 가면 손으로 그려보자.
'''
########################################
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input().split()) for i in range(N)]

    matrix90 = [ [ 0 for i in range(N)] for i in range(N)]
    matrix180 = [ [ 0 for i in range(N)] for i in range(N)]
    matrix270 = [ [ 0 for i in range(N)] for i in range(N)]
    
    # 90도 회전
    for i in range(N):
        for j in range(N):
            # 90도 회전
            matrix90[i][j] = matrix[N-j-1][i]

            # 180도 회전
            matrix180[i][j] = matrix[N-i-1][N-j-1]

            # 270도 회전
            matrix270[i][j] = matrix[j][N-i-1]

    print(f'#{tc}')
    for k in range(N):
        result90 = ''.join(matrix90[k])
        result180 = ''.join(matrix180[k])
        result270 =''.join(matrix270[k])


        print(result90, end=' ')
        print(result180, end=' ')
        print(result270, end=' ')
        print()

