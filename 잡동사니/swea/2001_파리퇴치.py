import sys
sys.stdin = open('파리퇴치.txt')
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for i in range(n)]
    
    max_total = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0

            for ii in range(m):
                for jj in range(m):
                    total += lst[i+ii][j+jj]

            if total >= max_total:
                max_total = total
            else:
                pass

    print(f'#{tc} {max_total}')