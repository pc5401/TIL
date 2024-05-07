import sys
sys.stdin = open('파리퇴치.txt')
T = int(input())
########################################
'''
순회와 인덱싱을 이해하고 있는지 물어보는 문제였다.
쉬웠지만, 여러가지 배울 수 있었던 문제였다.
for문이 4중으로 중첩되면 부담되었지만, 
이 문제로 조금은 괜찮아진거 같다.
+
range(n-m+1)에서 +1을 해야지 원하는 인덱스까지 범위로 지정될 수 있다.
왜 그런지 고민하고 잊지말자.
'''
########################################
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